#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ITS320_CTA2_Option2.py
# Author: Thomas Dewing
# Date 6/23/2024
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#GetInput==From_user make,model,year,original_miles,current_miles_miles_pergallon
#Put the data in a dictionary
#Print the data from the dictionary
#Perform a function on the data from the dictionary just because I can and I thought it was cool
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program inputs: car: make, model, year, original miles, current miles, miles per gallon
# Program outputs: are the same as the inputs with the exception of the output of miles driven
make, model, year, original_miles, current_miles, miles_pergallon = input("Enter the make of your vehicle "),input("Enter the model of your vehicle "),input("Enter the year of your vehicle "),input("Enter the odometer reading when you purchased the vehicle "),input("Enter the current odometer reading "),input("Enter the estimated miles per gallon of this vehicle ")
car = { 'car make': make,
        'car model': model,
        'car year': year,
        'Cars original miles': original_miles,
        'Cars current miles' : current_miles,
        'Miles per gallon' : miles_pergallon,
        }
print("Your Miles per gallon", str(miles_pergallon))
print(str(car))
print("Youve driven your car for ", (int(current_miles) - (int(original_miles)),"miles"))
