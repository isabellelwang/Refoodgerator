class Refrigerator: 
    capacity = 25
    fridgelist= []; 

    def __init__(self):
        self.fridgelist = [];

    def add_item(self, item, amount): 
        if((len(self.fridgelist) + amount) <= self.capacity):
            for x in range(amount): 
             self.fridgelist.append(item); 
            

    def print_items(self): 
        for items in self.fridgelist: 
            print(items, ": ", items.get_days_until_expiration());

    def remove_expired(self): 
        if(len(self.fridgelist) > 0): 
            for item in self.fridgelist: 
                if(item.get_days_until_expiration() == 0): 
                    print(self.fridgelist.remove(item), " is removed.")

    def remove_item(self, product): 
        if(len(self.fridgelist) > 0): 
            print(self.fridgelist.remove(product), " is removed") 
        

    



