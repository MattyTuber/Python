def searchVowels(word: str) -> set:
    """Trova le vocali nella parola inserita"""
    vow = set("aeiou")

    return vow.intersection(word)


word = set(input("Inserire una parola --> "))
print(searchVowels(word))
