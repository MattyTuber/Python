r = int(input("Inserire colore Red --> "))
g = int(input("Inserire colore Green --> "))
b = int(input("Inserire colore Blue --> "))

r = hex(r)[2:]
g = hex(g)[2:]
b = hex(b)[2:]

print("#"+(r.zfill(2)+g.zfill(2)+b.zfill(2)).upper())