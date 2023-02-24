# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:37:17 2023

@author: esteb
"""

print("Exercise 5")


letter=input("Type your spanish ID: ")

letter=letter.replace(' ', '')
letter=letter.replace('.','')

letter=int(letter)


letterList=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

print(letter)

print("The ID letter is: ", letterList[letter%23])