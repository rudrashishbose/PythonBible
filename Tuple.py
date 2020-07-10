# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:21:39 2020

@author: Desktop
"""


our_tuple = (1,2,3,"A","B","C") # tuples are immutable

print(type(our_tuple))
print(our_tuple[0:3])

our_list = [1,2,3,4,5]
our_list[2]= 100
#print(our_list)
our_list = tuple(our_list) #coverting lists to tuple,also works on strings
print(type(our_list))

#multiple variable initializations in one statement works on iterable data type like string, list and tuple

(A,B,C,D) =(1,[3,4,[2,6,9],5],(8,9,0),"Connie")

G,H,I = "ABC"

print(type(A))
print(type(B))
print(type(C))
print(type(D))