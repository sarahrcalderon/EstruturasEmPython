#Exercicio 5/6 - Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor, e pergunte se quer que multiplique o resultado ou não.

n1 = float(input("Digite o primeiro valor numérico: "))
n2 = float(input("Digite o segundo valor numérico: "))
subtracao = n1 - n2
print("A subtração do primeiro pelo segundo valor é:", subtracao)

# Pergunta se a pessoa deseja multiplicar o resultado
pergunta = input("Gostaria de multiplicar o resultado da subtração? (Digite 'sim' ou 'não'): ")
multiplicador = float(input("Por quanto você gostaria de multiplicar o resultado da subtração? "))

# Verifica a resposta e executa a multiplicação se for 'sim'
if pergunta.lower() == 'sim':
    resultado_final = subtracao * multiplicador  
    print("O resultado final da multiplicação é:", resultado_final)
else:
    print("Tchau!")



