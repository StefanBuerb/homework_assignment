import random

WORDS=["python", "aircraft","hangman", "farmer","Germany", "Austria", "programming", "developer", "apple", "github", "banana", "runway"]

def choose_word(): #Wählt zufällig ein Wort aus der Liste.
    return 0

def display_word(word, guessed_letters): #Zeigt das Wort mit erratenen Buchstaben und _ für unerratene Buchstaben.


    return 0

def hangman(): #Funktion des Spiels
    word=choose_word()

    guessed_letters=set()

    attempts=6  # Anzahl der maximal erlaubten falschen Versuche

    print("Willkommen bei Hangman!")


    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess=input("\nGib einen Buchstaben ein: ").lower()
        
        if len(guess)!                                                  =   1 or not guess.isalpha():
            print("Ungültige Eingabe! Bitte gib einen einzelnen Buchstaben ein.")
            continue
        
        if guess in guessed_letters:

            print("Du hast diesen Buchstaben schon geraten.")
            continue



        guessed_letters.add(guess)
        
        if guess not  in word:
            attempts-=1
            print(f"Falsch! Noch {attempts} Versuche übrig.")
        print(display_word(word, guessed_letters))
        
        if "_" not in display_word(word, guessed_letters):
            print("Glückwunsch, du hast das Wort erraten!")
            return
    print(f"Game Over! Das gesuchte Wort war: {word}")
if __name__=="__main__":



    hangman()
