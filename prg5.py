#!/usr/bin/python3
import random
i=0
def myroll():
	return random.randint(1,6)
while(i<=100):
    n=input("press r to roll a disc")
    if(n=='r'):
        r=myroll()
        i=i+r
        print("new position is",i)	

	