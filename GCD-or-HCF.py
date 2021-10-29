# -*- coding: utf-8 -*-
"""
Greatest Common Divisor(GCD) OR Highest Common Factor(HCF)

@author: SK
"""
#GCD / HCF

a=int(input("1st No.: "))
b=int(input("2nd No.: "))
num1=a
num2=b
while(b!=0):
    t=a%b
    a=b
    b=t
print("\nGCD/HCF of",num1,"&",num2,"is",a)
print(" Thanks ")
