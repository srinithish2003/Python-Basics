import random

words = ["python", "computer", "programming", "developer", "keyboard", "internet", "database",
         "function", "variable", "algorithm", "machine", "learning", "artificial", "intelligence",
         "network", "software", "hardware", "project", "github", "coding", "challenge", "hangman",
         "elephant", "giraffe", "tiger", "penguin", "mountain", "ocean", "rainbow", "sunshine"]

random_word = random.choice(words)
word_length = len(random_word)

lives = 6
dash_list = []
for _ in random_word:
    dash_list.append("_")

print("Welcome to Hangman!!!")

while lives > 0:

    print("\nWord:", " ".join(dash_list))
    print("Lives remaining:", lives)
    guess = input("Enter your guess: ").lower()
    found = False

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            dash_list[position] = letter
            found = True

    if not found:
        lives -= 1
        print("Wrong guess!")

    if "_" not in dash_list:
        print("\nCongratulations! You guessed the word:", random_word)
        break

if lives == 0:
    print("\nGame Over!")
    print("The word was:", random_word)