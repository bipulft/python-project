from operation import buy_laptop
from operation import sell_laptop
from write import write_purchased, write_sold


print('\n')
print('------------------------------------------------------------------------')
print('\t \t \t Welcome to Bipul Laptop Shop ')
print('------------------------------------------------------------------------')
print('\t \t Address: Pepsicola, Kathmandu Contact: 9818943491')
print('------------------------------------------------------------------------')
print('\n')

continueLoop = True
while continueLoop == True:

    print('\n')
    print('Press 1 to buy from manufacturer')
    print('Press 2 to sell to customer')
    print('Press 3 to exit')
    print('\n')
    print('------------------------------------------------------------------------')

    try:
        userinput = int(input('Choose Option 1,2 or 3 :' ))

        if  userinput == 1:
            name,phone,date_time,laptop_purchased_byShop,vatAmt, grand_total = buy_laptop()
            write_purchased(name,phone,date_time,laptop_purchased_byShop,vatAmt,grand_total)

        elif userinput == 2:
            name,phone,date_time,laptop_purchased_byUser, shipment_cost,grand_total,total = sell_laptop()
            write_sold(name,phone,date_time,laptop_purchased_byUser,shipment_cost,grand_total,total)


        elif userinput ==3:
            continueLoop = False
            print('Thank you for visiting and please do visit again')
        else:
            print('Choose an option from above menu list.')
    except ValueError:
        print("Invalid input. Please enter a valid option!")
    
