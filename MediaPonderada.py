#Exercicio 7 - Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4. Optei por utilizar zip e sum por tornar mais eficiente aqui um breve resumo da sua eficácia:

# ZIP = essa função é usada para combinar elementos de duas ou mais listas. Aqui temos os(números, pesos) cria pares de elementos, onde o primeiro elemento do par é um número e o segundo é o peso correspondente a esse número.

#SUM = é usada para calcular a soma dos elementos em uma lista. No caso do código, sum(pesos) calcula a soma dos pesos, já a >> sum(num * peso for num, peso in zip(numeros, pesos)) << calcula a soma dos produtos de cada número pelo seu peso correspondente.

numeros = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]

#Calculando a média
soma_pesos = sum(pesos)
soma_produtos = sum(num * peso for num, peso in zip(numeros, pesos))

# Calculando a média ponderada
media_ponderada = soma_produtos / soma_pesos

print("A média ponderada dos números é:", media_ponderada)
