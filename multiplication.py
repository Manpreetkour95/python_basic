# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:45:02 2020

@author: vikra
"""

def fn(a):
    b=[0,0,7,"m"]
    for i in a:
        if i==b[0]:
            b.pop(0)
        else:
            pass
    return len(b)==1
fn([11,0,0,7,8,9])

a=[6,7,8,9,33,63,88,62516,47,51,67,91]
def prime(a):
    c=[]
    for i in a:
        #if i>1:
            for b in range(2,i):
                if i%b==0:
                    break
            else:
             print(i)
             c.append(i)
    return len(c)
                 
prime(a)


def prime(num):
   # b=[]
  for num in a:
      if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,"is a prime number")
                    
prime(a)
 
input("x: " )



