class Refrigerator: 
    capacity = 25
    fridgelist= []; 

    def __init__(self):
        self.fridgelist = [];

    def add_item(self, item, amount): 
        if((len(self.fridgelist) + amount) <= self.capacity):
            for x in range(amount): 
             self.fridgelist.append(item);
        

    def check_inventory(self): 
        for items in self.fridgelist: 
            print(items, items.get_days_until_expiration());

    def remove_expired(self): 
        for item in self.fridgelist: 
            if(item.get_days_until_expiration() is 0): 
                print(self.fridgelist.remove(item))

    



