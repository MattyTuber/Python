bin = int(input('Inserire un numero binario: '))

dec, i, n = 0, 0, 0

while(bin != 0):
    
    decimal = bin % 10
    
    dec = dec + decimal * pow(2, i) 
    
    bin = bin//10
    
    i += 1

print(dec)
