
inventory = ()
inventory = ("sword", "armor", "sheild", "healing potion")
print("your items:")
for item in inventory:
  print (item)

print("\nPress the enter key to continue")
print("you have ",len(inventory),"items in your possession.")
print("\nPress the enter key to continue")
if "healing potion" in inventory:
   print("You will live to fight another day")
index = int(input("\nEnter the index number for an item in inventory : "))
print("At index ", index, "is",inventory[index])

slice1 = int(input("\nEnter the index number to begin a slice: "))
slice2 = int(input("Enter the index number to begin a slice: "))
print ("inventory[ ",slice1 ,":", slice2, "]\t",inventory[slice1 : slice2])

print("\nPress the enter key to continue.")
print("you find a chest. It contains:")
chest = ()
chest = ("gold","game")
print(chest[ : ])
print("you add the contents of the chest to your inventory")
print("Your inventory is now")
inventory += chest
print (inventory[ : ])
