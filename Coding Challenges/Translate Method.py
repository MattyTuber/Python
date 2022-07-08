genome = input("Inserire una Sequenza --> ")
dna = 'ACGT'
tran = 'TGCA'
#Confronto DNA e TRAN creando un modello di traduzione
#A <==> T, C <==> G
translate = dna.maketrans(dna, tran)

print(genome.translate(translate))