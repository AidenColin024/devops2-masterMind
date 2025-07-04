


#!/bin/python3
# MasterMind – Kleurenversie zonder backdoor + admin-check
# Bestand: mastermind.py

import random
import os

COLORS = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'P': 'purple',
    'O': 'orange'
}

MAX_ATTEMPTS = 10
CODE_LENGTH = 4
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")  # Nu met environment variable ondersteuning

def generate_code():
    return [random.choice(list(COLORS.keys())) for _ in range(CODE_LENGTH)]

def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(c, 0), guess_counts.get(c, 0)) for c in guess_counts)

    return black_pegs, white_pegs

def admin_check():
    pw = input("Admin login vereist om de geheime code te zien. Voer wachtwoord in: ").strip()
    return pw == ADMIN_PASSWORD

def play_mastermind():
    print("Welkom bij Mastermind – Kleurenversie!")
    print("Raad de geheime combinatie van 4 kleuren.")
    print("Beschikbare kleuren:")
    for code, name in COLORS.items():
        print(f" {code} = {name}")

    secret_code = generate_code()

    if input("Ben je een admin en wil je de geheime code bekijken? (y/n): ").lower().strip() == "y":
        if admin_check():
            print(f"Geheime code (alleen voor admin): {''.join(secret_code)}")
        else:
            print("Onjuist wachtwoord. Ga verder als speler.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        valid_guess = False
        guess = ""

        while not valid_guess:
            guess_input = input(f"Poging {attempt}: Voer 4 kleuren in (bijv. RGYB of 'red green blue yellow'): ").lower().strip()

            # Ondersteun zowel afkortingen als volledige woorden
            parts = guess_input.replace(",", " ").split()
            if len(parts) == 1 and len(parts[0]) == CODE_LENGTH:
                # Bijvoorbeeld: 'rgby'
                guess = [c.upper() for c in parts[0] if c.upper() in COLORS]
            else:
                # Bijvoorbeeld: 'red blue green yellow'
                reverse_map = {v: k for k, v in COLORS.items()}
                guess = [reverse_map.get(word.lower(), "") for word in parts]

            valid_guess = len(guess) == CODE_LENGTH and all(c in COLORS for c in guess)
            if not valid_guess:
                print("Ongeldige invoer. Gebruik 4 bekende kleuren of afkortingen. Probeer opnieuw.")

        black, white = get_feedback(secret_code, guess)
        print(f"Black pegs (juiste kleur + plek): {black}, White pegs (juiste kleur, verkeerde plek): {white}")

        if black == CODE_LENGTH:
            print(f"Gefeliciteerd! Je hebt het goed geraden: {''.join(secret_code)}")
            return

    print(f"Helaas, je hebt het niet geraden. De juiste code was: {''.join(secret_code)}")

if __name__ == "__main__":
    again = 'Y'
    while again.upper() == 'Y':
        play_mastermind()
        again = input("Opnieuw spelen (Y/N)? ").upper()
