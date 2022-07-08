#In phyton non è possibile convertitre le variabili carattere in variabili intere
#perciò non è possibile convertire una lettera maiuscola in minuscola e viceversa

car = input('Inserire un carattere: ')

if ((car >= 'a') and (car <= 'z')):

    car = car - 32

    print(car)

elif ((car >= 'A') and (car <= 'Z')):

    car = car + 32

    print(car)

else:

    print('*')
