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
          # Estamos definindo um retangulo aqui, para tracejar uma borda para todo o jogo.
          self.retangulo = self.superficie.get_rect(topleft = (ESPACAMENTO, ESPACAMENTO))
          
          # linhas
          self.superficie_linha = self.superficie.copy()
          self.superficie_linha.fill((0, 255, 0))
          self.superficie_linha.set_colorkey((0, 255, 0))
          self.superficie_linha.set_alpha(120)
          
          
     def desenhar_grade(self):
          '''  Observe que o metodo pygame.draw.line possui argumentos para representar o inicio e fim de uma linha.
               Logo após o argumento "LINHA_COR" está a posição inicial, que precisa ser representado por uma tupla,
               como exemplo, no desenho das linhas verticais, na tupla da posição inicial, nosso "x" é o tamanho da célula * a coluna atual,
               isso se deve pois, a cada iteração do loop a coluna será incrementada e o cálculo levará à posições mais distantes.
               Já nosso y é a posição 0 da superficie do jogo, pois ele representa aonde iniciará o tracejamento da linha, nesse caso,
               iniciará no topo da nossa superficie, por isso definimos como 0.
               
               A posição final, que é a segunda tupla, tem o mesmo raciocinio, primeiro definimos o "x" que é o espaçamento entre
               cada linha e depois pegado a altura da superficie (no caso das linhas verticais) 
               para definir até onde vai o tracejamento.
          '''
          # desenha as linhas verticais
          for coluna in range(1, COLUNAS):
               x = coluna * TAMANHO_CELULA
               pygame.draw.line(self.superficie_linha, LINHA_COR, (x, 0), (x, self.superficie.get_height()), 1)

          # desenha as linhas horizontais
          for linha in range(1, LINHAS):
               y = linha * TAMANHO_CELULA
               pygame.draw.line(self.superficie_linha, LINHA_COR, (0, y), (self.superficie.get_width(), y), 1)
          
          self.superficie.blit(self.superficie_linha, (0,0))
          
     def executar(self):
          self.superficie.fill(CINZA)
          self.desenhar_grade()
          
          # O método blit serve para colocarmos uma superficie em cima de outra superficie, nesse caso "superficie" -> "mostrar_superficie"
          self.mostrar_superficie.blit(self.superficie, (ESPACAMENTO, ESPACAMENTO))
          pygame.draw.rect(self.mostrar_superficie, LINHA_COR, self.retangulo, 2, 2)     
     