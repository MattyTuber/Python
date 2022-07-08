from datetime import datetime
import time
import random

i = 0

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range (5):

    minutoCorrente = datetime.today().minute

    if minutoCorrente in odds:
        print("Minuto Dispari!")
    else:
        print("Minuto Pari!")

    rand = random.randint(0, 60)

    time.sleep(rand)