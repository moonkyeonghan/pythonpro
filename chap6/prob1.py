inventory = []
inventory = ["sword", "armor", "sheild", "healing potion"]
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
chest = []
chest = ["gold","game"]
print(chest[ : ])
print("you add the contents of the chest to your inventory")
print("Your inventory is now")
inventory += chest
print (inventory[ : ])
print("\nPress the enter key to continue.")
print("you trade your sword for a crossbow.")
inventory[0] = "crossbow"
print(inventory)
print("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6]=["orb of future telling"]
print(inventory)
print("\nPress the enter key to continue.")
print("In a great battle, your sheild is destroyed.")
del inventory[2]
print("your inventory is now:")
print(inventory)
print("\nPress the enter key to continue.")
print("your crossbow and armor are stolen by thieves")
del inventory[:2]
print("your inventory is now:")
print(inventory)
