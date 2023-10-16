mport random as rd

print ('Guess the word !!!')
print("In this game, the program selects a word at random, and the player's objective is io guess the chosen word" )

words = ('difficult','banana','apple','python','daegu','catholic','university')

word = rd.choice(words)

letters = ""
wordlength = 0
attemps = 6
guessword = " "
blank = ""
for a in word:
    wordlength += 1
print("Length of the selected word =",wordlength)
print("Remaining attemps:",attemps)
while attemps > 0:
  if blank != 0:
    print("Current Guessed word:",end="")
  blank = 0;
  for a in word:
      if a in letters:
          print(a, end="")
      else:
          print("_ ",end="")
          blank += 1
  if blank == 0:
    print()
    print("Congraturations! you guessed the word:",word)
    break;
  print()
  guessword = input("Guess a word = ")

  if guessword not in letters:
      letters += guessword
  if guessword not in word:
      attemps -= 1
      print("Incorrect quess")
  print("Remaining attemps:",attemps)
if attemps == 0:
  print("You're used up all your attemps. the correct word was", word)

