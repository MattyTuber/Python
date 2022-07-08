persona = []

numero = int(input("Inserire numero di Persone --> "))

for persone in range(numero):
        nome = input("Inserire il Nome --> ")
        sesso = input("Inserire il sesso --> ")
        elenco = {'Nome': nome,
                  'Sesso': sesso }
        
        persona.append(elenco)

print(persona)