print("Inserie dei valori -> ")

a  = [int(i) for i in input().split()]

media = 0

for n in a:

    media+=n

print(media/len(a))