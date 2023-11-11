from Produce import *; 
from Refridgerator import *; 

class test: 
    def main(): 
        item = input("What produce would you like to put in the fridge?\n")
        item_num = input("What is the number of items you would like to store in fridge\n")
        exp_day = input("How many days until this produce expire?\n")

        product = Produce(item, exp_day)
        myfridge = Refrigerator(); 
        
        myfridge.add_item(product, item_num); 
        print(item_num + "number of " + product + " was added into your refridgerator!"); 
        
    main()