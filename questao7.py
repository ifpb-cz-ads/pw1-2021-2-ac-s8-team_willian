##7) Escreva uma função para validar uma variável string.
# Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo,
# falso em caso contrário.
def soma(string, min, max):
    tamanho = len(string)
    if tamanho >= min and tamanho <= max:
        return True
    else:
        return False


print(soma("string teste", 1, 5))
print(soma("string teste 2", 1, 20))
