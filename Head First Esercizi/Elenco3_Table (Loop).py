from pprint import pprint

elenco = {}
n = int(input("Inserire numero di persone --> "))

for i in range(n):
    elenco[str(i)] = {'Nome': input("Inserire Nome --> "),
                      'Cognome': input("Inserire Cognome --> "),
                      'Sesso': input("Inserire Sesso --> ")}

pprint(elenco)
