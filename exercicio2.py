#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)


# def is_anagram(string1, string2):


def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if sorted(string1) == sorted(string2):
        return True

    else:
        return False




        














