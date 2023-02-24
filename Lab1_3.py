# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:37:14 2023

@author: esteb
"""

print("Exercise 3")


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


factValue=int(input("Tipe the value of factorial: "))

if factValue < 0:

    print("Factorial does not exist for negative numbers")

elif factValue == 0:
    
    print("The factorial of 0 is 1")

else:
    
    print("The factorial of", factValue, "is ", factorial(factValue))