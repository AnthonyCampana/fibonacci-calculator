#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:38:03 2021

@author: anthonycampana
@title: fibonacci sequence
@description: This program returns the iTH iteration of the fibonacci sequence.
 The ith term is determined by human input
"""

def fibonacci(iteration):


    if iteration == 0:
        return 0
    elif iteration == 1 or iteration == 2:
        return 1
    else:
        return fibonacci(iteration - 1) + fibonacci(iteration - 2)



term = input("Please enter the ith iteration of the fibonacci sequence you would like to see:")

while term != 'q':
    sequence = fibonacci(int(term))
    print("The ith term is: ", sequence)
    term = input("Enter anotrher number: ")
