class Produce: 

    #Constructs a Product
    def __init__(self, producetype, daysuntilexpiration): 
        self.producetype = producetype; 
        self.daysuntilexpiration = daysuntilexpiration; 

    #Accesses the number of days until expiration  
    def get_days_until_expiration(self): 
        return self.daysuntilexpiration; 

    #Gets produce type 
    def get_produce_type(self): 
        return self.producetype; 

    

