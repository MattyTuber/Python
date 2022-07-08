n1 = int (input("Inserire un numero --> "))
n2 = int (input("Inserie un altro numero --> "))

ch = (input("S: Somma, D: Differenza M: Moltiplicazione --> "))

if (ch == 'S'):
	print ("Somma --> ", n1 + n2)
elif (ch == 'D'):
	print ("Differenza --> ", n1 - n2)
elif (ch == 'M'):
	print ("Moltiplicazione --> ", n1 * n2)