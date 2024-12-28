import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Definir la distribución
distribucion = stats.chi2(df=29)

# Calcular alpha
alpha_a = distribucion.ppf(1 - 0.70)
alpha_b = distribucion.ppf(0.15)

# Imprimir los resultados
print(f'a) Alpha tal que P(X >= alpha) = 0.70 es {alpha_a}')
print(f'b) Alpha tal que P(X <= alpha) = 0.15 es {alpha_b}')

# Generar valores para el eje x
x = np.linspace(distribucion.ppf(0.01), distribucion.ppf(0.99), 100)

# Calcular los valores de la pdf para cada x
pdf = distribucion.pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'r-', lw=2, label='chi2 pdf')
plt.fill_between(x, pdf, color='red', alpha=0.2)
plt.title('Distribución Chi Cuadrado con 29 grados de libertad')
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.axvline(alpha_a, color='blue', linestyle='--', label=f'P(X >= {alpha_a:.2f}) = 0.70')
plt.axvline(alpha_b, color='green', linestyle='--', label=f'P(X <= {alpha_b:.2f}) = 0.15')
plt.legend(loc='best')
plt.grid(True)
plt.show()