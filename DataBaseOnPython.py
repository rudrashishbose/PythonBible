'''
students = {
    "Alice": ["ID0001",45,"A"],
    "Bob": ["ID0002",20,"B"],
    "Claire": ["ID0003",78,"A+"],
    "Dan": ["ID0004",68,"B+"],
    "Emma": ["ID0005",89,"C"]
    }
'''
#student using dictionary of dictionaries, i.e using dictionaries as key value pairs within a dictionary 

students = {
    "Alice": {"id":"ID0001","age":45,"grade":"A"},
    "Bob": {"id":"ID0002","age":20,"grade":"B"},
    "Claire": {"id":"ID0003","age":78,"grade":"A+"},
    "Dan": {"id":"ID0004","age":68,"grade":"B+"},
    "Emma": {"id":"ID0005","age":89,"grade":"C"}
    }
print (students["Dan"]["age"]," ",students["Dan"]["grade"])
