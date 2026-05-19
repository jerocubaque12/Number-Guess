import random

def play_game():
    """
    Simulates a number guessing game.
    The user has 8 attempts to guess a randomly generated number 
    between 1 and 100, receiving hints after each incorrect guess.
    """
    user_name = input("Insert your name first!: ")
    print(f"\nHello {user_name}, in this game you have 8 attempts to guess a number between 1 and 100!")
    
    number = random.randint(1, 100)
    tries = 8

    while tries > 0:
        try:
            ask = int(input(f"\n[{tries} attempts left] Insert your number: "))
            
            # Validation for numbers out of the specified range
            if ask < 1 or ask > 100:
                print("Out of range! Please enter a number between 1 and 100.")
                continue # Skips the rest of the loop without losing a try
            
            if ask == number:
                print("You won! Congratulations!")
                return 
            elif ask > number:
                print("Aim lower!")
            else:
                print("Aim higher!")
                
            tries -= 1

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"\nGame over! You lost. The number was {number}.")

if __name__ == "__main__":
    play_game()