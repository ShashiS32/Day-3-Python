first_choice = input(("Hello, welcome to Tresure island \nYour goal is to find the treasure \nYou are at a crosswalk, would you like to go left or right: \n"))

if first_choice == "left":
  print ("You chose left, you walked into a cave")
  second_choice = input("You see an old man, would you like to talk to him? \nY/N \n")
  if second_choice == "Y":
    print("He ate you! You died, try again")
  elif second_choice == "N":
    third_choice = input(("You walked away, and survived from his attacks. You see a light. Do you approach it? \nY/N"))
    if third_choice == "Y":
      print ("Congrats, you made it out safley and found the tressure")
    else:
      print ("The old man sneaked up on you and killed you, try again")
  else:
    print ("You died of starvation because you didn't choose Y or N, try again.")
    
    
    
          

elif first_choice == "right":
  print ("You chose right, you walked into a forest")
bear = input("You see a bear, would you like to fight it? \n Y/N")
if bear == "Y":
  print ("The bear ripped you to shreds, you died, try again")
elif bear == "N":
  map = input("You see a map, would you like to follow it? \n Y/N")
  if map == "Y":
    print ("The map led you the wrong way, into pirates who killed you, try again")
  elif map == "N":
    print ("Congrats, you decided to go with your guts and found the tressure 2 minutes later!")
  else:
    print("You chose to go nowhere, which led to the bear finding and killing you, try again")


else:
  print("You didn't chose to go left or right, you died waiting for a decision, try again")


