#--------------------------------------------------------------------------------
# ITS320_CTA5_Option1.py
# Author: Thomas Dewing
# Date 7/14/2024
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
list = []

list = []


first_pet = str(),
second_pet = str(),
third_pet = str(),
print("This program will ask you for the names of three of your pets\n" 
      'if you have never had any pets then make up some names')
for i in range(1):
  list.append(input('Tell me the name of your first pet: ')), first_pet
  list.append(input('Tell me the name of your second pet: ')),second_pet
  list.append(input('Tell me the name of your third pet: ')), third_pet
        
print("your pets are")
print(*list, sep = "\n")

def third_inreverse(list):
    return list[2][::-1]
spinit = third_inreverse(list)

print("for my next trick I'll turn the last pet around: ", spinit)

#I can call the function to spinit without making a function to reverseit
#in the print statement I just did it because I could after I figured out how
#to work the slicing function inherent in Python
