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

print("Welcome to the rock, paper and scissors game!")
pchoice = input("Choose one of the following: rock, paper, scissor\n")
options = [rock, paper, scissors]
cchoice = options[random.randint(0, 2)]
if pchoice == 'rock':
    pchoice = rock
elif pchoice == 'paper':
    pchoice = paper
else:
    pchoice = scissors

print("you chose:")
print(pchoice)
print("The computer chose:")
print(cchoice)

if pchoice == cchoice:
    print("Draw")
elif pchoice == rock and cchoice == paper:
    print("You loose")
#elif pchoice == paper and cchoice == rock:
#  print('You won')
elif pchoice == paper and cchoice == scissors:
    print("You loose")
elif pchoice == scissors and cchoice == rock:
    print("You loose")
else:
    print("Hurrah, You won!")