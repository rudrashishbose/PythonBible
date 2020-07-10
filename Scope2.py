a = 250

def f1():
    global a #this is to override the global variable and yes it must be declared like this on a single line
    a=100
    print(a)

def f2():
    a=799 #local
    print(a)

f1()
f2()
print(a)