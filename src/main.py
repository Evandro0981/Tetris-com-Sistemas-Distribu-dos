from configuracao import *
from sys import exit

class Main:
     def __init__(self):
          pygame.init()
          # Criando a superfície do jogo com o pygame 
          self.exibir_superficie = pygame.display.set_mode((LARGURA_JANELA, LARGURA_JANELA))
          # Utilizaremos o relógio para várias coisas no jogo, já que ele permitirá que mexamos com o tempo do jogo.
          self.relogio = pygame.time.Clock()
          # Título da janela
          pygame.display.set_caption('Tetris')
          
     def executar(self):
          while True:
               # Esta sessão serve para finalizar o programa, sem ela a janela do jogo rodaria sem parar.
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         pygame.quit()
                         exit()
               
               # Exibição
               self.exibir_superficie.fill(CINZA)
             
               # Atualizando o jogo
               # Atualiza tudo que vemos dentro do jogo, assim podemos ver a janela do jogo
               pygame.display.update()
               '''clock' é um objeto que permite controlar os quadros (frames) do jogo, por exemplo:
                  Se quisermos que o jogo rode a 60fps apenas faça: self.relogio.clock.tick(60).
                  Caso não haja argumentos, o jogo rodará com a quantidade máxima de quadros por segundo
               '''
               self.relogio.clock.tick()
               
if __name__ == '__main__':
     main = Main()
     main.executar()    