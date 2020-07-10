# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:02:09 2020

@author: Desktop
"""
import random as rand

health = 50

difficulty = 1

potion_health = int(rand.randint(25, 50) / difficulty)

health = health + potion_health

print(health)


