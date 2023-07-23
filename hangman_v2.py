# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system,name

def limpaTela():
    
     if name == "nt":
        _ = system('cls')
     else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman():

	# Método Construtor
     
     def __init__(self, word):
         self.word = word
         self.tentativas = len(self.word) + 3
         self.letras_erradas = []
         self.letras_escolhidas = []
         self.word_hidden = []

	# Método para adivinhar a letra
     def guess(self,letra):
          if letra in self.word and letra not in self.letras_escolhidas:
               self.letras_escolhidas.append(letra)
               index=0
               for l in self.word:
                    if l == letra:
                         self.word[index]=letra
                    index+=1
                    
		
          elif letra not in self.word and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)
               self.tentativas -= 1
         

	# Método para verificar se o jogo terminou
     def hangman_over(self):
          return self.game_won() or (len(self.letras_erradas) == self.tentativas)
         

	# Método para verificar se o jogador venceu
     def game_won(self):
          if "_" not in self.word_hidden:
             return True
          return False
        
	# Método para não mostrar a letra no board
     def hide_word(self):

          self.word_hidden = []
          
          for letra in self.word:
               if letra not in self.letras_escolhidas:
                    self.word_hidden.append("_")
               else:
                    self.word_hidden.append(letra)
		
	# Método para checar o status do game e imprimir o board na tela
     def printBoard(self):
          print("Letra erradas:", self.letras_erradas)
          print("Letra escolhidas:", self.letras_escolhidas)
          print("Tentativas restantes:", self.tentativas)
          print(board[7 - self.tentativas])
		

def randomWord():

     palavras = open('./palavras.txt', 'r')
     conteudo = palavras.read()
     lista_de_palavras = conteudo.split(",")
     lista_de_palavras_formatada = list(map(lambda p: p.lower(), lista_de_palavras))
     palavras.close()

     palavra = random.choice(lista_de_palavras_formatada)
        
     return palavra

def main():
    
    limpaTela()

    hangman = Hangman(randomWord())

    while not hangman.hangman_over():
		
	     #  Status do game
          hangman.printBoard()
		
	     # Recebe input do terminal    
          user_input = input('\nDigite uma letra: ')
		
          # Verifica se a letra digitada faz parte da palavra
          hangman.guess(user_input)

	     # Verifica o status do jogo
          hangman.printBoard()

	     # De acordo com o status, imprime mensagem na tela para o usuário
          if hangman.game_won():
               print ('\nParabéns! Você venceu!!')
          else:
               print ('\nGame over! Você perdeu.')
               print ('A palavra era ' + hangman.word)
     
#Executa o programa  
if __name__ == "__main__":
    main()
