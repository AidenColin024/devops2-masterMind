print("MasterMind")

import random

# Gebruik woorden OF cijfers
ALLOWED_INPUTS = ['1', '2', '3', '4', '5', '6', 'red', 'blue', 'green', 'yellow', 'orange', 'purple']
USE_WORDS = True  # Zet op False als je alleen cijfers wil gebruiken

def generate_Code(length=4):
    pool = ALLOWED_INPUTS if USE_WORDS else [str(i) for i in range(1, 7)]
    return [random.choice(pool) for _ in range(length)]

def get_Feedback(secret, guess):
    black = sum(s.lower() == g.lower() for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}
    for s, g in zip(secret, guess):
        if s.lower() != g.lower():
            s_key = s.lower()
            g_key = g.lower()
            secret_counts[s_key] = secret_counts.get(s_key, 0) + 1
            guess_counts[g_key] = guess_counts.get(g_key, 0) + 1

    white = sum(min(secret_counts.get(k, 0), guess_counts.get(k, 0)) for k in guess_counts)
    return black, white

def show_Secret(mystery, is_admin=False):
    if is_admin:
        print("Secret code:", mystery)
    else:
        print("Access denied: Not an admin!")

def admin_check():
    password = input("Enter admin password: ")
    return password == "admin123"  # eenvoudig voorbeeld

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-code combination. Use words or digits depending on the version.")
    secret = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = []
        valid = False
        while not valid:
            raw_input = input(f"Attempt {attempt}: ").strip()
            if raw_input.lower() == "cheat":
                if admin_check():
                    show_Secret(secret, True)
                else:
                    show_Secret(secret, False)
                continue
            guess = raw_input.split()
            valid = len(guess) == 4 and all(item.lower() in [x.lower() for x in ALLOWED_INPUTS] for item in guess)
            if not valid:
                print("Invalid input. Enter 4 valid items (e.g., 'red blue green yellow' or '1 2 3 4').")

        black, white = get_Feedback(secret, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print("Congratulations! You guessed the code:", ' '.join(secret))
            return

    print("Sorry, you've used all attempts. The correct code was:", ' '.join(secret))

if __name__ == "__main__":
    again = 'Y'
    while again.upper() == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()
