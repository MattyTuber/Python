def searchLetters(phrase: set, letters: set) -> set:
    """Trova le lettere nella frase inserita"""

    return letters.intersection(phrase)


phrase = set(input("Inserire una parola --> "))
letters = set(input("Inserire le lettere da ricercare --> "))
print(searchLetters(phrase, letters))
