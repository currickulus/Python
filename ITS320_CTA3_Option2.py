#-----------------------------------------------------------------------------------------------------
# ITS320_CTA2_Option2.py
# Author: Thomas Dewing
# Date 6/30/2024
#-----------------------------------------------------------------------------------------------------
#GetInput==From_user:
#Put the data in a dictionary:
#Perform functions on the input compared to tax rates stored in the dictionary
#Evaluate the user input by determining tax rate how much will be taken
#with respect to the user's tax rate given the weekly income
#Print the data from the dictionary and subsequent evaluations:
#
#
#---------------------------------------------------------------------------------------------------
# Program inputs: user's weekly income
# Program outputs: tax rate, how much the government stole, what the user is left with after tax
weekly_income = input("Please submit your weekly income: ")
if int(weekly_income) > 0 and int(weekly_income) <= 500:
    print("youre being taxed 10% of your income")
    print("The government took")
    print((float(weekly_income))*.1)
    print( (float(weekly_income)) - (float(weekly_income))*.1)
elif int(weekly_income) > 500 and int(weekly_income) <= 1500:
    print("youre being taxed 15% of your income")
    print("The government took")
    print((float(weekly_income))*.15)
    print((float(weekly_income)) - (float(weekly_income))*.15)
elif int(weekly_income) > 1500 and int(weekly_income) <=2500:
    print("you're being taxed 20% of your income")
    print("The government took")
    print((float(weekly_income))*.2)
    print((float(weekly_income)) - (float(weekly_income))*.2)         
elif int(weekly_income) > 2500 and int(weekly_income) <= 350000:
    print("you're being taxed 30% of your income")
    print("The government took")
    print((float(weekly_income))*.3)
    print((float(weekly_income)) - (float(weekly_income))*.3)
    
print('This is the amount you get to keep after taxes')
