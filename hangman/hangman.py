import hangman_words
import hangman_art
import random

word = random.choice(hangman_words.word_list)
word_list = [*word]
blanks = []
lives = 6
for i in range(len(word)):
  blanks.append("_ ")

print(hangman_art.logo)
print("Welcome to Hangman\n")
while lives > 0:
  guess = ""
  for i in blanks:
    guess = guess + i
  print(guess)
  entry = input("Enter a letter you think is in the word:").lower()
  indices = [j for j in range(len(word_list)) if word_list[j] == entry]
  if entry in word_list:
    print("This letter is in the word\n\n")
    print('Next guess >>>>>>>>>>>')
    print(f"lives remaining: {lives}")
    indices = [j for j in range(len(word_list)) if word_list[j] == entry]
    if guess == word:
      print("Congratulations!! You have guessed the word correctly")
      break
    for k in indices:
      blanks[k] = entry
  else:
    print("This letter is not in the word\n\n")
    print('Next guess >>>>>>>>>>>')
    lives -= 1
    print(f"lives remaining: {lives}")
if lives == 0:
  print("Game Over All lives have been exhausted!!")