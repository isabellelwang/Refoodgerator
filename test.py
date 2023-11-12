from Produce import *; 
from Refridgerator import *; 


class test: 
    def main(): 
        myfridge = Refrigerator(); 

        choice = input("What would you like to do? Press: \n 0. Exit Program \n 1.Add produce \n 2.Print items in fridge \n 3.Remove produce \n")

        exit_menu = False
        while not exit_menu: 
            if "0" in choice:
                exit()
            elif "1" in choice:    
                item = input("What produce would you like to put in the fridge?\n")
                item_num = int(input("What is the number of items you would like to store in fridge\n"))
                exp_day = Produce.expiry_time(item)

                product = Produce(item)
        
                myfridge.add_item(product, item_num); 
                print(str(item_num), item, " was added into your refridgerator!"); 
            elif "2" in choice:
                myfridge.print_items() 
            elif "3" in choice: 
                option = input("What would you like to remove? Press \n 1. an expired item \n 2. item of your choice \n")
                if "1" in option: 
                    myfridge.remove_expired()
                elif "2" in option: 
                    prod = input("What produce would you like to remove?")
                    myfridge.remove_item(Produce(product))
            else :
                print("Error. Please choose a number 0 to 3.")
            exit_menu = True  

        choice = input("What would you like to do? Press: \n 0. Exit Program \n 1.Add produce \n 2.Print items in fridge \n 3.Remove produce \n")
    main()