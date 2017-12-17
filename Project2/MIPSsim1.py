#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:08:55 2017

这个程序主要是为了模拟Project2的程序
@author: 陈彪

"""
wi=[]
def main():
    #这一部分需要作整体来进行相关的操作
    sim=''
    for i in range(20):
        sim+='-'
        print('-',end='')
    print('\nCycle:'+str(2)+'\n\n')
    sim=sim+'\nCycle:'+str(2)+'\n\n'+'IF Unit:\n'
    #IF Unit
    print('IF Unit:')
    print('\tWaiting Instruction:')
    sim=sim+'\tWaiting Instruction:\n'
    print('\tExecuted Instruction:')
    sim=sim+'\tExecuted Instruction:\n'
    #Pre-Issue Queue,可以使用循环来做
    print('Pre-Issue Queue:')
    sim=sim+'Pre-Issue Queue:\n'
    print('\tEntry 0:')
    sim=sim+'\tEntry 0:\n'
    print('\tEntry 1:')
    sim=sim+'\tEntry 1:\n'
    print('\tEntry 2:')
    sim=sim+'\tEntry 2:\n'
    print('\tEntry 3:')
    sim=sim+'\tEntry 3:\n'
    #Pre-ALU1 Queue,可以使用循环来做
    print('Pre-ALU1 Queue:')
    sim=sim+'Pre-ALU1 Queue:\n'
    print('\tEntry 0:')
    sim=sim+'\tEntry 0:\n'
    print('\tEntry 1:')
    sim=sim+'\tEntry 1:\n'
    print('Pre-MEM Queue:')
    sim=sim+'Pre-MEM Queue:\n'
    print('Post-MEM Queue:')
    sim=sim+'Post-MEM Queue:\n'
    #Pre-ALU2 Queue可以使用循环来做
    print('Pre-ALU2 Queue:')
    sim=sim+'Pre-ALU2 Queue:\n'
    print('\tEntry 0:')
    sim=sim+'\tEntry 0:\n'
    print('\tEntry 1:\n')
    sim=sim+'\tEntry 1:\n'
    print('Post-ALU2 Queue:\n')
    sim=sim+'Post-ALU2 Queue:\n\n'
    print('Registers')
    sim=sim+'Registers\n'
    
    '''下面所有的算法都是第一个项目的程序的打印出来就行了,
    这里的更细就需要涉及到project1项目中的一些具体的操作
    '''
    
    
    
    return s




      '''    
            if(getnames(instrs[J][1])=='BREAK'):
                break
            
            
           ''' 
