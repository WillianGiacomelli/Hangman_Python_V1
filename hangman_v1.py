#Jogo da Forca - Versão 1 - Desenvolvimento de game utilizando a LP Python

#importação dos pacotes necessários
import random 
import re
from os import system,name

#função para limpar o prompt em cada execução 
def limpaTela():
    
    if name == "nt":
        _ = system("cls")
    else:
        _ = system('clear')

#função para verificar se o valor da tentativa é uma letra e apenas um valor utilizando regex
def verifica_tentativa(letra):
    padrao = r'^[a-zA-Z]$'
    return re.match(padrao, letra) is not None

#função do jogo
def game():
    
    limpaTela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #faz a leitura das palavras que estão no arquivo txt
    palavras = open('./palavras.txt', 'r')
    conteudo = palavras.read()
    lista_de_palavras = conteudo.split(",")
    lista_de_palavras_formatada = list(map(lambda p: p.lower(), lista_de_palavras))
    palavras.close()

    #escolha aleatória de uma palavra na lista 
    palavra_escolhida = random.choice(lista_de_palavras_formatada)

    letras_descobertas = ["_" for letra in palavra_escolhida]

    chances = len(palavra_escolhida) + 3

    letras_erradas = []

    #enquanto tiver tentativas
    while chances > 0:
        print("".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if verifica_tentativa(tentativa):

          qtde_carac_tentativa = len(tentativa)

          if tentativa in palavra_escolhida:
            index = 0

            for letra in palavra_escolhida:
                if letra == tentativa:
                    letras_descobertas[index] = tentativa
                index += 1
          else:
            chances -= 1
            letras_erradas.append(tentativa)

          if "_" not in letras_descobertas:
            print("\nParabéns! Você venceu, a palavra era:", palavra_escolhida)
            break
        else:
            print("O valor de entrada dever ser uma letra e apenas 1 valor")
    
    if "_" in letras_descobertas:
           print("\nVocê perdeu, a palavra era:", palavra_escolhida)


if __name__ == "__main__":
    game()