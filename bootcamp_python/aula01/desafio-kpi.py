# Questão: Cálculo de Bônus com Entrada do Usuário

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

VALOR_ADICIONAL = 1000


nome = str(input("Digite seu nome: "))
salario_mensal = float(input("Digite o seu salário mensal: "))
bonus = float(input("Digite o Bônus: "))

valor_do_bonus = VALOR_ADICIONAL + (salario_mensal * bonus)


# da forma como sabia inicialmente
print("Olá, " + nome + ", o seu bônus foi de, " + str(valor_do_bonus))

# da forma como foi ensinada na aula
print(f"Olá, {nome}, o seu bônus foi de, {valor_do_bonus}")