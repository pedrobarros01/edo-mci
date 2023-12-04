import math
from typing_extensions import TypedDict
import matplotlib.pyplot as plt
import pandas as pd


class Ponto_Kutta4(TypedDict):
  x: float | int
  y: float | int
  K1: float | int
  K2: float | int
  K3: float | int
  K4: float | int


class RangeKutta4K:
  def __init__(self, n: int, h: float | int, x0=0, y0=1, f_xy=None) -> None:
    self.n = n
    self.h = h
    self.f_xy = f_xy
    K1 = self.f_xy(x0, y0)
    K2 = self.f_xy(x0 + (1/2*self.h), y0 + (1/2*K1*self.h))
    K3 = self.f_xy(x0 + (1/2*self.h), y0 + (1/2*K2*self.h))
    K4  =self.f_xy(x0 + self.h, y0 + (K3*self.h))
    ponto_inicial: Ponto_Kutta4 = {'x': x0, 'y':y0, 'K1': K1, 'K2': K2, 'K3': K3, 'K4': K4}
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
      print(f'K3 = {ponto["K3"]}')
      print(f'K4 = {ponto["K4"]}')
      print('='*15)


  def edo(self):
     i = 1
     while i <= self.n:
      ponto = self.lista_result[i - 1]
      xi = ponto['x']
      yi = ponto['y']
      K1 = ponto['K1']
      K2 = ponto['K2']
      K3 = ponto['K3']
      K4 = ponto['K4']
      y_n1 = yi + (K1 + 2*K2 + 2*K3 + K4)*(self.h / 6)
      x_n = xi + self.h
      x_n = round(x_n, 2)


      K1_n = self.f_xy(x_n, y_n1)
      K2_n = self.f_xy(x_n + (1/2*self.h), y_n1 + (1/2*K1_n*self.h))
      K3_n = self.f_xy(x_n + (1/2*self.h), y_n1 + (1/2*K2_n*self.h))
      K4_n  =self.f_xy(x_n + self.h, y_n1 + (K3_n*self.h))
      ponto_novo: Ponto_Kutta4 = {'x': x_n, 'y': y_n1, 'K1': K1_n, 'K2': K2_n, 'K3': K3_n, 'K4': K4_n}
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
  range_kutta4 = RangeKutta4K(n, h_1_q, x0_1_q, y0_1_q, f_xy=func_1_q)
  range_kutta4.edo()
  range_kutta4.printar()
  range_kutta4.plotar_grafico('questao 1')
  df = pd.DataFrame(range_kutta4.lista_result)

  range_kutta4 = RangeKutta4K(n, h_2_q, x0_2_q, y0_2_q, f_xy=func_2_q)
  range_kutta4.edo()
  range_kutta4.plotar_grafico('questao 2')
  df = pd.DataFrame(range_kutta4.lista_result)
