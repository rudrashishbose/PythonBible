# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:59:22 2020

@author: Desktop
"""


name = input ("What is your name? : ")

age = input ("What is your age? : ")

city = input ("Which city do you live in? : ")

love = input ("What do you enjoy doing? : ")  

string = "Nice to meet you {}, so you're a {} year old living in {} and love {} !"

output = string.format(name,age,city,love)

print (output)

#concatenation using special formatting
##s ="{} - {}".format(name,age)
##s ="{1} - {0}".format(name,age)
# the indexes in the curly braces indicates the position of the arguments in format()
##print(s)