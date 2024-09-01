#--------------------------------------------------------------------------------
# ITS320_CTA5_Option1.py
# Author: Thomas Dewing
# Date 7/21/2024
#-----------------------------------------------------------------------------------------------------
#GetInput from user in the form of the first and second parts of an imaginary number twice:
#Evaluate the addition, subtraction, multiplication and absolute value of the numbers
#
#
#
#
#
#
#
#
#---------------------------------------------------------------------------------------------------
# Program inputs: arbitrary numbers from user
# Program outputs: addition subtraction multiplication division and absolute value of the 2 numbers

import math

first = int(input('please enter the real portion of your first number '))
second = int(input('please enter the imaginary portion of your first number '))
third = int(input('please enter the real portion of your second numter '))
fourth = int(input('Please enter the imaginary portion of your second number '))



def Comadd(x1, x2):
    return x1+x2

x1 = complex(first, second)
x2 = complex(third, fourth)

print("The addition of your complex numbers results in :", Comadd(x1,x2))

def Comsub(x1, x2):
    return x1-x2
x1 = complex(first, second)
x2 = complex(third, fourth)

print("The subtraction of your complex numbers results in :", Comsub(x1,x2))

def Mulcom(x1, x2):
    return x1*x2
x1 = complex(first, second)
x2 = complex(third, fourth)

print("The multiplication of your complex numbers results in :", Mulcom(x1, x2))

def Divcom(x1, x2):
    return x1/x2
x1 = complex(first, second)
x2 = complex(third, fourth)

print("The division of your complex numbers results in :", Divcom(x1, x2))

def Modfirst(x1):
    return abs(x1)
x1 = complex(first, second)

print("The absolute value of your first number is :", Modfirst(x1))

def Modsecond(x2):
    return abs(x2)
x1 = complex(third, fourth)

print("The absolute value of your second number is :", Modsecond(x2))
