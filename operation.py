
from read import read_file
from datetime import datetime

def buy_laptop():

    laptop_purchased_byShop = []
    grand_total = 0
    
    print("Thank you for buying")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone = input("Enter your phone :")
    
    #while loop to ask user if they want to buy more laptop or not
    while True:        
        print("*******************************************************************************************************")
        print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
        print("*******************************************************************************************************")
        a = 1
        file = open("laptop.txt","r")
        for line in file:
            print(a, "\t" + line.replace(",","\t"))
            a =a+ 1
        print("*******************************************************************************************************")  
        file.close()
        print("\n")
    
        valid_id = int(input("Please Provide the ID of the product you want to buy:"))
        print("\n")

        #Validating ID
    
        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please provide a valid laptops ID !!")
            print("\n")
            valid_id = int(input("Please Provide the ID of the laptops you want to buy:"))
        users_quantity = int(input("Please Provide the number of quantity of the laptops you want to buy:"))
        print("\n")
        
    
        #Validating Quantity

        myDict = read_file()
        selected_quantity = myDict[valid_id][3]
        while users_quantity <= 0:
            print("Dear Admin, please provide a quantity other than 0. Please check the laptop list again")
            print("\n")
            users_quantity = int(input("Please Provide the number of quantity of the laptops you want to buy: "))
        print("\n")

        #Update the text file

        myDict[valid_id][3] = int(myDict[valid_id][3]) + int(users_quantity)

        file = open("laptop.txt","w")

        for values in myDict.values():
            file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
            file.write("\n")
        file.close()

        #Purchasing laptops from manufacturer
    
        product_name = myDict[valid_id][0]
        quantity_of_user = users_quantity
        unit_price = myDict[valid_id][2]
        price_of_item = myDict[valid_id][2].replace("$",'')
        total_price = int(price_of_item)*int(quantity_of_user)
        total_price = round(total_price, 2)
        
        laptop_purchased_byShop.append([product_name, quantity_of_user, price_of_item, total_price])
        grand_total += total_price
        
        #Asking user if they want to buy more laptop or not
        buy_more = input("Do you want to buy more laptops from manufacturer?(y/n):")
        while buy_more.lower() not in ["y","n"]:
            buy_more = input("Please enter (y/n)!!:")
        if buy_more.lower() == "n":
            break
   #Calculate total vat on every purchased laptops
    vatAmt = 13/100*(grand_total)
    grand_total += vatAmt

    date_time = datetime.now()

    # print final bill with all purchased items in textfile
    print("\n")
    print("\t \t \t \t Bipul's laptops Shop")
    print("\n")
    print("\t \t Pepsicola, Kathmandu | Phone No: 9818943491 ")
    print("\n")
    print("****************************************************************************************")
    print("Customer's Details: ")
    print("****************************************************************************************")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("****************************************************************************************")
    print("\n")
    print("Purchase Details are:")
    print("************************************************************************************************************")
    print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("************************************************************************************************************")
    for i in laptop_purchased_byShop:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("************************************************************************************************************")

    print("Total: $"+str(grand_total-vatAmt))
    print("Vat Amount: $",  vatAmt)
    print("Grand Total: $" + str(grand_total))
    print("Note: Vat Amount has been added to grand total")
    
    return name,phone,date_time,laptop_purchased_byShop,vatAmt,grand_total



def sell_laptop():
    
    laptop_purchased_byUser = []
    grand_total = 0
    
    print("Thank you for selling")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone = input("Enter your phone :")

    #while loop to ask user if they want to buy more laptop or not
    while True:
        
        print("*********************************************************************************************************")
        print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
        print("*********************************************************************************************************")
        file = open("laptop.txt","r")
        a = 1
        for line in file:
            print(a, "\t" + line.replace(",","\t"))
            a =a+ 1
        print("*********************************************************************************************************")  
        file.close()
        print("\n")
    
        valid_id = int(input("Please Provide the ID of the product you want to sell:"))
        print("\n")

        #Valid ID

        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please provide a valid laptop ID !!")
            print("\n")
            valid_id = int(input("Please Provide the ID of the laptop you want to sell:"))

        users_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
        print("\n")

        #Valid Quantity

        myDict = read_file()
        selected_quantity = myDict[valid_id][3]
        while users_quantity <= 0 or users_quantity > int(selected_quantity):
            print("Dear Admin, the quantity you are looking for is not available in our shop. Please look again in the laptop List")
            print("\n")
            users_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell: "))
        print("\n")

        #Update the text file

        myDict[valid_id][3] = int(myDict[valid_id][3]) - int(users_quantity)

        file = open("laptop.txt","w")

        for values in myDict.values():
            file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
            file.write("\n")
        file.close()

        #getting user purchased items

        product_name = myDict[valid_id][0]
        quantity_of_user = users_quantity
        unit_price = myDict[valid_id][2]
        price_of_item = myDict[valid_id][2].replace("$",'')
        total_price = int(price_of_item)*int(quantity_of_user)
        total_price = round(total_price, 2)

        laptop_purchased_byUser.append([product_name, quantity_of_user, price_of_item, total_price])
        grand_total += total_price

        buy_more = input("Do you want to purchase more laptop from the shop?(y/n):")
        print("\n")
        while buy_more.lower() not in ["y","n"]:
            buy_more = input("Please enter (y/n)!!:")
        if buy_more.lower() == "n":
            break

    #asking user about shipping cost and adding $500 respectively
    date_time = datetime.now()
    shipment_cost = input("Dear Customer do you want your laptops to be shipped?(Y/N)").lower()
    if shipment_cost == "y":
        total = 0
        shipment_cost = 500
        for i in laptop_purchased_byUser:
            total = total + int(i[3])
        grand_total = grand_total + shipment_cost           
        today_date_and_time = datetime.now()
        
        print("\n")
        print("\t \t \t \t  Bipul's laptop Shop")
        print("\n")
        print("\t \t Pepsicola, Kathmandu | Phone No: 9818943491 ")
        print("****************************************************************************************")
        print("\n")
        print("Customer's Details: ")
        print("*****************")
        print("Customer Name:" + str(name))
        print("Phone Number: " + str(phone))
        print("Date and Time: " + str(date_time))
        print("****************************************************************************************")
        print("\n")
        print("Purchase Details are:")
        print("************************************************************************************************************")
        print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
        print("************************************************************************************************************")
        for i in laptop_purchased_byUser:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("************************************************************************************************************")
        if shipment_cost:
            print("Your total Price of laptop is: $"+str(total))
            print("Your Shipping Cost: $", shipment_cost)
            print("Grand Total: $" + str(grand_total))
            print("Note: Shipping Cost has been added to grand total")
        else:
            print("Grand Total: $" + str(total))
    else:
        total = 0
        shipment_cost = 0
        for i in laptop_purchased_byUser:
            total = total + int(i[3])
        grand_total = total + shipment_cost
        today_date_and_time = datetime.now

        print("\n")
        print("\t \t \t \t  Bipul's laptop Shop")
        print("\n")
        print("\t \t Pepsicola, Kathmandu | Phone No: 9818943491 ")
        print("****************************************************************************************")
        print("\n")
        print("Customer's Details: ")
        print("*****************")
        print("Customer Name:" + str(name))
        print("Phone Number: " + str(phone))
        print("Date and Time: " + str(date_time))
        print("****************************************************************************************")
        print("\n")
        print("Purchase Details are:")
        print("************************************************************************************************************")
        print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
        print("************************************************************************************************************")
        for i in laptop_purchased_byUser:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("************************************************************************************************************")
        
        print("Your total Price is: $"+str(total))
        print("Your shipping cost is: $"+str(shipment_cost))
        print("Grand Total: $"+str(grand_total))
        print("Note: Shipping cost has not been added to the grand total")
        
            
    return name,phone,date_time,laptop_purchased_byUser,shipment_cost,grand_total,total
