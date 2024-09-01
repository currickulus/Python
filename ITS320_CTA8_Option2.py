#--------------------------------------------------------------------------------
# ITS320_CTA8_Option2.py
# Author: Thomas Dewing
# Date 8/5/2024
#-----------------------------------------------------------------------------------------------------
#GetInput from the user in a list of strings relating to the requirements of a home inventory
#Store the data in a file in this case a csv file is created
#Develop the code so the data in the file can be changed
#Prompt the user for data and subsequent data to be changed when requested
#Loop the program so multiple iterations of the data can be input and later be modified
#
#
#
#
#
#
#---------------------------------------------------------------------------------------------------
# Program inputs: housing data of a homebuilders inventory
# Program outputs: output stored data to a file which can be subsequently changed and saved

 
class home_inventory:
    import csv
    
      

  
    def __init__(self, model, sqfeet, address, city, state, zipcode, sold, forsale,
                 underconn):
        self.model = []
        self.sqfeet = []
        self.address = []
        self.city = []
        self.state = []
        self.zipcode = []
        self.sold = []
        self.forsale = []
        self.undercon = []

    def add_house(self):
        import csv
        
        with open('homeInventory.csv', 'a')as file:
            myFile = csv.writer(file)
            myFile.writerow(["address","model","sqfeet","city","state","zipcode","sold","for sale","under contract"])
        
            model = input("Please enter the model name "),
            sqfeet = input("Enter the square feet of this home "),
            address = input("Enter this home'''s street address "),
            city = input("Enter the city this home is in "),
            state = input("Enter the state this home is in "),
            zipcode = input("Enter the zipcode for this home "),
            sold = input("Is this home sold yes or no? "),
            forsale = input("Is this home for sale? "),
            undercon = input("Is this home under contract? "),
            myFile.writerow([address, model, sqfeet, city, state, zipcode, sold, forsale, undercon])
        
    def view_inventory(self):
        import csv
        

        with open ("homeInventory.csv", "r") as file:
            homes = csv.reader(file)
            for row in homes:
                print(row)

    def modify_inventory():
        import csv
        myList=[]
        with open('homeInventory.csv', "r") as file:
            myFile=csv.reader(file)
            for row in myFile:
                myList.append(row)
            
        
        editRow = int(input("which row would you like to change Enter 2 - " +str(len(myList)-1) + ":"))
        print("Please enter new details for each of the following :")
        for i in range (len(myList[0])):
                            newDetails = input("Enter new data for " + str(myList[0][i]) + ":")
                            myList[editRow][i] = newDetails
        print("\nPlease see the new file below ")
        for i in range (len(myList)):
            print("Row" + str(i)+" :" + str(myList[i]))

        saveCsv = input("\nWould you like to save the new changes? y/n ").lower()
        if saveCsv == ("y"):
            with open('homeInventory.csv', 'w+')as file:
                myFile = csv.writer(file)
                for i in range(len(myList)):
                    myFile.writerow(myList[i])
       
    def remove_inventory():
        remove_name = address.get()
        with open('homeInventory.csv', 'r') as file:
            inventory_data = file.readlines()
        with open('homeInventory.csv', 'w') as file:
            for line in inventory_data:
                address, model = line.strip().split(',')
            if address != remove_name:
                file.write(line)
    


        



user = True
while user:
    print("1. Add home to inventory")
    print("2. Remove home from inventory")
    print("3. Modify entry")
    print("4. View inventory")
    print("5. View selected line")
 
    selection = input("What would you like to do? ")
    if selection == "1":
            home_inventory.add_house(input)
    elif selection == "4":
            home_inventory.view_inventory(input)
    elif selection == "3":
            home_inventory.modify_inventory()
    elif selection == "2":
            home_inventory.remove_inventory(input)
    
    
