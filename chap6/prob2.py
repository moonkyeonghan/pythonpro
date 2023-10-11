scores = [("Moe", 1000),("Larry",1500),("Curly", 3000)]
choice = ""

while choice != 0:
  print("Higher Scores Keeper\n")
  print("0 - Quit")
  print("1 - List Scores")
  print("2 - Add a score")
  
  choice = input("choice : ") 

  if choice == "0":
      print("bye")
  elif choice == "1":
      for entry in scores:
        score, name = entry
        print(name, "\t", score)
  elif choice == "2":
      score = input(("What is the player's name?:"))
      name = input(("what score did the player get?:"))
      entry = (score, name)
      scores.append(entry)
