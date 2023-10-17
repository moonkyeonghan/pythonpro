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
      break
  elif choice == "1":
    print()
    print("High scores\n")
    print("NAME \t SCORE",)
    for entry in scores:
      name, score = entry
      print(name, "\t", score)
    print()
  elif choice == "2":
      name = input("What is the player's name?:")
      score = int(input("what score did the player get?:"))
      entry = (name, score)
      scores.append(entry)
      scores.sort(key=lambda x: x[1], reverse= True)
