s = input("Inserire una stringa --> ")
asc = []

for word in s:
  asc.append(ord(word))

av = sum(asc) // len(asc)
print(av)