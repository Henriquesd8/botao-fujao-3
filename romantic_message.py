# Código em Python para exibir mensagem romântica
def exibir_mensagem_romantica():
    print("Te amo, meu amor!")

# Função para perguntar se quer namorar
resposta = input("Quer namorar comigo? (sim/não): ")

if resposta.lower() == "sim":
    exibir_mensagem_romantica()
else:
    print("Poxa, o botão escapou!")

exibir_mensagem_romantica()
