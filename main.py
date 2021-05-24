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
game_images=[rock,paper,scissors]
# print(game_images[2])
user=int(input("What do you choose? type 0 for rock,1 for paper,2 for scissors: "))

if user >=3 or user < 0:
  print("You typed an invalid number")
else:
  print(f"user choose {user}:")

  print(game_images[user])  
  
  computer=random.randint(0,2)
  print(f"computer choose {computer}:")
  print(game_images[computer])

  if user == 0 and computer == 2:
    print("You win!")
  elif computer == 2  and user==0:
    print("You lose")
  elif computer>user:
     print("You lose")
  elif user>computer:
    print("You win")
  elif computer == user:
    print("It's draw")     


