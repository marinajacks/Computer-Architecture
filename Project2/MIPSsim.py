'''/* On my honor, I have neither given nor received unauthorized aid on this assignment */'''

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:34:12 2017
This program used to 
@author: 陈彪
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:53:40 2017

@author: 陈彪
Copyright © 2017 - ChenBiao. All Rights Reserved
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

执行该程序后,然后只要给出inputfilename.txt的绝对路径path即可
使用SIMPsim(path)来完成需要的功能。

This is a  script file write by chenbiao.
"""
#首先设计输出为rd,rs,rt类型的数据
def getsource1(s):
    rd='R'+str(int(s[16:21],2))
    rs='R'+str(int(s[6:11],2))
    rt='R'+str(int(s[11:16],2))
    ss=' '+rd+', '+rs+', '+rt
    return ss

#输出类型为rt,rs,im类型的数据
def getsource2(s):
    rs='R'+str(int(s[6:11],2))
    rt='R'+str(int(s[11:16],2))
    im='#'+str(int(s[16:32],2))
    ss=' '+rt+', '+rs+', '+im
    return ss

#二进制补码转化成十进制
def com2dec(s):
    if(s[0]=='0'):
        ss=str(int(s,2))
    elif(s[0]=='1'):
        s1=[]
        for i in range(1,len(s)):
            if(s[i]=='0'):
                s1.append('1')
            elif(s[i]=='1'):
                s1.append('0')
        ss='-'+str(int(''.join(s1),2)+1)
    return ss


#获取模拟指令信息
def getnames(s):
    s2=s[0:6]  #获取操作符代码
    if(s2=='010000'):
        ss='J'+' #'+str(int(s[6:32],2)<<2)
    elif(s2=='010001'):
        ss='JR'+' R'+str(int(s[6:11],2))  #JR rs
    elif(s2=='010010'):
        ss='BEQ'+' R'+str(int(s[6:11],2))+', R'+str(int(s[11:16],2))+', #'+str(int(s[16:32],2)<<2)
    elif(s2=='010011'):
        ss='BLTZ'+' R'+str(int(s[6:11],2))+', #'+str(int(s[16:32],2)<<2)
    elif(s2=='010100'):
        ss='BGTZ'+' R'+str(int(s[6:11],2))+', #'+str(int(s[16:32],2)<<2)
    elif(s2=='010101'):
        ss='BREAK'
    elif(s2=='010110'):
        ss='SW'+' R'+str(int(s[11:16],2))+', '+str(int(s[16:32],2))+'(R'+str(int(s[6:11],2))+')'
    elif(s2=='010111'):
        ss='LW'+' R'+str(int(s[11:16],2))+', '+str(int(s[16:32],2))+'(R'+str(int(s[6:11],2))+')'
    elif(s2=='011000'):
        ss='SLL'+' R'+str(int(s[16:21],2))+', R'+str(int(s[11:16],2))+', #'+str(int(s[21:26],2))
    elif(s2=='011001'):
        ss='SRL'+' R'+str(int(s[16:21],2))+', R'+str(int(s[11:16],2))+', #'+str(int(s[21:26],2))
    elif(s2=='011010'):
        ss='SRA'+' R'+str(int(s[16:21],2))+', R'+str(int(s[11:16],2))+', #'+str(int(s[21:26],2))
    elif(s2=='011011'):
        ss='NOP'
    elif(s2=='110000'):
        ss='ADD'+getsource1(s)
    elif(s2=='110001'):
        ss='SUB'+getsource1(s)
    elif(s2=='110010'):
        ss='MUL'+getsource1(s)
    elif(s2=='110011'):
        ss='AND'+getsource1(s)
    elif(s2=='110100'):
        ss='OR'+getsource1(s)
    elif(s2=='110101'):
        ss='XOR'+getsource1(s)
    elif(s2=='110110'):
        ss='NOR'+getsource1(s)
    elif(s2=='110111'):
        ss='SLT'+getsource1(s)
    elif(s2=='111000'):
        ss='ADDI'+getsource2(s)
    elif(s2=='111001'):
        ss='ANDI'+getsource2(s)
    elif(s2=='111010'):
        ss='ORI'+getsource2(s)
    elif(s2=='111011'):
        ss='XORI'+getsource2(s)
    else:
        ss=com2dec(s)
    return ss

def MIPSsimulation(fadds,adds,s,a,b):
    """fadds是初始data地址,adds是地址,s是二进制指令集合,
       表里边的a是register信息,b是data信息
    """
    op=s[0:6]
    rd=(int(s[16:21],2))
    rs=(int(s[6:11],2))
    rt=(int(s[11:16],2))
    sa=(int(s[21:26],2))
    im=(int(s[16:32],2))
    if(op=='010000'):#J
        adds=(int(s[6:32],2)<<2)  #Jump to the target
    elif(op=='010001'):#JR
        adds=a[rs]
    elif(op=='010010'):#BEQ
        if(a[rs]==a[rt]):
            adds=adds+(im<<2)
        adds=adds+4
    elif(op=='010011'):#BLTZ
        if(a[rs]<0):
            adds=adds+(im<<2)
        adds=adds+4
    elif(op=='010100'):#BGTZ
        if(a[rs]>0):
            adds=adds+(im<<2)
        adds=adds+4
    elif(op=='010101'): #BREAK
        pass   #如果是break的话不做操作
    elif(op=='010110'):#SW    
        tmp=int((a[rs]+im-fadds)/4) 
        b[tmp]=a[rt]   #将a[rt]对应的数据存入缓存表中
        adds=adds+4
    elif(op=='010111'):#LW  
        tmp=int((a[rs]+im-fadds)/4) 
        a[rt]=b[tmp]    #将data中的数据写入到a[rt]中
        adds=adds+4
    if(op=='011000'):#SLL
        a[rd]=(a[rt])<<sa
        adds=adds+4
    elif(op=='011001'):#SRL
        a[rd]=(a[rt])>>sa#logical
        adds=adds+4
    elif(op=='011010'):#SRA
        a[rd]=(a[rt])>>sa#arithmetic
        adds=adds+4
    elif(op=='011011'):#NO
        pass
        #To perform no operation.
    elif(op=='110000'):#ADD
        a[rd]=a[rs]+a[rt]
        adds=adds+4
    elif(op=='110001'):#SUB
        a[rd]=a[rs]-a[rt]
        adds=adds+4
    elif(op=='110010'):#MUL
        a[rd]=a[rs]*a[rt]
        adds=adds+4
    elif(op=='110011'):#AND
        a[rd]=a[rs]&a[rt]
        adds=adds+4
    elif(op=='110100'):#OR
        a[rd]=a[rs]|a[rt]
        adds=adds+4
    elif(op=='110101'):#XOR
        a[rd]=a[rs]^a[rt]
        adds=adds+4
    elif(op=='110110'):#NOR
        a[rd]=~(a[rs]|a[rt])
        adds=adds+4
    elif(op=='110111'):#SLT
        a[rd]=(int)(a[rs]<a[rt])
        adds=adds+4
    elif(op=='111000'):#ADDI
        a[rt]=a[rs]+im
        adds=adds+4
    elif(op=='111001'):#ANDI
        a[rt]=a[rs]&im
        adds=adds+4
    elif(op=='111010'):#ORI
        a[rt]=a[rs]|im
        adds=adds+4
    elif(op=='111011'):#XORI
        a[rt]=a[rs]^im
        adds=adds+4
    return adds,a,b
#MIPS Spase function
'''mac操作系统的地址格式与win操作系统的格式是不一样的,
这里在mac下的脚本需要进行调整才行
'''
def MIPSparse(p1):  
    adds=256
    try:
        f1=open(p1,'r')
    except IOError:
        print("No such file or directory "+p1)
    else:
        if(('/') in p1):
            p2=p1.replace(p1.split('/')[-1],'disassembly.txt')
        else:
            p2=p1.replace(p1.split('//')[-1],'disassembly.txt')
        f=open(p2,'w')
        lines=f1.readlines()
        for i in range(len(lines)):
           f.write(lines[i].strip()+'\t'+str(adds+4*i)+'\t'+getnames(lines[i])+'\n')
        f.close()
#MIPS simulation function
 
def MIPSsimulations(p1):
    try:
        f=open(p1,'r')
    except IOError:
        print("No such file or directory "+p1)
    else:
        if(('/') in p1):
        #由于mac系统和win系统存在地址的差异,这个需要对win程序下的软件进行调整
        #才可以执行这个操作,否则会导致数据存在异常
            p2=p1.replace(p1.split('/')[-1],'simulation.txt')  
        else:
            p2=p1.replace(p1.split('//')[-1],'simulation.txt')
        f1=open(p2,'w')
        lines=f.readlines()
        adds0=256
        reg=[]
        for i in range(32):
            reg.append(0)  #Initialized register Data
        mem=[]
        j=0
        for k in range(len(lines)):
            if(lines[k][0:6]=='010101'):
                j=k
        fadds=adds0+(j+1)*4 #first data address
        for l in range(j+1,len(lines)):
            mem.append(int(getnames(lines[l]))) #Initialized memory Data
        instrs=[]
        for i in range(len(lines)):
            s=[adds0+4*i]
            s.append(lines[i].strip())
            instrs.append(s) #get instruction from file
            
        I=0
        J=0
        adds,reg,mem=MIPSsimulation(fadds,adds0,instrs[I][1],reg,mem)
        adds=adds0   #Initialized Data Information
        while(1):
            adds,reg,mem=MIPSsimulation(fadds,adds,instrs[I][1],reg,mem)
            sim=''
            for j in range(20):
                sim=sim+'-'
            sim=sim+'\n'
            sim=sim+'Cycle:'+str(J+1)+'\t'+str(instrs[I][0])+'\t'+getnames(instrs[I][1])+'\n'+'\nRegisters\n'+'R00:'
            for k in range(32):
                if(k==8):
                    sim=sim+'\nR08:'
                elif(k==16):
                    sim=sim+'\nR16:'
                elif(k==24):
                    sim=sim+'\nR24:'
                sim=sim+'\t'+str(reg[k])
            sim=sim+'\n\nData\n'+str(fadds)+':'
                    
            for i1 in range((len(mem))):
                sim=sim+'\t'+str(mem[i1])
                if((i1+1)%8==0 and (i1+1)!=len(mem)): 
                    sim=sim+'\n'+str(fadds+4*(i1+1))+':'
            sim=sim+'\n\n'
            
            f1.write(sim)
            if(getnames(instrs[I][1])=='BREAK'):
                break;
            for l in range(len(instrs)):
                if(instrs[l][0]==adds):
                    I=l
            J=J+1
        f1.close()
#main function
def MIPSsim(p1):
    MIPSparse(p1)
    MIPSsimulations(p1)
    
#测试数据的地址
#p='/Users/macbook/documents/华东师大/硕士课程/计算机体系结构/课后作业/Project2/sample.txt'