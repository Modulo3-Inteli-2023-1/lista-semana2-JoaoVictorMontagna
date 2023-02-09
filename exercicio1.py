#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui








# Teste a sua função aqui (caso ache necessário)
text=input("Digite um texto para contarmos as palavras unicas")

c=[",",".","?","!"]

for i in c:
    remover_pontos=text.replace(i,"")
    text=remover_pontos

palavras=text.split(" ")
palavrasUnicas=set(palavras)
qntPalavras=len(palavrasUnicas)
print(qntPalavras)

    






    





    
    












