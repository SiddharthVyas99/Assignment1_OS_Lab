# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 02:16:01 2019

@author: Sid
"""

def func(st,t):
#    n=len(st)
    st="".join(st.split(","))
    st="".join(st.split("."))
    st="".join(st.split(" "))
    print(st)
    lr=list(st)
    rr=list(st) 
    for j in range(t):
        lst=rr[-1]
        rst=lr[0]
        for i in range(len(rr)-1,-1,-1):
            rr[i]=rr[i-1]
        rr[0]=lst
        for j in range(1,len(lr)):
#             print(j)
            lr[j-1]=lr[j]
        lr[-1]=rst
#    print(rr)
    rrs=""
    lrs=""
    for i in range(len(rr)):
        rrs+=rr[i]
        lrs+=lr[i]
    return rrs,lrs

lrr=[]
rrr=[]
#st=input("Enter string:")
#d=int(input("Enter number"))
st="Open Source Software Lab , Quiz 1."
d=2
lrr,rrr=func(st,d)
print(lrr)
print(rrr)
