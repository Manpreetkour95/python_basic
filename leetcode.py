# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:23:42 2020

@author: vikra
"""


gamelist=[0,1,2]

def position_choice():
    choice="wrong"
    while choice not in ['0','1','2']:
        choice= input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry")
            
def replacement(gamelist,position):
    userplacement= input("Type a string to replace")
    gamelist[position]=userplacement
    return gamelist

def gameon():
    choice="wrong"
    while choice not in ['Y','N']:
        choice= input("KEEP PLAYING(Y,N): ")
        if choice not in ['Y','N']:
            print("Sorry")
    if choice=="Y":
        return True
    if choice=="N"
        return False
    
z=["ab","aab","bab","aba","cda","a","adc"]
s="ab"

count=0
allowed_len=len(s)

for word in z:
    k=s+word
   # k=list(set(k))
    # k=set(k)
    allowed_word=len(set(k))
    if allowed_len==allowed_word:
        print(word)
        count+=1
        

  
    
    
     

    
        
        
        
        z=["ab","aab","bab","aba","cda","a"]
s=set("ab")

count=0
k=[]
for i in range(0,len(z)):
    print(i)
    k.append(set(z[i]))
    if k[i] == s
        count+=1




k=["ab","aab","bab","aba","cda","a"]
for 
k[0]=set("vikram")


x={'a','b'}
y={'b','a'}
len(x)
print(list(x))

x==y



        
    
    
    