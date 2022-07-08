num = input('Inserire un numero: ')

base = int(input('Inserire la base: '))

if base == 2:

    num = int(num)

    bin = int(num)
    
    dec, i, n = 0, 0, 0

    while(bin != 0):
    
        decimal = bin % 10
    
        dec = dec + decimal * pow(2, i) 
    
        bin = bin//10
    
        i += 1

    oct = oct(dec)
    
    hex = hex(dec)

    print('Decimale: ', dec)
    
    print('Ottale: ', oct)

    print('Esadecimale: ', hex)

elif base == 10:

    num = int(num)

    bin = bin(num)

    oct = oct(num)

    hex = hex(num)

    print('Binario:', bin)

    print('Ottale:', oct)

    print('Esadecimale:', hex)

elif base == 8:

    dec = str(int(num,8))

    dec = int(dec)

    bin = bin(dec)

    hex = hex(dec)

    print('Binario: ', bin)

    print('Decimale: ', dec)

    print('Esadecimale: ', hex)

else:

    print('La base non è implementata nel convertitore')
