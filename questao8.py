
#8) Escreva uma função que receba uma string e uma lista.
#A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.
def pertence(string, lista):
    if string in lista:
        return True
    else:
        return False


print(pertence("teste", ["foo",2,"teste"]))
