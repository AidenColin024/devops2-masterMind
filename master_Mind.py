#!/bin/python3
# MasterMind – Kleurenversie zonder backdoor
# Bestand: master_Mind.py

import random

COLORS = ['R', 'G', 'B', 'Y', 'P', 'O']
MAX_ATTEMPTS = 10
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

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

def play_mastermind():
    print("🎮 Welkom bij Mastermind – Kleurenversie!")
    print("Raad de geheime combinatie van 4 kleuren.")
    print("Kleuren: R (rood), G (groen), B (blauw), Y (geel), P (paars), O (oranje)")
    print("Voorbeeld invoer: RGBY")

    secret_code = generate_code()

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = ""
        valid_guess = False
        while not valid_guess:
            guess = input(f"Poging {attempt}: ").upper().strip()
            valid_guess = len(guess) == CODE_LENGTH and all(c in COLORS for c in guess)
            if not valid_guess:
                print(f"❌ Ongeldige invoer. Gebruik precies {CODE_LENGTH} kleurenletters, zoals RGBY.")

        black, white = get_feedback(secret_code, guess)
        print(f"✔️ Black pegs (juiste kleur + plek): {black}, White pegs (juiste kleur, verkeerde plek): {white}")

        if black == CODE_LENGTH:
            print(f"🎉 Gefeliciteerd! Je hebt het goed geraden: {''.join(secret_code)}")
            return

    print(f"🔚 Helaas, je hebt het niet geraden. De juiste code was: {''.join(secret_code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_mastermind()
        again = input("Opnieuw spelen (Y/N)? ").upper()


