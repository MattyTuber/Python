ore = input("Inserire il numero di ore: ")

ore = int(ore)

minuti =  input("Inserire il numero di minuti: ")

minuti = int(minuti)

sec = input("Inserire il numero di secondi: ")

sec = int(sec)

secondi = ore * 3600 + minuti * 60 + sec

print("I secondi totali sono: ", secondi)


