def somma(lista):
    
    risultato = 0

    for numero in lista:

        risultato += numero

    return risultato

print("Inserie dei valori -> ")

lista  = [int(i) for i in input().split()]

som=somma(lista)

print(som)
