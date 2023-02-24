# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:37:16 2023

@author: esteb
"""

print("Exercise 4")



valueString = input("")
res = " "

for index in range(len(valueString)):
    if index % 2:
       res = res + valueString[index].upper()
    else:
        res = res + valueString[index].lower()
        

print(" ",valueString.upper()," ",valueString.lower(), " ", valueString.title(), " ", str(res))
