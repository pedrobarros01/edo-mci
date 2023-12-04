import math
from typing_extensions import TypedDict
import matplotlib.pyplot as plt
import pandas as pd

class Ponto_Kutta2(TypedDict):
  x: float | int
  y: float | int
  K1: float | int
  K2: float | int


class RangeKutta2K:
  def __init__(self, n: int, h: float | int, x0=0, y0=1, f_xy=None) -> None:
    self.n = n
    self.h = h
    self.f_xy = f_xy
    K1 = self.f_xy(x0, y0)
    K2 = self.f_xy(x0 + self.h, (y0 + K1 * self.h))
    ponto_inicial: Ponto_Kutta2 = {'x': x0, 'y':y0, 'K1': K1, 'K2': K2}
    self.ponto_inicial = ponto_inicial
    self.lista_result = []
    self.x = []
    self.y = []
    self.lista_result.append(ponto_inicial)


  def printar(self):
    for i,ponto in enumerate(self.lista_result):
      print(f'n = {i}')
      print(f'x = {ponto["x"]}')
      print(f'y = {ponto["y"]}')
      print(f'K1 = {ponto["K1"]}')
      print(f'K2 = {ponto["K2"]}')
      print('='*15)

  def edo(self):
    i = 1
    while i <= self.n:
      ponto = self.lista_result[i - 1]
      yi = ponto['y']
      xi = ponto['x']
      K1 = ponto['K1']
      K2 = ponto['K2']
      y_n1 = yi + (1/2 * K1 + 1/2 * K2) * self.h
      xn = xi + self.h
      xn = round(xn, 2)
      K1_n = self.f_xy(xn, y_n1)
      K2_n = self.f_xy(xn + self.h, (y_n1 + K1_n * self.h))
      ponto_novo: Ponto_Kutta2 = {'x':xn, 'y': y_n1, 'K1': K1_n, 'K2': K2_n}
      self.lista_result.append(ponto_novo)
      i += 1

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
  range_kuta = RangeKutta2K(n, h_1_q, x0_1_q, y0_1_q, f_xy=func_1_q)
  range_kuta.edo()
  range_kuta.printar()
  df = pd.DataFrame(range_kuta.lista_result)

  range_kuta.plotar_grafico('questao 1')
  range_kuta = RangeKutta2K(n, h_2_q, x0_2_q, y0_2_q, f_xy=func_2_q)
  range_kuta.edo()
  range_kuta.printar()
  range_kuta.plotar_grafico('questao 2')
  df = pd.DataFrame(range_kuta.lista_result)