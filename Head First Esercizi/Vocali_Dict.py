word = input("Inserire una parola --> ")
vow = {'a': 0,
       'e': 0,
       'i': 0,
       'o': 0,
       'u': 0}

for letter in word:
  if letter in vow:
    vow[letter] += 1
    
print (vow)