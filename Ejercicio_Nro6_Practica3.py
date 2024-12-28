import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Definir la distribución
distribucion = stats.t(df=8)

# Calcular la probabilidad
P = distribucion.cdf(4)

# Imprimir el resultado
print(f'P(X <= 4) = {P}')

# Generar valores para el eje x
x = np.linspace(distribucion.ppf(0.01), distribucion.ppf(0.99), 100)

# Calcular los valores de la pdf para cada x
pdf = distribucion.pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'r-', lw=2, label='t pdf')
plt.fill_between(x, pdf, color='red', alpha=0.2)
plt.title('Distribución t con 8 grados de libertad')
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.fill_between(x, pdf, where=(x<=4), color='blue', alpha=0.3, label='P(X <= 4)')
plt.legend(loc='best')
plt.grid(True)
plt.show()