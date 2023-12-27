print ("Hello welcome to the rollerocatser!")
height = int(input("What is your height in centimeres?: "))

if height >= 120:
  
  print("You are tall enough to ride the rollercoaster!")
  photo = input("Would you like a photo taken during your ride [extra 3$] ? (y/n): ")
  age = int(input("What is your age?: "))
  if age >= 18:
    if photo == "y":
      print ("You have to pay 18$")
    else:
      print("You have to pay 15$")
  elif 12 <= age <= 17:
    if photo == "y":
      print ("You have to pay 13$")
    else:
      print("You have to pay 10$")
  else:
    if photo == "y":
      print ("You have to pay 8$")
    else:
      print("You have to pay 5$")
  
else:
  print("You are not tall enough to ride the rollercoaster!")

