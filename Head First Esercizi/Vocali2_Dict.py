vowels = ['a', 'e', 'i', 'o', 'u']
vow = {}

word = input("Inserire una parola --> ")

for letter in word:
  if letter in vowels:
    vow.setdefault(letter, 0)
    vow[letter] += 1
    
print (vow)