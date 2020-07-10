a = [1,2,3]

#a = 250

def f1():
    a[0]=5 # changes global value of the list/dictionary without first using the global keyword 
    print(a)

def f2():
    a=799 #local
    print(a)

f1()
f2()
print(a)