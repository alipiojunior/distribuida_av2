import matplotlib.pyplot as plt
import numpy as np

instancias = ['1', '2', '3']
users_10 = [1.7, 1.3, 1.4]
users_100 = [14.6, 13.6, 14.2]
users_1000 = [71.6, 116.9, 111.2]

x = np.arange(len(instancias))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width, users_10, width, label='10 usuários', color='#ccebc5', edgecolor='black')
rects2 = ax.bar(x, users_100, width, label='100 usuários', color='#7bccc4', edgecolor='black')
rects3 = ax.bar(x + width, users_1000, width, label='1000 usuários', color='#fec44f', edgecolor='black')

ax.set_xlabel('Número de instâncias')
ax.set_ylabel('Requisições por segundo (s)')
ax.set_xticks(x)
ax.set_xticklabels(instancias)
ax.legend()

plt.tight_layout()
plt.savefig('grafico_rps_cenario1.png')
print("Gráfico gerado e guardado como grafico_rps_cenario1.png")