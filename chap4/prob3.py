import random as rd
print(" \tWelcome to 'Guess My Number'!\n")

print("I'm thinking of a number between 1 and 100")
print("Try to Guess it in as few attempts as possible\n")
guess = 1
stack=0;
secretguess = rd.randrange(1,100)
while guess != secretguess:
  guess = int(input("take a guess:"))
  if guess > secretguess:
      print("Lower.....")
  elif guess < secretguess:
      print("upper")
  elif guess == secretguess:
      print("you guess it! the number was",secretguess)
  stack += 1
print("And it only took you",stack,"tries!")
