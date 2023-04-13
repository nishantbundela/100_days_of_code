word = "prometheus"
word_list = [*word]
blanks = []
lives = 6
for i in range(len(word)):
  blanks.append("_ ")
while lives > 0:
  guess = ""
  for i in blanks:
    guess = guess + i
  print(guess)
  entry = input("Enter a letter you think is in the word:").lower()
  indices = [j for j in range(len(word_list)) if word_list[j] == entry]
  if entry in word_list:
    indices = [j for j in range(len(word_list)) if word_list[j] == entry]
    if guess == word:
      print("Congratulations!! You have guessed the word correctly")
      break
    for k in indices:
      blanks[k] = entry
  else:
    print("This letter is not in the word")
    lives -= 1
if lives == 0:
  print("Game Over All lives have been exhausted!!")