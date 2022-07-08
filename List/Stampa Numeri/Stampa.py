N = int(input("Inseire il numero di valori --> "))

a = []

i = 0

for i in range(N):
    num = int(input("Inseire un valore --> "))

    a.append(num)

print("Pari --> ")

i = 0

for i in  range(N):
    if (a[i] % 2 == 0):
        print(a[i])

print("\nDispari --> ")

while i >= 0:
    if (a[i] % 2 != 0):
        print(a[i])

    i=i-1