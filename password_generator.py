import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.\n")
        return None
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to Password Generator\n")
    
    while True:
        try:
            length = int(input("\nEnter the desired length of the password: "))
           
            if length < 4:
                print("Password length should be at least 4 for beter security.\n")
                continue

            password = generate_password(length)
            if password:
                print(f"\nYour password is: {password}")
        except ValueError:
            print("Invalid input! Please enter a numerical value.\n")
        
        next_generation = input("\nDo you want to generate another password? (y/n): ")
        if next_generation.lower() != 'y':
            print("Thanks for using password generator.\n")
            break

if __name__ == "__main__":
    main()
