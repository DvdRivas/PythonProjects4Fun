import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
while True:
    n=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
    m=random.randint(0,2)
    if n==0:
      print("You chose Rock")
      print(rock)
      if m==1:
        print("AI chose Paper")
        print(paper)
        print("You loose")
      elif m==0:
        print("AI chose Rock")
        print(rock)
        print("Its a draw")
      else:
        print("AI chose Scissors")
        print(scissors)
        print("You Win!")
    elif n==1:
      print("You chose Paper")
      print(paper)
      if m==2:
        print("AI chose Scissors")
        print(scissors)
        print("You loose")
      elif m==1:
        print("AI chose Paper")
        print(paper)
        print("Its a draw")
      else:
        print("AI chose Rock")
        print(rock)
        print("You Win!")
    elif n==2:
      print("You chose Scissors")
      print(scissors)
      if m==0:
        print("AI chose Rock")
        print(rock)
        print("You loose")
      elif m==2:
        print("AI chose Scissors")
        print(scissors)
        print("Its a draw")
      else:
        print("AI chose Paper")
        print(paper)
        print("You win!")
    else:
      print("Choose a correct number")

