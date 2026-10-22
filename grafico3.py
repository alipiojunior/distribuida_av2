import matplotlib.pyplot as plt
import numpy as np

instancias = ['1', '2', '3']
users_10 = [1.5, 1.5, 1.3]
users_100 = [14.9, 14.3, 14.1]
users_1000 = [76.9, 73.3, 72.3]

x = np.arange(len(instancias))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width, users_10, width, label='10 utilizadores', color='#ccebc5', edgecolor='black')
rects2 = ax.bar(x, users_100, width, label='100 utilizadores', color='#7bccc4', edgecolor='black')
rects3 = ax.bar(x + width, users_1000, width, label='1000 utilizadores', color='#fec44f', edgecolor='black')

ax.set_xlabel('Número de instâncias')
ax.set_ylabel('Requisições por segundo (s)')
ax.set_title('Cenário 3 - Publicação de Imagem (300KB)')
ax.set_xticks(x)
ax.set_xticklabels(instancias)
ax.legend()

plt.tight_layout()
plt.savefig('grafico_rps_cenario3.png')
print("Gráfico gerado e guardado como grafico_rps_cenario3.png")