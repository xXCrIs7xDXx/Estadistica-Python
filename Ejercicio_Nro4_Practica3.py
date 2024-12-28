import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Definir la distribución
distribucion = stats.chi2(df=17)

# Calcular a y b
a = distribucion.ppf((1 - 0.88) / 2)
b = distribucion.ppf(1 - 0.02)

# Imprimir los resultados
print(f'a tal que P(a < X < b) = 0.88 es {a}')
print(f'b tal que P(X > b) = 0.02 es {b}')

# Generar valores para el eje x
x = np.linspace(distribucion.ppf(0.01), distribucion.ppf(0.99), 100)

# Calcular los valores de la pdf para cada x
pdf = distribucion.pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'r-', lw=2, label='chi2 pdf')
plt.fill_between(x, pdf, color='red', alpha=0.2)
plt.title('Distribución Chi Cuadrado con 17 grados de libertad')
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.fill_between(x, pdf, where=(x>a) & (x<b), color='blue', alpha=0.3, label='P(a < X < b) = 0.88')
plt.axvline(b, color='green', linestyle='--', label='P(X > b) = 0.02')
plt.legend(loc='best')
plt.grid(True)
plt.show()