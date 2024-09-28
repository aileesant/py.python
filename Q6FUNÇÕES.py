# algoritmo que recebe o nome
# e o sobrenome e mostre na tela o 
# nome completo
# utilizando função

def  completo(primeironome , sobrenome):     
    full = primeironome + ' ' + sobrenome
    print(f'Seu nome completo é: {full}')

primeironome = input('Digite o primeiro nome: ')
sobrenome = input('Digite o sobre nome: ')

completo(primeironome , sobrenome) 

