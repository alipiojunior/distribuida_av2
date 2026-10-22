import matplotlib.pyplot as plt
import numpy as np

instancias = ['1', '2', '3']
users_10 = [1.1, 1.3, 1.3]
users_100 = [14.2, 13.6, 14.3]
users_1000 = [77.5, 71.7, 76.6]

x = np.arange(len(instancias))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width, users_10, width, label='10 utilizadores', color='#ccebc5', edgecolor='black')
rects2 = ax.bar(x, users_100, width, label='100 utilizadores', color='#7bccc4', edgecolor='black')
rects3 = ax.bar(x + width, users_1000, width, label='1000 utilizadores', color='#fec44f', edgecolor='black')

ax.set_xlabel('Número de instâncias')
ax.set_ylabel('Requisições por segundo (s)')
ax.set_title('Cenário 2 - Publicação de Texto (400KB)')
ax.set_xticks(x)
ax.set_xticklabels(instancias)
ax.legend()

plt.tight_layout()
plt.savefig('grafico_rps_cenario2.png')
print("Gráfico gerado e guardado como grafico_rps_cenario2.png")