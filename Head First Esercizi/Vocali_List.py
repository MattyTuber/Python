vocali = ['a', 'e', 'i', 'o', 'u']

found = []
parola = input("Inserire una parola --> ")

for lettere in parola:
    if lettere in vocali:
        if lettere not in found:
            found.append(lettere)
for vocali in found:
    print(vocali)