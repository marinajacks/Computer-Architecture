#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:10:53 2017

@author: macbook
"""

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
        if(('//') in p1):
            p2=p1.replace(p1.split('//')[-1],'disassembly.txt')
        else:
            p2=p1.replace(p1.split('\\')[-1],'disassembly.txt')
        f=open(p2,'w')
        lines=f1.readlines()
        for i in range(len(lines)):
           f.write(lines[i].strip()+'\t'+str(adds+4*i)+'\t'+getnames(lines[i])+'\n')
        f.close()
        
'''MIPS simulation function,这一步部分是需要进行修改的,因为这一部分原始的脚本是为了进行
模拟mips的操作,但是新的要求是执行流水线的操作'''
def MIPSsimulationss(p1):
    try:
        f=open(p1,'r')
    except IOError:
        print("No such file or directory "+p1)
    else:
        if(('//') in p1):
        #由于mac系统和win系统存在地址的差异,这个需要对win程序下的软件进行调整
        #才可以执行这个操作,否则会导致数据存在异常
            p2=p1.replace(p1.split('//')[-1],'simulation.txt')  
        else:
            p2=p1.replace(p1.split('\\')[-1],'simulation.txt')
        
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
            for i in range(20):
                sim+='-'
                print('-',end='')
            sim=sim+'\nCycle:'+str(2)+'\n\n'+'IF Unit:\n'
            sim=sim+'\tWaiting Instruction:\n'
            sim=sim+'\tExecuted Instruction:\n'
            sim=sim+'Pre-Issue Queue:\n'
            sim=sim+'\tEntry 0:\n'
            sim=sim+'\tEntry 1:\n'
            sim=sim+'\tEntry 2:\n'
            sim=sim+'\tEntry 3:\n'
            sim=sim+'Pre-ALU1 Queue:\n'
            sim=sim+'\tEntry 0:\n'
            sim=sim+'\tEntry 1:\n'
            sim=sim+'Pre-MEM Queue:\n'
            sim=sim+'Post-MEM Queue:\n'
            sim=sim+'Pre-ALU2 Queue:\n'
            sim=sim+'\tEntry 0:\n'
            sim=sim+'\tEntry 1:\n'
            sim=sim+'Post-ALU2 Queue:\n'
            sim=sim+'\nRegisters\n'+'R00:'
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
            print(sim)
            f1.write(sim)
            if(getnames(instrs[I][1])=='BREAK'):
                break;
            for l in range(len(instrs)):
                if(instrs[l][0]==adds):
                    I=l
            J=J+1
        f1.close()
        
#测试数据的地址
#p1='/Users/macbook/documents/华东师大/硕士课程/计算机体系结构/课后作业/Project2/sample.txt'


'''首先实现读取两天指令的操作,并且取两天指令的时候应该注意,取得是两条满足条件的指令,实际上
还是每次执行一个如队列的操作,只不过是这个队列入的要满足条件,那就是长度一定是4而且满足每次
的数量至多是2个.这里给一个参数,用来描述给定的指令的个数.
'''
#p1='E:\\project\\Computer\\Computer-Architecture\\Project2\\sample.txt'

def MIPSsimulations(p1):
    try:
        f=open(p1,'r')
    except IOError:
        print("No such file or directory "+p1)
    else:
        if(('//') in p1):
            p2=p1.replace(p1.split('//')[-1],'simulation.txt')  #这个是用来写的
        else:
            p2=p1.replace(p1.split('\\')[-1],'simulation.txt')
    
       # p1='E:\\project\\Computer\\Computer-Architecture\\Project2\\sample.txt'
      #  f=open(p1,'r')
        lines=f.readlines()
        f1=open(p2,'w')
        adds=256    #初始化的adds地址信息
        adds0=256    #初始化的adds地址信息
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
    
        #初始化队列信息
        from collections import deque
        
        IF_Unit=deque()    #长度为1
        Pre_Issue=deque()  #长度为4
        Pre_ALU1=deque()   #长度为2
        Pre_MEM=deque()    #长度为1
        Post_MEM=deque()   #长度为1
        Pre_ALU2=deque()   #长度为2
        Post_ALU2=deque()  #长度为1
        
        J=0  #这个参数用来标注,指令的地址

        flag=True     #这是一个标志,用来标记
        flag1=True

        #这里边的I给出的是正确的,但是错误的地方在于获取指令的时候不能获取
        #对应的地址信息
        K=1  #从第一个开始
        lens=len(Pre_Issue)
        
        while(1):
            
            I=0
            #这里需要注意的是,只有在IF_Unit的长度为0的时候允许进入,否则是不允许进入的
            while(I<2 and lens <4 and len(Pre_Issue)<4 and flag==True and flag1==True and len(IF_Unit)<1):
                if(getnames(instrs[J][1]).split(' ')[0]=='BEQ' or getnames(instrs[J][1]).split(' ')[0]=='BLTZ'
                or getnames(instrs[J][1]).split(' ')[0]=='BGTZ' or getnames(instrs[J][1]).split(' ')[0]=='JR'):
                    #J, JR, BEQ, BLTZ, BGTZ这些指令都是要进行下面的操作的
                    IF_Unit.append(instrs[J][1])
                    flag=False
                    break
                
                elif(getnames(instrs[J][1]).split(' ')[0]=='J'):
                    IF_Unit.append(instrs[J][1])
                    Pre_ALU2.append(Pre_Issue.pop())
                   # adds,reg,mem=MIPSsimulation(fadds,adds,IF_Unit[0],reg,mem)
                    flag=False
                    break
                else:
                    Pre_Issue.append((instrs[J][1]))
                I=I+1
                lens=lens+1
                J=J+1
                if(getnames(instrs[J][1]).split(' ')[0]=='J'):
                    break
           
              
            
            len0=len(Post_ALU2)
            
            if(len(Post_MEM)>0):
                if(Pre_Issue[len(Pre_Issue)-1]==Post_MEM[0]):
                    adds,reg,mem=MIPSsimulation(fadds,adds,Post_MEM.popleft(),reg,mem)
                    #Post_MEM.popleft()  
   
                    
            '''但是,其实这里最好的方式是从后边反过来执行,就是先把后边的指令,靠近写入数据的
            指令执行了,然后再进行后期的处理,下面的可以用来处理,下面的指令都是处理非LW和SW
            的数据'''
            
            
            
            '''最好的方式是把指令放置在里边,这样的话后边容易进行处理,因为数据
            等相关的信息都保存在里边了,后边执行的时候就可以不需要判断这些数据'''
            
            '''使用deque这种数据结构的popleft函数可以实现从队列中输出
            一条数据,并且这条数据会被打印出来'''
            #Post_MEM.append(Pre_Issue.popleft())
            
            #这一部分实现的是如何把执行与不执行的部分放在一起进行分析,但是这一步需要注意的是
            #应该首先确定让更新先执行,然后在继续
            sim=''
            for i in range(20):
                #print('-',end='')
                sim=sim+'-'
            
            sim=sim+'\nCycle:'+str(K)+'\n\nIF Unit:\n'
           # print('\nCycle:'+str(K)+'\n\n'+'IF Unit:')
           # print(sim)
          #  IF_Unit=deque()
           # IF_Unit.append(instrs[0][1])
            if(len(IF_Unit)>0):
                if(flag==True or getnames(instrs[J][1]).split(' ')[0]=='J' ):
                    sim=sim+'\tWaiting Instruction:\n\tExecuted Instruction: ['+getnames(IF_Unit[0])+']\n'
           
                    '''print('\tWaiting Instruction:')
                    print('\tExecuted Instruction:',end='')
                    print('['+getnames(IF_Unit[0])+']')
                    print(sim)'''
                    
                    '''在这个跳转的时候实现J的转换,必须在这个地方进行,等到执行的时候就必须进行了
                    #这一步找到下一个地址后,这里需要注意的是其实这个操作本质上是不改变寄存器和
                    缓存数据的,而且下面的数据操作实现了数据地址的寻找'''
                    ''' adds,reg,mem=MIPSsimulation(fadds,adds0,IF_Unit[0],reg,mem)
                    #这个操作要等到最后的写入操作完成之后才能进行,否则会报错
                    for l in range(len(instrs)):
                        if(instrs[l][0]==adds): 
                            J=l
                    IF_Unit.popleft()
                    '''
                    
                else:
                    sim=sim+'\tWaiting Instruction: ['+getnames(IF_Unit[0])+']\n\tExecuted Instruction: \n'
                    # sim=sim+sims
                    ''' print('\tWaiting Instruction:',end='')
                    print('['+getnames(IF_Unit[0])+']')
                    print('\tExecuted Instruction:')'''
                  #  print(sims)
            else:
                sim=sim+'\tWaiting Instruction:\n\tExecuted Instruction:\n'
               # sim=sim+sims
                '''print('\tWaiting Instruction:')
                print('\tExecuted Instruction:')'''
               # print(sims)
            
            
            #将指令按照顺序打印出来,Pre_Issue指令
            '''Pre_Issue=deque()  #长度为4
            for i in range(3):
                Pre_Issue.append(instrs[i][1])
            sim='''
            sim=sim+'Pre-Issue Queue:\n'
            #print('Pre-Issue Queue:')
            for i in range(0,len(Pre_Issue)):
                sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_Issue[i])+']\n'
                #print('\tEntry '+str(i)+':['+getnames(Pre_Issue[i])+']')
            for i in range(len(Pre_Issue),4):
                sim=sim+'\tEntry '+str(i)+':\n'
                #print('\tEntry '+str(i)+':')
                #print(sim)
            
            #将指令按照顺序打印出来,Pre_ALU1指令
            '''Pre_ALU1=deque()  #长度为4
            for i in range(1):
                Pre_ALU1.append(instrs[i][1])
            sim='' '''
            sim=sim+'Pre-ALU1 Queue:\n'
            #print('Pre-ALU1 Queue:')
            for i in range(0,len(Pre_ALU1)):
                sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_ALU1[i])+']\n'
                #print('\tEntry '+str(i)+':['+getnames(Pre_ALU1[i])+']')
            for i in range(len(Pre_ALU1),2):
                sim=sim+'\tEntry '+str(i)+':\n'
                #print('\tEntry '+str(i)+':')
            #print(sim)
                
            #完成pre-mem的数据打印
            '''Pre_MEM.append(instrs[0][1])
            sim='' '''
            if(len(Pre_MEM)>0):
                sim=sim+'Pre-MEM Queue: ['+getnames(Pre_MEM[0])+']\n'
                #print('Pre-MEM Queue:',end='')
                #print('['+getnames(Pre_MEM[0])+']')
            else:
                sim=sim+'Pre-MEM Queue:\n'
                #print('Pre-MEM Queue:')
            #print(sim)
    
            #完成post-mem的数据打印
            '''Post_MEM.append(instrs[0][1])
            sim='' '''
            if(len(Post_MEM)>0):
                sim=sim+'Post-MEM Queue: ['+getnames(Post_MEM[0])+']\n'
                #print('Post-MEM Queue:',end='')    
                #print('['+getnames(Post_MEM[0])+']')
            else:
                sim=sim+'Post-MEM Queue:\n'
                #print('Post-MEM Queue:')    
            #print(sim)
    
            #将指令按照顺序打印出来,Pre_ALU2指令
            
            '''Pre_ALU2.append(instrs[0][1])
            sim='' '''
            sim=sim+'Pre-ALU2 Queue:\n'
            #print('Pre-ALU2 Queue:')
            for i in range(0,len(Pre_ALU2)):
                sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_ALU2[i])+']\n'
                #print('\tEntry '+str(i)+':['+getnames(Pre_ALU2[i])+']')
            for i in range(len(Pre_ALU2),2):
                sim=sim+'\tEntry '+str(i)+':\n'
                #print('\tEntry '+str(i)+':')
            #print(sim)
                
            #完成post-mem的数据打印
            '''Post_ALU2.append(instrs[0][1])
            sim='' '''
            if(len(Post_ALU2)>0):
                sim=sim+'Post-ALU2 Queue: ['+getnames(Post_ALU2[0])+']\n'
                #print('Post-ALU2 Queue:',end='')
                #print('['+getnames(Post_ALU2[0])+']')
            else:
                sim=sim+'Post-ALU2 Queue:\n'
                #print('Post-ALU2 Queue:')
            #print(sim)
                
                    
            #sim=''
            sim=sim+'\nRegisters\n'+'R00:'
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
            print(sim)
            f1.write(sim)
            
            flag2=True
            
            lens=len(Pre_Issue)
             
 
            if(len(Post_MEM)>0):
                adds,reg,mem=MIPSsimulation(fadds,adds,Post_MEM[0],reg,mem)
                Post_MEM.popleft()
                flag2=False
                if(len(Pre_MEM)>0):
                    Post_MEM.append(Pre_MEM.popleft())
                    if(len(Pre_ALU1)>0):
                        Pre_MEM.append(Pre_ALU1.popleft())
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                    else:
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                else:
                    if(len(Pre_ALU1)>0):
                        Pre_MEM.append(Pre_ALU1.popleft())
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                    else:
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
           
            else:
                if(len(Pre_MEM)>0):
                    Post_MEM.append(Pre_MEM.popleft())
                    if(len(Pre_ALU1)>0):
                        Pre_MEM.append(Pre_ALU1.popleft())
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                    else:
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                else:
                    if(len(Pre_ALU1)>0):
                        Pre_MEM.append(Pre_ALU1.popleft())
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                    else:
                        if(len(Pre_Issue)>0):
                            if(len(Pre_ALU2)==0 and len(Post_ALU2)==0 and (getnames(Pre_Issue[0]).split(' ')[0]=='LW' or getnames(Pre_Issue[0]).split(' ')[0]=='SW')):
                                Pre_ALU1.append(Pre_Issue.popleft())
                                flag2=False
                    #执行模拟操作,只有在这一步才进行数据的写入
                    #flag=True    
                    #作为标签,当这个数据更新之后才更新寄存器和存储器,
                
            if(len(Post_ALU2)>0):
                adds,reg,mem=MIPSsimulation(fadds,adds,Post_ALU2[0],reg,mem)
                Post_ALU2.popleft()
                if(len(Pre_ALU2)>0):
                       Post_ALU2.append(Pre_ALU2.popleft()) #and len(Pre_ALU1)==0  and len(Pre_MEM)==0
                       if(len(Pre_Issue)>0 and getnames(Pre_Issue[0]).split(' ')[0]!='SW' and getnames(Pre_Issue[0]).split(' ')[0]!='LW' and flag2==True  and len(Post_MEM)==0):
                           Pre_ALU2.append(Pre_Issue.popleft())
                else:# and len(Pre_ALU1)==0 and len(Pre_MEM)==0
                       if(len(Pre_Issue)>0 and getnames(Pre_Issue[0]).split(' ')[0]!='SW' and getnames(Pre_Issue[0]).split(' ')[0]!='LW' and flag2==True  and len(Post_MEM)==0):
                           Pre_ALU2.append(Pre_Issue.popleft())
            else:
                if(len(Pre_ALU2)>0):
                    Post_ALU2.append(Pre_ALU2.popleft())#and len(Pre_ALU1)==0  and len(Pre_MEM)==0 
                    if(len(Pre_Issue)>0 and getnames(Pre_Issue[0]).split(' ')[0]!='SW' and getnames(Pre_Issue[0]).split(' ')[0]!='LW' and flag2==True and len(Post_MEM)==0):
                        Pre_ALU2.append(Pre_Issue.popleft())
                else:# and len(Pre_ALU1)==0  and len(Pre_MEM)==0
                    if(len(Pre_Issue)>0 and getnames(Pre_Issue[0]).split(' ')[0]!='SW' and getnames(Pre_Issue[0]).split(' ')[0]!='LW'and flag2==True  and len(Post_MEM)==0):
                        Pre_ALU2.append(Pre_Issue.popleft())
            

              
            flag2=True
  
            if(len(IF_Unit)>0): 
                    if(flag==True or getnames(IF_Unit[0]).split(' ')[0]=='J'):
                        '''在这个跳转的时候实现J的转换,必须在这个地方进行,等到执行的时候就必须进行了
                        #这一步找到下一个地址后,这里需要注意的是其实这个操作本质上是不改变寄存器和
                        缓存数据的,而且下面的数据操作实现了数据地址的寻找''' 
                        adds=instrs[J][0] #更新跳转的地址信息
                        adds,reg,mem=MIPSsimulation(fadds,adds,IF_Unit[0],reg,mem)
                        #这个操作要等到最后的写入操作完成之后才能进行,否则会报错
                        for l in range(len(instrs)):
                            if(instrs[l][0]==adds): 
                                J=l
                        IF_Unit.popleft()
                        flag=True
            #用于判断Post_ALU2的个数是不是为空,如果是的话,IF_Unit的数据可以执行
            if(len0==0 and len(Post_ALU2)==0):
                flag=True
        
            
            if(len(Post_MEM)==0):
                flag1=True
              
            if(getnames(instrs[J][1])=='BREAK'): 
                break

          
            
            K=K+1
             #这一部分实现的是如何把执行与不执行的部分放在一起进行分析,但是这一步需要注意的是
            #应该首先确定让更新先执行,然后在继
        
        
        sim=''
        for i in range(20):
            sim=sim+'-'
            #print('-',end='')
        sim=sim+'\nCycle:'+str(K+1)+'\n\n'+'IF Unit:\n\tWaiting Instruction:\n\tExecuted Instruction: ['+getnames(instrs[J][1])+']\n'
        #print('\nCycle:'+str(K+1)+'\n\n'+'IF Unit:')
        #print('\tWaiting Instruction:')
        #print('\tExecuted Instruction:',end='')
        #print('['+getnames(instrs[J][1])+']')  
        #print(sim)
        #将指令按照顺序打印出来,Pre_Issue指令
        '''Pre_Issue=deque()  #长度为4
        for i in range(3):
            Pre_Issue.append(instrs[i][1])
        sim='''
        sim=sim+'Pre-Issue Queue:\n'
        #print('Pre-Issue Queue:')
        for i in range(0,len(Pre_Issue)):
            sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_Issue[i])+']\n'
            #print('\tEntry '+str(i)+':['+getnames(Pre_Issue[i])+']')
        for i in range(len(Pre_Issue),4):
            sim=sim+'\tEntry '+str(i)+':\n'
            #print('\tEntry '+str(i)+':')
            #print(sim)
        
        #将指令按照顺序打印出来,Pre_ALU1指令
        '''Pre_ALU1=deque()  #长度为4
        for i in range(1):
            Pre_ALU1.append(instrs[i][1])
        sim='' '''
        sim=sim+'Pre-ALU1 Queue:\n'
        #print('Pre-ALU1 Queue:')
        for i in range(0,len(Pre_ALU1)):
            sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_ALU1[i])+']\n'
            #print('\tEntry '+str(i)+':['+getnames(Pre_ALU1[i])+']')
        for i in range(len(Pre_ALU1),2):
            sim=sim+'\tEntry '+str(i)+':\n'
            #print('\tEntry '+str(i)+':')
        #print(sim)
            
        #完成pre-mem的数据打印
        '''Pre_MEM.append(instrs[0][1])
        sim='' '''
        if(len(Pre_MEM)>0):
            sim=sim+'Pre-MEM Queue: ['+getnames(Pre_MEM[0])+']\n'
            #print('Pre-MEM Queue:',end='')
            #print('['+getnames(Pre_MEM[0])+']')
        else:
            sim=sim+'Pre-MEM Queue:\n'
            #print('Pre-MEM Queue:')
        #print(sim)
        
        #完成post-mem的数据打印
        '''Post_MEM.append(instrs[0][1])
        sim='' '''
        if(len(Post_MEM)>0):
            sim=sim+'Post-MEM Queue: ['+getnames(Post_MEM[0])+']\n'
            #print('Post-MEM Queue:',end='')    
            #print('['+getnames(Post_MEM[0])+']')
        else:
            sim=sim+'Post-MEM Queue:\n'
            #print('Post-MEM Queue:')    
        #print(sim)
        
        #将指令按照顺序打印出来,Pre_ALU2指令
        
        '''Pre_ALU2.append(instrs[0][1])
        sim='' '''
        sim=sim+'Pre-ALU2 Queue:\n'
        #print('Pre-ALU2 Queue:')
        for i in range(0,len(Pre_ALU2)):
            sim=sim+'\tEntry '+str(i)+': ['+getnames(Pre_ALU2[i])+']\n'
            #print('\tEntry '+str(i)+':['+getnames(Pre_ALU2[i])+']')
        for i in range(len(Pre_ALU2),2):
            sim=sim+'\tEntry '+str(i)+':\n'
            #print('\tEntry '+str(i)+':')
        #print(sim)
            
        #完成post-mem的数据打印
        '''Post_ALU2.append(instrs[0][1])
        sim='' '''
        if(len(Post_ALU2)>0):
            sim=sim+'Post-ALU2 Queue: ['+getnames(Post_ALU2[0])+']\n'
            #print('Post-ALU2 Queue:',end='')
            #print('['+getnames(Post_ALU2[0])+']')
        else:
            sim=sim+'Post-ALU2 Queue:\n'
            #print('Post-ALU2 Queue:')
        #print(sim)
        
        ''''
        print('Pre-Issue Queue:')
        for i in range(0,len(Pre_Issue)):
            print('\tEntry '+str(i)+':['+getnames(Pre_Issue[i])+']')
        for i in range(len(Pre_Issue),4):
            print('\tEntry '+str(i)+':')
         
         #将指令按照顺序打印出来,Pre_ALU1指令
        print('Pre-ALU1 Queue:')
        for i in range(0,len(Pre_ALU1)):
            print('\tEntry '+str(i)+':['+getnames(Pre_ALU1[i])+']')
        for i in range(len(Pre_ALU1),2):
            print('\tEntry '+str(i)+':')
        #完成pre-mem的数据打印
        if(len(Pre_MEM)>0):
            print('Pre-MEM Queue:',end='')
            print('['+getnames(Pre_MEM[0])+']')
        else:
            print('Pre-MEM Queue:')
        
         #完成post-mem的数据打印
        if(len(Post_MEM)>0):
            print('Post-MEM Queue:',end='')    
            print('['+getnames(Post_MEM[0])+']')
        else:
            print('Post-MEM Queue:')    
        
         #将指令按照顺序打印出来,Pre_ALU2指令
        print('Pre-ALU2 Queue:')
        for i in range(0,len(Pre_ALU2)):
            print('\tEntry '+str(i)+':['+getnames(Pre_ALU2[i])+']')
        for i in range(len(Pre_ALU2),2):
            print('\tEntry '+str(i)+':')
             
         #完成post-mem的数据打印
        if(len(Post_ALU2)>0):
            print('Post-ALU2 Queue:',end='')
            print('['+getnames(Post_ALU2[0])+']')
        else:
            print('Post-ALU2 Queue:')
             
        '''
        #sim=''
        sim=sim+'\nRegisters\n'+'R00:'
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
        print(sim)
        f1.write(sim)
        f1.close()
    
#main function
def MIPSsim(p1):
    MIPSparse(p1)  #这一部分不需要做任何的调整
    MIPSsimulations(p1)