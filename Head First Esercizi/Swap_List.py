frase = "Don't panic!"
lFrase = list(frase)

print (frase)
print (lFrase)

for i in range (4):
    lFrase.pop()

lFrase.pop(0)

lFrase.remove("'")

lFrase.insert(2, lFrase.pop(3))
lFrase.extend([lFrase.pop(), lFrase.pop()])

nuovaFrase = ''.join(lFrase)

print("\n")
print (lFrase)
print (nuovaFrase)