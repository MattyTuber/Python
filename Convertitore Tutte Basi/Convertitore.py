num = input('Inserire un numero: ')

base = int(input('Inserire la base: '))

dec = int(num,base)

bin = bin(dec)

oct = oct(dec)

hex = hex(dec)

print('Binario: ', bin)

print('Ottale: ', oct)

print('Decimale: ', dec)

print('Esadecimale: ', hex)