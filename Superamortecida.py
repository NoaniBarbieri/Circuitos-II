#Alunas: Manoella Leite e Noani Barbieri 
#Matéria: Circuitos 2

#Definindo as bibliotecas
import math
import numpy as np
import matplotlib.pyplot as plt

#parametros escolhidos para realização dos graficos
R = 400
L = 1.25
C = 1.25e-6
A = 20
Wo = 1/(math.sqrt(L*C))
alfa = (R/(2*L))
r =  math.sqrt((pow(alfa,2))-(pow(Wo,2)))

#frequencia definida
t = np.arange(0, 5e-2, 1e-5)

#auxiliares
K1=(A/(2*L*r))

#definindo a corrente pelos calculos realizados
iT=np.array([])
for i in t:
    iT = np.append(iT,((K1*math.exp(-(alfa-r)*i)) - (K1*math.exp(-(alfa+r)*i))))

#definindo a tensão pelos calculos realizados
vT=np.array([])
for i in t:
    vT=np.append(vT,((A/(L*C*(alfa**2-r**2)))+(A/(L*C*(2*r**2+2*r*alfa)))*math.exp((-alfa-r)*i)+(A/(L*C*(2*r**2-2*r*alfa))*math.exp((-alfa+r)*i))))

#funções para plotar graficos
fig, ax1 = plt.subplots(1, 1)
fig2, ax2 = plt.subplots(1, 1)

#grafico corrente
ax1.plot(t, iT, 'r-', linewidth=2)
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Corrente-i(t)")
ax1.grid(True)
ax1.set_title('Grafico Corrente')
ax1.set_xlim(0,5e-2)

#grafico tensao
ax2.plot(t, vT, 'r-', linewidth=2)
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Tensao-v(t)")
ax2.grid(True)
ax2.set_title('Grafico Tensao')
ax2.set_xlim(0,5e-2)

fig.tight_layout()
fig2.tight_layout()

plt.show()

#fim