import random

wordlist = ['greece', 'tokyo', 'olympic']

chosen_word = random.choice(wordlist)

print(chosen_word)

blank = []

for item in range(len(chosen_word)):
    blank += "_"

print(blank)

chk = False
lives = 6
while not chk:
    guess_letter = input("Guess a litter in a chosen word :").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            blank[position] = letter
    print(blank)
    if guess_letter not in chosen_word:
        lives -=1
        if lives == 0:
            chk = True
            print("You lose!")
    if '_' not in blank:
        chk = True
        print("You Win!")
