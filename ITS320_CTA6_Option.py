#--------------------------------------------------------------------------------
# ITS320_CTA5_Option1.py
# Author: Thomas Dewing
# Date 7/21/2024
#-----------------------------------------------------------------------------------------------------
#GetInput==From_user 3 times:
#Put the data in a LIST:
#Leaves the inputs as strings
#Regurgitates the user input to the screen as a list VERTICALLY and informs
#The user of whats happening and to make due in the event of having been
#bereft of being a pet owner
#
#As writing this Im wishing I could type DD to delete the whole line
#Then it spins the last user input around in the third individual string
#
#---------------------------------------------------------------------------------------------------
# Program inputs: arbitrary names from user
# Program outputs: the list of user inputs the last of which in reverse seperately

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
