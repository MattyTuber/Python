x = 0
frase = ""
nuovafrase = ""
i = 0

while ( True ):
    x = input("Inserisci un numero da 1 a 10 o premi f per terminare")
    x = int(x)

    if(x == "f"):
        break
   
    if(x > 10):
        print("Numero troppo grande, inserire nuovamente il numero.")

    if(x > 1 and x < 10):
        frase = input("Inserisci una frase o una parola lunga almeno 10 caratteri")

        if(len(frase) < 10):
            print("Frase troppo corta. Inserisci una nuova frase.")

    nuovafrase = frase[:x] + '*' + frase[x:]

    print(nuovafrase)
