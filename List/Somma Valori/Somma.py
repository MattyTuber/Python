dimensione = int(input("Inserire il numero di valori --> "))

somma = 0

numeri = []

for i in range (dimensione):
    num = int(input("Inserire un numero --> "))
    numeri.append(num)

print(numeri)
print("Somma dei valori inseriti --> ", sum(numeri))