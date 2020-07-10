
sentence = input ("Enter the sentence you want to convert to Pig Latin: ").strip().lower()
consonent_counter = 0
word_list= sentence.split()
new_words=[]

for word in word_list:
    consonent_counter = 0
    if word[0] in "aeiou":
        word = word+"yay"
        new_words.append(word)
    else:
        for letter in word:
             if letter in "aeiou":
                 break
             else:
                 consonent_counter = consonent_counter +1
        
        word = word[consonent_counter:]+word[0:consonent_counter]+"ay" 
        new_words.append(word)     

output = " ".join(new_words)
print(output)