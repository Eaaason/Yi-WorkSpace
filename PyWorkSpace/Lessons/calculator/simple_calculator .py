#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

def calculator (expression):
    try:
        result = eval (expression)
        return result
    except:
        return "ERROR: Invalid Expression"
    
def get_expression ():
    expression = input ("Please enter expression or enter \"q\" to exit calculator\n")
    expression = expression.replace (" ", "")
    return expression

def display_result (result):
    print ("Result:", result)
    return

if __name__ == "__main__":
    
    print ("[This is a calculator]")
    while True:
        expression = get_expression()
        if expression == "q":
            exit_calculator = True
            break
        print ("Your enter expression", expression)
        result = calculator (expression)
        display_result (result)
