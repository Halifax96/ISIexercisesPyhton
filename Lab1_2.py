# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:37:06 2023

@author: esteb
"""

print("Exercise 2")

nums = []
numspow=[]
plusSquare=0


while True:
   

   try:
       
       numtyped=float(input())
   
       if not numtyped:
           print("There is any number typed")
       
       if numtyped >=0:
           nums.append(numtyped)
           numspow.append(numtyped**2)
           
       else:
           nums.append(numtyped)
           numspow.append(numtyped**2)
           break
   except ValueError:
       print("Chars are not available element")
      
 
print(nums)
print(numspow)

for plus in numspow:
    plusSquare+=plus
    
print(plusSquare)