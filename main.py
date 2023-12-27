print ("Hello welcome to the rollerocatser!")
height = int(input("What is your height in centimeres?: "))

if height >= 120:
  print("You are tall enough to ride the rollercoaster!")
  age = int(input("What is your age?: "))
  if age >= 18:
    print("You have to pay 15$")
  else:
    print("You have to pay 10$")
else:
  print("You are not tall enough to ride the rollercoaster!")

