import random

def generate_number(start, end):
    #Generates a random number within the specified range.
    return random.randint(start, end)

def compare_numbers(guess, target):
    #Compares the user's guess with the target number.
    if guess < target:
        return "Higher!"
    elif guess > target:
        return "Lower!"
    else:
        return "equal"

def compute_difference(guess, target):
    #Computes the absolute difference between two numbers.
    return abs(guess - target)

def validate_input(user_input):
    #Validates if the user's input is a valid number.
    if user_input.isdigit():
        return True
    else:
        print("Invalid input. Please enter a valid number.")
        return False

def guess_number(start, end):
    #Prompts the user to guess a number and provide clues.
    target_number = generate_number(start, end)
    attempts = 0
   

    while True:
        attempts += 1
        guess = input(f"Guess a number between {start} and {end}: ")

        if not validate_input(guess):
            continue

        guess = int(guess)
        difference = compute_difference(guess, target_number)
        comparison = compare_numbers(guess, target_number)

        if comparison == "equal":
            if attempts <= 5:
                print(f"Congratulations! You guessed the number in {attempts} attempts. Great Job! You should be a psychic.")
            else:
                print(f"Congratulations! You are dumb! You guessed the number in so many attempts even I could not count it.\n Great Job! {attempts} attempts. It's a new world record you dumb ass.")
            break
        else:
            if difference <= 10:
                print("So close, yet so far!")
            elif difference <= 15:
                print("Meeh. Close enough.")
            elif difference <= 20:
                print("You're not even close you dumb freak")
            elif difference >= 30:
                print("Emotional Damage!")
            else:
                print("You've got to be kidding me. Are you even trying?")
            print(comparison)

def main():
    print()
    print("Welcome to the Number Guessing Game! Try your luck you unlucky bastard!")

    while True:
        print("\n----- MENU -----")
        print("1. Start the game")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            guess_number(start, end)
        elif choice == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        

if __name__ == "__main__":
    main()    