#--------------------------------------------------------------------------------
# ITS320_CTA2_Option2.py
# Author: Thomas Dewing
# Date 7/7/2024
#-----------------------------------------------------------------------------------------------------
#GetInput==From_user FIVE TIMES:
#Put the data in a LIST:
#Convert the inputs into floating point
#Perform functions on the input compared to according to the requested criteria
#Evaluate the user input by determining the total, average, the lowest number
#---the highest number, reprinting the numbers entered, and producing
#---the product of the initial input with accrued interest
#
#
#
#
#---------------------------------------------------------------------------------------------------
# Program inputs: arbitrary numbers from user input
# Program outputs: total, average, low high, the numbers and the numbers with interest
list = []
    
for i in range( 1,6):
    list.append(float(input("Please enter a number ")))
      


print(list)

Sum = sum(list)

print("The total is", Sum)

def Average(list):
    return sum(list) / len(list)

average = Average(list)
print("The average is ", (average))

def Minimum(list):
    return min(list)

minimum = Minimum(list)

print("The lowest number is ", (minimum))

def Maximum(list):
    return max(list)

maximum = Maximum(list)

print("The highest number is ", (maximum))

print("The numbers you entered are", list)






new_list = [ i * 1.2 for i in list]

print("The numbers reflecting accrued intrerest are",new_list)
