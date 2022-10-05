# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:29:10 2022

@author: Daniel Xolalpa Unda
"""

def palindrome(phrase:str)->bool:
    phrase=phrase.replace(" ","")
    if phrase == phrase[::-1]:
        return True
    else:
        return False


if __name__=='__main__':
    phrase=input("Enter a phrase: ")
    if palindrome(phrase):
        print("The phrase: {} is palindrome.",format(phrase))
    else:
        print("The phrase: {} is not palindrome.",format(phrase))