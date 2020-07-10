import random as rand
films = {
    "Finding Dory": {"min_age":3, "seats":5},
    "Bourne": {"min_age":18, "seats":5},
    "Tarzan": {"min_age":15, "seats":5},
    "Ghost Busters":{"min_age":12, "seats":5}
        }
goodbye_quotes = ["They must often change, who would be constant in happiness or wisdom.- Confucius","Goodbye always makes my throat hurt - Charlie Brown","Goodbyes, they often come in waves"]
continueBooking = True
while continueBooking == True:
    choice = input("What movie do you want to watch?: ").strip().title()
    if choice in films:
        # pass   # pass can be used as a place holder
        age = int(input("How old are you?: ").strip())
        
        # check user name
        
        if age >= films[choice]["min_age"]:
            
            # check available seats
            
            if films[choice]["seats"] > 0:
                
                print("Ticket Booked!")     
                films[choice]["seats"] = films[choice]["seats"] - 1
            else:
                print("Sorry, this movie is sold out")         
        else:
            print("You are too young to watch this movie")
    else:
        print("I'm sorry, we don't have that movie!")
    
    choice = input("Do you want to continue booking tickets (Y/N)?: ").strip().upper()
    if choice == "Y":
        continueBooking = True
    else:
        continueBooking = False
        print("Goodbye and take care!")
        print("~~~~~",goodbye_quotes[rand.randint(0, 2)],"~~~~~")
    
    
