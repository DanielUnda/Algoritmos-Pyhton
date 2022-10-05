# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:10:14 2022

@author: Daniel Xolalpa Unda
"""

def lowercase(phrase:str)->str:
    """
    
    >>> lowercase("Hello my name is Daniel")
    'hello my name is daniel'
    >>> lowercase("HELLO, MY AGE IS 27 YEARS OLD.")
    'hello, my age is 27 years old.'
    >>> lowercase("¡We can use a quotes!")
    '¡we can use a quotes!'
    """
    return phrase.lower()

if __name__=='__main__':
    from doctest import testmod
    print(testmod())