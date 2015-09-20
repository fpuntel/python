##########
# Fernando Emilio Puntel
# 09/2015
# Inversao de Matriz e Matriz Transposta
# Comparar a diferenca como matlab
#####

from datetime import datetime # Biblioteca utilizada para calcular o tempo

# Bibliotecas para manipulacao de matriz. Caso nao tenha a bib numpy, eh preciso instalar:
# apt-cache policy python-numpy
# sudo apt-get install python-numpy
from numpy import matrix
from numpy import linalg
import numpy

# Utilizada para povoar a matriz
import random

# Total de posicoes matriz (Matriz quadrada 1000 x 1000)
t = 1000

# Valores uniformes entre -1 e 1	
x = numpy.random.uniform(-1, 1, size=(t,t))	

# MatrizTransposta e MatrizInversa povoadas com zero
matrizTransposta = numpy.zeros((t,t))
matrizInversa = numpy.zeros((t,t))

# Matriz Transposta
matrizTransposta = x.T

# Matriz Inversa
now = datetime.now() # Tempo inicial
print(now.hour, now.minute, now.second)
matrizInversa = numpy.linalg.inv(x)
now = datetime.now() # Tempo final
print(now.hour, now.minute, now.second)

# Tamanho matrizes para conferencia
print (matrizTransposta.shape)
print (matrizInversa.shape)

