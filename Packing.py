print("abc")#default case
print(*"abc") #unpacked version (each iterable element is separated out)

'''
def sum(x,y): #this will only add two numbers
    return(x+y)
'''

'''
#-----------------PACKING----------------------------#

#Packing basically works on the principle of a tuples#

def add(*numbers): #this will only add as many numbers as we want
    #this *number is basically a tuple of all the numbers  
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add(1,4,6,8,0))

print(add(1,4,6,9))

#--------------------PACKING----------------------------#
'''
'''
#--------------------UNPACKING----------------------------#

#Unpacking works basically on the principle of a dictionaries

def about(name,age,likes):
    sentence = "Meet {}! They are {} years old and like {}".format(name,age,likes)
    return(sentence)

print(about("Hakim Ziech",56,"Golf")) 
#print(about(likes="Hakim Ziech",age=56,name="Golf")) # alternative way of passing arguments

dictionary = {"name":"Hamilton","age":90,"likes":"football"}

print(about(**dictionary))# exactly same as print(about(likes="Hakim Ziech",age=56,name="Golf")

#VERY IMPORTANT ---- *(one star) for normal arguments (args) and **(2 stars) for keyword arguments (kwargs)
'''

#packing down keyword arguments into a dictionary when you are unsure of the number of arguments
def foo(**kwargs): 
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))       
foo(madeline = "yes",criss = "kringle",kilngon= "y")
