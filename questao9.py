# 9) Altere o programa abaixo de forma que o usuário tenha três chances de acertar o número.
#   O programa termina se o usuário acertar ou errar três vezes.
#   A função ‘random.randint(x, y)’ recebe como parâmetros dois inteiros, x e y,
#   e retorna um outro inteiro escolhido aleatoriamente entre x e y.

import random

n = random.randint(1, 10)
contLose = 0
while contLose < 3:
    contLose +=1
    x = int(input("Escolha um número entre 1 e 10:"))
    if x == n:
        print("Você acertou!")
        contLose = 4
    else:
        print("Você errou.")
print("Fim de jogo!")
