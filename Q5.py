numeros = []

for i in range(5):
    valor = int(input('Digite o valor:'))
    numeros.append(valor)

media = sum(numeros) / len(numeros)
print(f'A média dos números da lista: {media:.2f}') 

#esse {media:.f} serve para tirar as dízimas periódicas 
# deixa com apena 2 dígitos 
