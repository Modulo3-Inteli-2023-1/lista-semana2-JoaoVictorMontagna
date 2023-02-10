#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)


# def is_anagram(string1, string2):
p1=input("Digite a primeira palavra a ser comparada")

p2=input("Digite a segunda palavra a ser comparada")

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if sorted(string1) == sorted(string2):
        print(p1 + " e " + p2 +" são um anagrama")

    else:
        print(p1 + " e " + p2 +" não são um anagrama")

print(is_anagram(p1,p2))


        














