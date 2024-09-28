aula 2 - python 
21/09/2024

vetor - array - lista

x = [12,13,45,33,66]

print(x[3])

#imprime UM andar
-----------------------------------------------
x = [12,13,45,33,66]

print(f'{x[0]} - - {x[4]}')  

#imprime DOIS andares
---------------------------------------------
COMANDOS 

#append() - insere na última posição
#insert() - insere na posição desejada
#pop() - deleta uma posição
#remove() - deleta um valor
#sum() - soma todos os valores do vetor
#max() - procura o maior valor do vetor, também serve para string porém ele procura pela qntd de letras
#min() - procura o menor valor do vetor
#choice() - escolhe um "andar" (posição) aleatório(a)
#sort() - ordena o vetor  (também ordena string)
#set() - eliminar elementos repetidos    
-------------------------------------------
x = [12,13,45,33,66]

x.append(88)

print(x)

#insere o valor na última posição
--------------------------------------------

x = [12,13,45,33,66]

  x.insert(88,0)

print(x)

#insere o valor em uma posição específica
--------------------------------------------

x = [12,13,45,33,66]

x.pop()

print(x)

#exclui a última posição
-------------------------------------------

x = [12,13,45,33,66]

x.pop(1)

print(x)

#exclui uma POSIÇÃO específica

---------------------------------------

x = [12,13,45,33,66]

x.remove(45)

print(x)

#remove um VALOR específico

--------------------------------------------

x = [12,13,45,33,66] 

total = sum(x)  

print(total)

#soma todos os valores do vetor

-------------------------------------- 
x = [12,13,45,33,66] 

maior_valor = max(x)
menor_valor = min(x) 

print(maior_valor)
print(menor_valor)

-----------------------------------
  
import random 

x = [12,13,45,33,66] 

sortudo = random.choice(x)

print(sortudo)

# o random serve para abrir mods e mais comandos
  
---------------------------------------------------

import random 

x = [12,13,45,33,66] 

x.sort()

print(x)

# o sort ordena o vetor 
  
-------------------------------------------------
import random 

x = [12,13,45,33,66] 
y = [13,21,66,77,88]

uniao = set(x+y) 

print(uniao)

# o set elimina duplicatas do vetor

  
