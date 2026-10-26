'''
     Este arquivo serve para representarmos o jogo em si, 
     ele é o arquivo principal e que conterá a maior parte da lógica do projeto.
'''

from configuracao import *


class Jogo:
     def __init__(self):
          # Define a superficie da aba do jogo
          self.superficie = pygame.Surface((LARGURA_JOGO, ALTURA_JOGO))
          # Esse metodo permite com que obtenhamos o exibir_superficie, ou melhor dizendo, o display da superfície que estamos usando
          self.mostrar_superficie = pygame.display.get_surface()
          
     def executar(self):
          # O método blit serve para colocarmos uma superficie em cima de outra superficie, nesse caso "superficie" -> "mostrar_superficie"
          self.mostrar_superficie.blit(self.superficie, (ESPACAMENTO, ESPACAMENTO))     
     