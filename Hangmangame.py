import random

def choose_word():
    word_list = ["python", "java", "programming", "hangman", "computer", "code", "developer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Hangman Game")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations, you guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect. Attempts remaining:", attempts)

    if attempts == 0:
        print("You ran out of attempts. The word was:", word)

if __name__ == "__main__":
    main()
