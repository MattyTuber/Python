
def capitalize(s):
    string = list(s)
    conv = []
    output = ""
    cont = 0
    
    for i in string:
        cont += 1
    
    for i in range(0, cont, 1):
        if i % 2 == 0:
            output += string[i].upper()
        else:
            output += string[i].lower()
            
    conv.append(output)
    
    output = ""
    
    for i in range(0, cont, 1):
        if i % 2 != 0:
            output += string[i].upper()
        else:
            output += string[i].lower()
            
    conv.append(output)
    
    return conv
  
print(capitalize("abcdef"))