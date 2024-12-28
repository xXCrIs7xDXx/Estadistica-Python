import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Definir la distribución
distribucion = stats.chi2(df=4)

# Calcular las probabilidades
P_a = 1 - distribucion.cdf(0.484)
P_b = distribucion.cdf(10.026)
P_c = distribucion.cdf(16.924) - distribucion.cdf(0.711)
P_d = distribucion.cdf(5)

# Imprimir los resultados
print(f'a) P(X >= 0.484) = {P_a}')
print(f'b) P(X <= 10.026) = {P_b}')
print(f'c) P(0.711 <= X <= 16.924) = {P_c}')
print(f'd) P(X < 5) = {P_d}')

# Generar valores para el eje x
x = np.linspace(distribucion.ppf(0.01), distribucion.ppf(0.99), 100)

# Calcular los valores de la pdf para cada x
pdf = distribucion.pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'r-', lw=2, label='chi2 pdf')
plt.fill_between(x, pdf, color='red', alpha=0.2)
plt.title('Distribución Chi Cuadrado con 4 grados de libertad')
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.legend(loc='best')
plt.grid(True)
plt.show()