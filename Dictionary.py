# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:40:39 2020

@author: Desktop
"""


students = {}
students ={"Alice":25,"Johnny":26, "Emma":56}

print(students["Alice"])

students["Fred"] = 25 #adding new element

print(students["Fred"])

del students["Fred"]

print (students.keys())

keys_list = list(students.keys()) # coverting key values from dict_keys to list
values_list = list(students.values())# coverting key values from dict_values to list

print (str((57/90)*100)) 