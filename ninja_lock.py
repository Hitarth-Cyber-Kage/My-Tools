import random
import string
from termcolor import colored

# ASCII Art for Ninja Lock
print(colored('''\
 ____  _____   _                _          _____                    __       
|_   \|_   _| (_)              (_)        |_   _|                  [  |  _   
  |   \ | |   __   _ .--.      __  ,--.     | |       .--.   .---.  | | / ]  
  | |\ \| |  [  | [ `.-. |    [  |`'_\ :    | |   _ / .'`\ \/ /'`\] | '' <   
 _| |_\   |_  | |  | | | |  _  | |// | |,  _| |__/ || \__. || \__.  | |`\ \  
|_____|\____|[___][___||__][ \_| |\'-;__/ |________| '.__.' '.___.'[__|  \_] 
                            \____/                                           
''', 'cyan'))

print(colored("Welcome to Ninja Lock: The Ultimate Password and PIN Generator!\n", 'green'))

while True:
    # Display options
    print(colored("Password Generator", 'yellow'))
    print(colored("1. Generate a password with lowercase letters (a-z)", 'green'))
    print(colored("2. Generate a secure password (a-z, A-Z, 1-9, special characters)", 'green'))
    print(colored("3. Create a password based on a sentence", 'green'))
    print(colored("4. Generate a numerical PIN", 'green'))
    print(colored("5. Exit", 'red'))
    
    choice = input(colored("Select an option (1-5): ", 'cyan'))

    if choice == '1':
        while True:
            length = input(colored("How many characters do you want in your password? ", 'magenta'))
            if length.isdigit() and int(length) > 0:
                length = int(length)
                password = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
                print(colored(f"Generated Password: {password}", 'green'))

                satisfied = input(colored("Are you satisfied with this password? (yes/no): ", 'yellow'))
                if satisfied.lower() == 'yes':
                    break
            else:
                print(colored("Invalid length. Please enter a positive integer.", 'red'))

    elif choice == '2':
        while True:
            length = input(colored("How many characters do you want in your password? ", 'magenta'))
            if length.isdigit() and int(length) > 0:
                length = int(length)
                characters = string.ascii_letters + string.digits + string.punctuation
                password = "".join(random.choice(characters) for _ in range(length))
                print(colored(f"Generated Password: {password}", 'green'))

                satisfied = input(colored("Are you satisfied with this password? (yes/no): ", 'yellow'))
                if satisfied.lower() == 'yes':
                    break
            else:
                print(colored("Invalid length. Please enter a positive integer.", 'red'))

    elif choice == '3':
        suggestions = {
            "movies": [
                "I love Iron Man.",
                "My favorite movie is Inception.",
                "The Godfather is a classic.",
                "I enjoy watching Titanic."
            ],
            "hobbies": [
                "I like painting.",
                "My hobby is gardening.",
                "I enjoy playing cricket.",
                "Reading books is my passion."
            ],
            "food": [
                "I love pizza.",
                "My favorite dish is sushi.",
                "I enjoy cooking pasta.",
                "Ice cream is my weakness."
            ]
        }
        
        while True:
            field = input(colored("In which field do you want to create a sentence password? (e.g., movies, hobbies, food): ", 'magenta'))
            
            if field in suggestions:
                print(colored("Here are some suggestions:", 'green'))
                for sentence in suggestions[field]:
                    print(colored(f"- {sentence}", 'white'))
                
                while True:
                    chosen_sentence = input(colored("Enter your sentence for the password: ", 'magenta'))
                    print(colored(f"Generated Sentence Password: {chosen_sentence}", 'green'))

                    satisfied = input(colored("Are you satisfied with this sentence password? (yes/no): ", 'yellow'))
                    if satisfied.lower() == 'yes':
                        break
                break  # Exit the outer loop after getting a sentence password
            else:
                print(colored("No suggestions available for this field. Please try again.", 'red'))

    elif choice == '4':
        while True:
            pin_choice = input(colored("How many digits for the PIN? (1. 4 digits, 2. 6 digits, 3. 8 digits): ", 'magenta'))
            if pin_choice == '1':
                length = 4
                break
            elif pin_choice == '2':
                length = 6
                break
            elif pin_choice == '3':
                length = 8
                break
            else:
                print(colored("Invalid choice, please try again.", 'red'))

        while True:
            pin = "".join(random.choices(string.digits, k=length))
            print(colored(f"Generated PIN: {pin}", 'green'))

            satisfied = input(colored("Are you satisfied with this PIN? (yes/no): ", 'yellow'))
            if satisfied.lower() == 'yes':
                break  # Exit the while loop and finish this option

    elif choice == '5':
        confirm_exit = input(colored("Are you sure you want to exit? (yes/no): ", 'red'))
        if confirm_exit.lower() == 'yes':
            print(colored("Exiting the program. Goodbye!", 'red'))
            break  # Exit the main loop and end the program

    else:
        print(colored("Invalid choice, please try again.", 'red'))