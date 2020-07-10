#even_numbers = [x for x in range(1,101) if x%2 == 0]
#print(even_numbers)

words = ["This","is","a","test"]
answer = [[w.upper(),w.lower(),len(w)] for w in words]
print(answer)