N = int(input("Inserire il numero dei valori --> "))

a = []

i = 0

for i in range(N):
    num = int(input("Inserire un numero --> "))

    a.append(num)

i = 0

while i < N:
    print(a[i])

    i = i + 2
