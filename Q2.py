numeros = []

while True:
    valor = int(input('Digite um valor: ')) #o int se põe quando é da variavel NUMERO
    if(valor == 0):
        break
    else:
        numeros.append(valor)
        
print(f'os números digitados foram: {numeros}') 

total = sum(numeros)  
print (f'a soma dos numeros digitados é: {total}')
       
