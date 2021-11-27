import numpy as np

# Armazena os valores atuais dos pontos
pontos = np.zeros(4)
# Armazena os últimos valores dos pontos
pontos_anterior = []

iteracao = 1
erro_aceitavel = 0.001

# Preenche os valores iniciais dos pontos anteriores, no caso todos = 0
for i in range(len(pontos)):
    pontos_anterior.append(pontos[i])

while iteracao <= 20:
    # Cria a lista que irá armazenar os erros de cada iteração
    erros = []
    # Variável que vai contar a quantidade de erros menores que o erro aceitável
    quant_erros_menores = 0

    # Altera cada valor da lista pontos em função dos pontos anteriores
    pontos[0] = (-0.035 - pontos_anterior[1] - pontos_anterior[2])/-4
    pontos[1] = (-4.187 - 21.3*pontos_anterior[0] - 16*pontos_anterior[3])/-96
    pontos[2] = (0.187 - pontos_anterior[0] -
                 pontos_anterior[3] - pontos_anterior[4])/-4
    pontos[3] = (0.469 - pontos_anterior[2] -
                 pontos_anterior[1] - pontos_anterior[5])/-4
    pontos[4] = (0.117 - pontos_anterior[2] - pontos_anterior[5])/-4
    pontos[5] = (0.312 - pontos_anterior[4] -
                 pontos_anterior[3] - pontos_anterior[6])/-4
    pontos[6] = (-0.195 - 21.3*pontos_anterior[5])/-96

    # Além de calcular o erro para cada ponto sendo erro = |pontos[i] - pontos_anterior[i]|,
    # Altera o valor dos pontos anteriores para os pontos atuais depois de calcular o erro
    for i in range(len(pontos)):
        erros.append(abs(pontos[i] - pontos_anterior[i]))
        pontos_anterior[i] = pontos[i]

    # Verifica quantos erros são menores que o erro aceitável
    for i in range(len(erros)):
        if erros[i] < erro_aceitavel:
            quant_erros_menores += 1

    print("Iteração", iteracao, ":")
    print("Erros:", np.round(erros, 5))

    # Caso todos os erros sejam menores que o erro aceitável, finalizamos o loop mais cedo
    if quant_erros_menores == len(pontos):
        break

    iteracao += 1

for i in range(len(pontos)):
    print("Ponto", i+1, ":", pontos[i])

"""print("=================== A =====================")

while iteracao <= 10: 
    erros = []
    quant_erros_menores = 0

    pontos[0] = (6 + pontos_anterior[1] - (2*pontos_anterior[2]))/10
    pontos[1] = (25 + pontos_anterior[0] + pontos_anterior[2] - (3*pontos_anterior[3]))/11
    pontos[2] = (-11 - (2*pontos_anterior[0]) + pontos_anterior[1] + pontos_anterior[3])/10
    pontos[3] = (15 - (3*pontos_anterior[1]) + pontos_anterior[2])/8
    
    for i in range(len(pontos)):
        erros.append(abs(pontos[i] - pontos_anterior[i]))
        pontos_anterior[i] = pontos[i]

    for i in range(len(erros)):
        if erros[i] < erro_aceitavel:
            quant_erros_menores += 1

    print("Iteração", iteracao, ":")
    print("Erros:", np.round(erros, 5))

    if quant_erros_menores == len(pontos):
        break

    iteracao += 1

for i in range(len(pontos)):
    print("Ponto", i+1, ":", pontos[i])"""

"""print("=================== B =====================")

while iteracao <= 10:
    erros = []
    quant_erros_menores = 0

    pontos[0] = (1 - pontos_anterior[1] + (4*pontos_anterior[2]) + pontos_anterior[3])
    pontos[1] = (1 + (10*pontos_anterior[0]) - (5*pontos_anterior[2]) + (6*pontos_anterior[3]))
    pontos[2] = (11 - pontos_anterior[0] + (11*pontos_anterior[1]) + (22*pontos_anterior[3]))/2
    pontos[3] = (-6 - pontos_anterior[0] + (18*pontos_anterior[1]) - (8*pontos_anterior[2]))/2
    
    for i in range(len(pontos)):
        erros.append(abs(pontos[i] - pontos_anterior[i]))
        pontos_anterior[i] = pontos[i]

    for i in range(len(erros)):
        if erros[i] < erro_aceitavel:
            quant_erros_menores += 1

    if quant_erros_menores == len(pontos):
        print("tetrste")
        break
    
    iteracao += 1

for i in range(len(pontos)):
    print("Ponto", i+1, ":", pontos[i])"""
