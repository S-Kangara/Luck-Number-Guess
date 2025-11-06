import random

print("---Welcome to the Luck Guess Number Game!---")

while True:
    secret_number = random.randint(1,10)
    attempts = 0
    max_attempts = 3

    print("\nI'm thinking of a number between 1 and 10...")
    print(f"You have {max_attempts} attempts. Good Luck!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        attempts +=1
        
        if attempts == max_attempts and guess != secret_number:
            print(f"Out of attempts! The number was {secret_number}.")
            break       
        elif guess < secret_number:
            print("Too Low! Try Again...") 
        else:
            print("Too High! Try Again...")


    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! GoodBye!")
        break

    

      
