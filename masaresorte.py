# -*- coding: utf-8 -*-
"""MasaResorte.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFnipVQvotmFRBAsNiQHQ22EiaVBqM2u
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Oscilador:
  def __init__(self,ki,mi,b,tiempo,posicioninicialyi,velocidadiniciali,tiempoi):
    self.k = ki   #constante del resorte
    self.masa = mi  #masa que oscila
    self.b = b #factor de amortiguamiento
    self.tiempo = np.arange(0.0 , tiempoi, 0.1)
    self.posicioninicialy = posicioninicialyi 
    self.velocidadinicial = velocidadiniciali
    self.condicionesiniciales = [ self.posicioninicialy ,self.velocidadinicial]

  def funcionintegrable(self):
    def fun(y,t):
      return np.array([y[1], -(self.k /self.masa)* y[0]])
    return odeint(fun,self.condicionesiniciales,self.tiempo)

caso1 = Oscilador(2,3,4,5,6,7,8)
solucion = Oscilador.funcionintegrable(caso1)

plt.figure
plt.axes
fig, ax = plt.subplots(figsize=(15,15))
plt.title("Sistema no amortiguado")

plt.xlabel('tiempo [s]') 
plt.plot( caso1.tiempo, solucion[:,0], label="Posicion [m]")  
plt.plot( caso1.tiempo, solucion[:,1], label="Velocidad [m/s]")
plt.grid()
plt.legend()                              
plt.show()

plt.title("Diagrama de fase", 
          position=(0.3, 0.9),
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 10})
plt.xlabel('posicion [m]') 
plt.ylabel('velocidad [m/s]')
plt.plot( solucion[:,0], solucion[:,1], label="Espacio de fase")

class OsciladorAmortiguado:
  def __init__(self,ki,mi,b,tiempo,posicioninicialyi,velocidadiniciali,tiempoi):
    self.k = ki   #constante del resorte
    self.masa = mi  #masa que oscila
    self.b = b #factor de amortiguamiento
    self.tiempo = np.arange(0.0 , tiempoi, 0.1)
    self.posicioninicialy = posicioninicialyi 
    self.velocidadinicial = velocidadiniciali
    self.condicionesiniciales = [ self.posicioninicialy ,self.velocidadinicial]

  def funcionintegrable(self):
    def fun(y,t):
      return np.array([y[1], -(self.k /self.masa)* y[0]]+ (self.b/self.masa)*y[1])
    return odeint(fun,self.condicionesiniciales,self.tiempo)

caso2 = OsciladorAmortiguado(1,3,1,5,6,7,8)
solucion2 = OsciladorAmortiguado.funcionintegrable(caso2)

plt.figure
plt.axes
fig, ax = plt.subplots(figsize=(15,15))
plt.title("Sistema amortiguado")

plt.xlabel('tiempo [s]') 
plt.plot( caso2.tiempo, solucion2[:,0], label="Posicion [m]")  
plt.plot( caso2.tiempo, solucion2[:,1], label="Velocidad [m/s]")
plt.grid()
plt.legend()                              
plt.show()


plt.title("Diagrama de fase", 
          position=(0.3, 0.9),
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 10})
plt.xlabel('posicion [m]') 
plt.ylabel('velocidad [m/s]') 

plt.plot( solucion2[:,0], solucion2[:,1], label="Espacio de fase")

