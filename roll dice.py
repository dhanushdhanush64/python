import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Dice Rolling Simulator")
    play = True

    while play:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            play = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
