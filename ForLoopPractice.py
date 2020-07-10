'''
for number in range(1,11,2): # range (start,end+1,step)
    print(number)
'''
vowel = 0
consonant = 0
sentence = input("Enter a sentence and I'll tell you the number of vowels and consonants it contains!: ")

for letter in sentence:
    if letter.lower() in "aeiou":
        vowel = vowel + 1
    elif letter in " !.":
        pass
    else:
        consonant = consonant+1

print("Your sentence has {} vowels and {} consonants".format(vowel,consonant))