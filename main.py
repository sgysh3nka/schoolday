import time

print("THIS GAME IN ALPHA")
print("THIS GAME CAN CONTAINS BUGS")
time.sleep(5)
print("Welcome to SchoolDay!")
input('Press enter to play.')
print("Day 1")
time.sleep(5)
print("Do you wanna go to school today?")
print("Yes or No")
quest1 = input('')
if quest1 == "yes":
  input('Good!')
elif quest1 == "no":
  print("Bad Ending")
  print("You got grounded..")
  time.sleep(2)
  print("And you didn't get girlfriend...")
  time.sleep(5)
  print("LOSER!!!")
  time.sleep(0.9)
