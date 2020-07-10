import random as rand
class Pound:
    
    def __init__(self,rare=False):                                  #constructor --- self is a convention (always has to be there)
        
        self.rare = rare
        
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.14 #mm
        self.heads = True
        
    def rust(self):
        self.color ="greenish"
    
    def clean(self):
        self.color ="gold"
        
    def flip(self):
        heads_options =[True,False]
        choice = rand.choice(heads_options)
        self.heads = choice
    
    def __del__(self):          #DESTRUCTOR - will delete object of this class on being called
        print("Coin Spent")

coin1 = Pound()
print(type(coin1))
print(coin1.value)


print(coin1.color)
coin1.color = "blue"
print(coin1.color)

coin2 = Pound(rare=True)
print(type(coin1))
print(coin1.value)

        
coin1 = Pound()
coin2 = Pound()

print(coin1.color)
print(coin2.color)

coin1.rust() #applying rust

print(coin1.color) 
print(coin2.color)


coin1.clean() #cleaning coin

print(coin1.color) 

print(coin1.heads)

coin1.flip() #flipping coin

print(coin1.heads)


