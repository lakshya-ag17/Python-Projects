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
choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list1 = [rock, paper, scissors]
print(list1[choice1])
import random as ran
print("Computer chose:")
choice2 = ran.randint(0,2)
print(list1[choice2])
if choice1==choice2:
    print("Its a draw")
elif (choice1 and choice2) in [0,1]:
    if choice1==1:
        print("You win")
    else:
        print("You lose")
elif (choice1 and choice2) in [1,2]:
    if choice1==2:
        print("You win")
    else:
        print("You lose")
elif (choice1 and choice2) in [2,0]:
    if choice1==0:
        print("You win")
    else:
        print("You lose")
        