def fibonacci(n):
    
    if n <= 1:
        
        return n
    
    else:
        
        return (fibonacci(n-1) + fibonacci(n-2))


limite = int(input('Inserisci il numero massimo di valori --> '))

for num in range(1, limite+1):
    
    print(fibonacci(num))
