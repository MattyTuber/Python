import math

l = input('Inserisci un lato: ')

l = int(l)

quad = l**2

r = l / 2

cerchio = 3.14 * r**2

alt = math.sqrt (pow(l,2) - pow (l/2,2))

equi = l * alt / 2

print('Area Quadrato: ', quad)

print('Area Cerchio: ', cerchio)

print('Area Equilatero: ', equi)
