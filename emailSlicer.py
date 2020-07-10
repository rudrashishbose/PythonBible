# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:24:24 2020

@author: Desktop
"""


email_id = input("enter your email id: ")

username = email_id[0:email_id.index("@"):1]

domain_name = email_id[email_id.index("@")+1:]

output = "Your username is {} and your domain name is {}"



print(output.format(username,domain_name))