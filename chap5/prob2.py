import random as rd

words = ("difficult","banana","apple", "python", "daegu", "catholic", "university")

print("Welcome to word jumble!")
print("Unscramble the letters to make a word.")
answer = rd.choice(words)
word = answer
word = list(word)
rd.shuffle(word)
print("jumbles word: ", end='')
for i in word:
    print(i, end='')
correct = input("\nYour quess : ")
if(answer == correct):
  print("correct")
else:
    print("Sorry, that's not correct. the word was :", answer)
