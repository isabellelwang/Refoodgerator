from Produce import *; 
from Refridgerator import *; 

class test: 
    def main(): 
        myfridge = Refrigerator(); 

        choice = choice = input("What would you like to do? Press: \n 0. Exit Program \n1.Add produce \n 2.Print items in fridge\n 3.Remove produce \n")

        while(choice != 0) : 
            choice = input("What would you like to do? Press: \n 0. Exit Program \n1.Add produce \n 2.Print items in fridge\n 3.Remove produce \n")
            
            if(choice == 1):    
                item = input("What produce would you like to put in the fridge?\n")
                item_num = int(input("What is the number of items you would like to store in fridge\n"))
                exp_day = input("How many days until this produce expire?\n")

                product = Produce(item, exp_day)
        
                myfridge.add_item(product, item_num); 
                print(str(item_num), item, " was added into your refridgerator!"); 
            elif (choice == 2) :
                myfridge.print_items() 
            elif (choice == 3): 
                option = input("What would you like to remove? Press \n 1. an expired item \n 2. item of your choice")
                if(option == 1): 
                    myfridge.remove_expired()
                elif (option == 2): 
                    prod = input("What produce would you like to remove?")
                    myfridge.remove_item(Produce(product))
            else :
                print("Error. Please choose a number 0 to 3.")
            
    
    
    
        
        
    main()