import math
from typing_extensions import TypedDict
import matplotlib.pyplot as plt
import pandas as pd


class Ponto_Euler(TypedDict):
  x: float | int
  y: float | int
  f_xy: float | int


class Euler:
  def __init__(self, n: int, h: float | int, x0=0, y0=1, f_xy=None) -> None:
    self.n = n
    self.h = h
    self.f_xy = f_xy
    f0_xy = self.f_xy(x0, y0)
    ponto_inicial: Ponto_Euler = {'x': x0, 'y': y0, 'f_xy':f0_xy}
    self.ponto_inicial = ponto_inicial
    self.lista_result = []
    self.lista_result.append(ponto_inicial)
    self.x = []
    self.y = []

  def printar(self):
    for i,ponto in enumerate(self.lista_result):
      print(f'n = {i}')
      print(f'x = {ponto["x"]}')
      print(f'y = {ponto["y"]}')
      print(f'f_xy = {ponto["f_xy"]}')
      print('='*15)

  def edo(self):
    i = 1
    x_n = self.ponto_inicial['x']
    while i <= self.n:
      ponto = self.lista_result[i - 1]
      x_n = ponto["x"] + self.h

      x_n = round(x_n, 10)
      y_n1 = ponto['y'] + self.h * ponto['f_xy']
      fn_xy = self.f_xy(x_n, y_n1)
      new_ponto:Ponto_Euler = {'x': x_n, 'y': y_n1, 'f_xy': fn_xy}
      self.lista_result.append(new_ponto)
      i+=1


  def plotar_grafico(self, titulo: str):
    for obj in self.lista_result:
      self.x.append(obj['x'])
      self.y.append(obj['y'])

    plt.title(titulo)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(self.x, self.y)
    plt.show()



  def erro(self):
    return super().erro()

if __name__ == '__main__':
    n = 30
    func_1_q = lambda x,y: x - 2*x*y
    x0_1_q = 0
    y0_1_q = 3
    h_1_q = 0.01

    func_2_q = lambda x,y: -0.06*math.sqrt(y)
    x0_2_q = 0
    y0_2_q = 3
    h_2_q = 1
    
    print('questao 1 - ')
    euler = Euler(n, h_1_q, x0_1_q, y0_1_q, f_xy=func_1_q)
    euler.edo()
    euler.printar()
    euler.plotar_grafico('questao 1')
    df = pd.DataFrame(euler.lista_result)

    print('questao 2 - ')
    euler = Euler(n, h_2_q, x0_2_q, y0_2_q, f_xy=func_2_q)
    euler.edo()
    euler.printar()
    euler.plotar_grafico('questao 2')
    df = pd.DataFrame(euler.lista_result)