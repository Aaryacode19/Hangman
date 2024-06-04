import random
from aasci_art import stages, main_logo

word_list = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]

print(main_logo)
print("Welcome to the Hangman Game!, Here words are based on planets of our solar system.")
word = random.choice(word_list)

display = []
for letter in word:
    display.append("_")

print(display)

endgame = False
life = 6

while not endgame:
    guess = input("Guess a letter: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            print("Correct!")
            display[position] = letter
            print(display)
    if "_" not in display:
        endgame = True
        print("You win!")
    elif guess not in word:
        life -= 1
        print("Wrong guess.")
        print("Remaining lives:", life)
        if life == 0:
            endgame = True
            print("You lose!")
            print(stages[life])
            print(f" The word was {word}")
            break
    print(stages[life])

