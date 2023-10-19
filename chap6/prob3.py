geek = {"404" : "clueless.","Uninstalled" : "being fired"}

choice = ""
while choice != 0:
  print("\n\tGeek Translation\n")
  print("\t0 - Quit")
  print("\t1 - Look Up a Geek Term")
  print("\t2 - Add a Geek Term")
  print("\t3 - Redefine a Geek Term")
  print("\t4 - Delete a Geek Term")
  
  choice = int(input("choice:"))
  if choice == 0:
    print("bye")
  elif choice == 1:
    key = input("What term do you want me to translation?:")
    if key in geek:
      value = geek[key]
      print(key + " means " + value+ ".")    
    else:
      print("NONE")
  elif choice == 2:
    key = input("what do you add to the Geek?:")
    if key not in geek:
      value = input("What is the translation?:")
      geek[key] = value
      print(key+" has been added to the Geek")
    else:
      print("This key is already in the Geek")
      
  elif choice == 3:
    key = input("What do you want to change?:")
    if key in geek:
      value = input("What is the new translation?:")
      geek[key] = value
      print(key+" has been changed to "+value)
    else:
      print("This key is not in the Geek")
      
  elif choice == 4:
    key = input("What do you want to delete?:")
    if key in geek:
      del geek[key]
      print(key+" has been deleted")
    else:
      print("This key is not in the Geek")
      
  else:
    print("This key is not in the Geek")
