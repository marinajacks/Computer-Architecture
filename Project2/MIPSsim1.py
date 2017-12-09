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
    s=''
    for i in range(20):
        s+='-'
        print('-',end='')
    print('\nCycle:'+str(2)+'\n\n')
    s=s+'\nCycle:'+str(2)+'\n\n'+'IF Unit:\n'
    print('IF Unit:')
    print('\tWaiting Instruction:')
    s=s+'\tWaiting Instruction:\n'
    print('\tExecuted Instruction:')
    s=s+'\tExecuted Instruction:\n'
    print('Pre-Issue Queue:')
    s=s+'Pre-Issue Queue:\n'
    print('\tEntry 0:')
    s=s+'\tEntry 0:\n'
    print('\tEntry 1:')
    s=s+'\tEntry 1:\n'
    print('\tEntry 2:')
    s=s+'\tEntry 2:\n'
    print('\tEntry 3:')
    s=s+'\tEntry 3:\n'
    print('Pre-ALU1 Queue:')
    s=s+'Pre-ALU1 Queue:\n'
    print('\tEntry 0:')
    s=s+'\tEntry 0:\n'
    print('\tEntry 1:')
    s=s+'\tEntry 1:\n'
    print('Pre-MEM Queue:')
    s=s+'Pre-MEM Queue:\n'
    print('Post-MEM Queue:')
    s=s+'Post-MEM Queue:\n'
    print('Pre-ALU2 Queue:')
    s=s+'Pre-ALU2 Queue:\n'
    print('\tEntry 0:')
    s=s+'\tEntry 0:\n'
    print('\tEntry 1:\n')
    s=s+'\tEntry 1:\n'
    print('Post-ALU2 Queue:\n')
    s=s+'Post-ALU2 Queue:\n\n'
    print('Registers')
    s=s+'Registers\n'
    
    '''下面所有的算法都是第一个项目的程序的打印出来就行了,
    这里的更细就需要涉及到project1项目中的一些具体的操作
    '''
    
    return s
