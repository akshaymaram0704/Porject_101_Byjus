import random

class DiceSimulator:
    def roll_dice(self):
        return random.randint(1, 6)

def main():
    dice = DiceSimulator()
    response = 'y'

    while response.lower() == 'y':
        input("Press Enter to roll the dice...")
        rolled_number = dice.roll_dice()
        print_dice(rolled_number)

        response = input("press y to again and n to exit: ")

    print("Thanks for playing! Goodbye.")

def print_dice(number):
    print("---------")
    if number == 1:
        print("|       |")
        print("|   •   |")
        print("|       |")
    elif number == 2:
        print("| •     |")
        print("|       |")
        print("|     • |")
    elif number == 3:
        print("| •     |")
        print("|   •   |")
        print("|     • |")
    elif number == 4:
        print("| •   • |")
        print("|       |")
        print("| •   • |")
    elif number == 5:
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
    elif number == 6:
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
    print("---------")

if __name__ == "__main__":
    main()

