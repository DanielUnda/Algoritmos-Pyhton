# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:35:47 2022

@author: Daniel Xolalpa Unda
"""

def uppercase(phrase:str)->str:
    """
    Will convert the entire string to uppercase letters
    >>> uppercase("hi my name is Daniel")
    'HI MY NAME IS DANIEL'
    >>> uppercase("My age is 27.")
    'MY AGE IS 27.'
    """

    return phrase.upper()

if __name__=="__main__":
    from doctest import testmod
    print(testmod())    