import random

wordlist = ['greece', 'tokyo', 'olympic']

chosen_word = random.choice(wordlist)

print(chosen_word)

blank = []

for item in range(len(chosen_word)):
    blank += "_"

print(blank)

guess_letter = input("Guess a litter in a chosen word :").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess_letter:
        blank[position] = letter
print(blank)