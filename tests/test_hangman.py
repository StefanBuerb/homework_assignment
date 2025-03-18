import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importiere die Hangman-Funktionen aus homework_1.py
from Homework_1 import choose_word, display_word

#Testet die beiden Funktionen
def test_choose_word():
    """Testet, ob die Funktion ein Wort aus der Liste wählt."""
    word=choose_word()
    assert word in ["python", "aircraft","hangman", "farmer","Germany", "Austria", "programming", "developer", "apple", "github", "banana", "runway"]

def test_display_word():
    """Testet die Darstellung des Wortes mit erratenen Buchstaben."""
    assert display_word("python", {"p", "y"})=="p y _ _ _ _"
    assert display_word("apple", {"a", "e"})=="a _ _ _ e"