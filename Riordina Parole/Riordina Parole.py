ripetizioni = int(input("Inserire il numero di parole --> "))

parole = []

for i in range(ripetizioni):

    p = input("Inseire una parola --> ")

    parole.append(p)

parole.sort()

print(parole)