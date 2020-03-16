# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:52:47 2020

@author: 18pw08
"""

def check_address(lis):
    
    if lis[0]>=1 and lis[0]<127:
        ret_val='A'
    elif lis[0]>=128 and lis[0]<=191:
        ret_val='B'
    elif lis[0]>=192 and lis[0]<=254:
        ret_val='C'
    elif lis[0]==127:
        ret_val='L'
    elif lis[0]==255:
        ret_val='BR'
    return ret_val
ip=input('Enter the IP address:')
lis=ip.split('.')
lis=[int(i) for i in lis]


val=check_address(lis)
if val=='A' or val=='B' or val=='C':
    print('The given IP address belongs to Class ',val)
elif val=='BR':
    print('The given IP address is a Broadcast address')
elif val=='L':
     print('The given IP address is a LoopBack address')
    