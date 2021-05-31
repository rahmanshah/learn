import random

wordlist = ['greece', 'tokyo', 'olympic']

chosen_word = random.choice(wordlist)

print(chosen_word)

guess_letter = input("Guess a litter in a chosen word :").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print("Right!")
    else:
        print("Wrong!")