#Exercicio 4 - Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores. Obs:Optei pelo float por conta da flexibilidade para a digitação de números, por exemplo caso quisesse somar um salário, se eu pusesse int isso não ficaria adequado.

n1 = float(input("Digite o primeiro valor numérico: "))
n2 = float(input("Digite o segundo valor numérico: "))
soma = n1 + n2
# Imprime a soma do input
print("A soma dos valores é:", soma)
