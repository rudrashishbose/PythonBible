# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:53:48 2020

@author: Desktop
"""


known_users= ["Ratnaboli","Nandini","Rahul","Piyush","Vishakha",
              "Rudrashish","Phalguni","James"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().title()
    if (name in known_users):
        print ("Hello {}, nice to see you!".format(name))
        remove = input("Would you liked to be removed from the system (Y/N)?: ").upper()
        if remove =="Y":
            print ("*******************************")
            print (known_users)
            print ("*******************************")
            known_users.remove(name)
            print("USER REMOVED SUCCESFULLY!")
            print ("*******************************")
            print (known_users)
            print ("*******************************")
    else:
        new_user = input("Hey {} , I'm sorry but I couldn't recognize you ,would you like to be added to the list (Y/N)? :".format(name)).upper()
        if (new_user == "Y"):
            print ("*******************************")
            print (known_users)
            print ("*******************************")
            known_users.append(name)
            print ("Welcome {},NEW USER ADDED!!".format(name))
            print ("*******************************")
            print (known_users)
            print ("*******************************")
            