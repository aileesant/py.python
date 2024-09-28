list = []

for i in range(10): 
    valor = int(input('Digite um número: '))
    list.append(valor)

print(f'os números digitados foram: {list}')

maior_valor = max(list)
print(f'o maior número digitado foi: {maior_valor}')

total = sum(list)  
print(f'o totl dos números digitado foi: {total}')
