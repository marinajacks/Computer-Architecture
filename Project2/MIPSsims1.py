# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:30:26 2017

@author: Administrator
"""

    
        for i in range(20):
            print('-',end='')
        print('\nCycle:'+str(K+1)+'\n\n'+'IF Unit:')
        if(len(IF_Unit)>0):
            if(flag==True ):
                print('\tWaiting Instruction:')
                print('\tExecuted Instruction:',end='')
                print('['+getnames(IF_Unit[0])+']')
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
                print('\tWaiting Instruction:',end='')
                print('['+getnames(IF_Unit[0])+']')
                print('\tExecuted Instruction:')
        else:
             print('\tWaiting Instruction:')
             print('\tExecuted Instruction:')
         
         
         #将指令按照顺序打印出来,Pre_Issue指令
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
             
                 
        sim=''
        sim=sim+'\nRegisters\n'+'R00:'
        for k in range(32):
            if(k==8):
                   sim=sim+'\nR08:'
            elif(k==16):
                sim=sim+'\nR16:'
            elif(k==24):
                sim=sim+'\nR24:'
            sim=sim+'\t'+str(reg[k])
        #sim=sim+'\n\nData\n'+str(fadds)+':'
        print(sim)
                     
        ''' for i1 in range((len(mem))):
            sim=sim+'\t'+str(mem[i1])
            if((i1+1)%8==0 and (i1+1)!=len(mem)): 
                sim=sim+'\n'+str(fadds+4*(i1+1))+':'
        sim=sim+'\n\n'
        print(sim)
        '''
        '''
            
            p1='E:\\project\\Computer\\Computer-Architecture\\Project2\\sample.txt'
            f=open(p1,'r')
            lines=f.readlines()
            for line in lines:
                print(line)
                
        '''
        

            
            