students = {
    "male":["Tom", "Tim","Jim","John"],
    "female":["Alice","Jance","Marta","Juila"]
    }

for key in students.keys():
    for name in students[key]:
        if "t" in name.lower():
            print(name)