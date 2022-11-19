# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 19:00:14 2022

@author: user



"""
def oh():
    import time as t
    for i in range(0,10):
        print('\a')
        t.sleep(1)
###################################
def num():
    num=1
    print('%d' % (num))
####################################
def c():
    c=bool(0)
    print(c)
####################################
def water():
    for i in range(100,1000):
        a=i%10
        b=(i//10)%10
        c=(i//100)%10
        if (a**3+b**3+c**3)==i:
            print(i)
#####################################    
class Dick:
    def __init__(self,name):
        self.name=name
    def sing(self):
        print(self.name)
        
#######################################  
def high():
    k=Dick('000')
    print(k.name)
    k.sing()
########################################
class Animal():
    name='cat'
    def jumple(self):
        print(' 1 \n1 1')
def f():
    l=Animal()
    l.jumple()
########################################
class been:
    def __init__(self,name,age,life):
        self.name=name
        self.age=age
        self.life=life
    def time(self):
        for i in range(1,self.life):
            import time as t
            self.age=i
            print(i)
            t.sleep(2)
        self.age=0
        print('you are dead')
    def action(self):
        while self.age!=0:
            action=int(input())
            if action==0:
                print('  1  \n 1 1 \n1   1')
            elif action==1:
                self.age+=1
            else:
                print('not this action')
p=been('john',1,10)
p.action()
p.time()
##########################################
            

        











