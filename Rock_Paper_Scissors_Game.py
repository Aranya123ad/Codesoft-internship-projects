import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("\nWelcome to Rock-Paper-Scissors Game!")
    
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("\nInvalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nComputer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print("\n",result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nScores - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
