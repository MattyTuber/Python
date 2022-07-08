def moltiplicazione(lista):
    
    risultato = 1

    for numero in lista:

        risultato *= numero

    return risultato

print("Inserie dei valori -> ")

lista  = [int(i) for i in input().split()]

molt=moltiplicazione(lista)

print(molt)
