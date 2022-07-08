frase = "Don't panic!"
lFrase = list(frase)

print (frase)
print (lFrase)

nuovaFrase = ''.join(lFrase[1:3])
nuovaFrase = nuovaFrase + ''.join([lFrase[5], lFrase[4], lFrase[7], lFrase[6]])

print("\n")
print (lFrase)
print (nuovaFrase)