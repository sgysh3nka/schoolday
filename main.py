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
  print("Good!")
  input('You see a beautiful girl...')
  input("She's name's Jessica...")
  quest2 = input('Do you wanna talk with her? ')
  if quest2 == "yes":
    input('You go to her to talk...')
    input("You say 'hi' to her")
    input('She says "no"')
    input('~WHAT THE HELL "NO" IS MEANS???~')
    input('You: Why no?')
    input('Jessica: cus u ugly asf')
    input('You really likes Jessica..')
    input('You: Bye!')
    input('Jessica: Bye, bye, ugly boy')
    quest3 = input('Do you wanna go to GYM to be beautiful? ')
    if quest3 == "yes":
      input('You going to GYM..')
      print("Dear player")
      print("This is end of alpha-1.1")
      input('Press enter to exit')
    elif quest3 == "no":
      print("GYM Ending (bad)")
      print("still no gf...?")
      time.sleep(2)
      print("LOSER!!!")
      time.sleep(0.9)
    else:
      input('Error')
  elif quest2 == "no":
    print("No girlfriend Ending")
    print("no gf?..")
    time.sleep(2)
    print("LOSER!!!")
    time.sleep(0.9)
  else:
    input('Error')
elif quest1 == "no":
  print("Bad Ending")
  print("You got grounded..")
  time.sleep(2)
  print("And you didn't get girlfriend...")
  time.sleep(5)
  print("LOSER!!!")
  time.sleep(0.9)
else:
  input('Error')
