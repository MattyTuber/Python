i = 0
st = input("Inserire una stringa --> ")
x = int(input("Inserire un numero --> "))

for i in range(len(st)):
    if (i % x == 0):
        if (st[i] == " "):
            print("Spazio,")
        else:
            print(st[i] + ",")