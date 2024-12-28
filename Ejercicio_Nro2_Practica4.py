import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Datos de entrada
rayones = np.array([0, 1, 2, 3, 4, 5, 6, 7])
frecuencia = np.array([18, 37, 42, 30, 13, 7, 2, 1])

# a) Estimador insesgado de lambda
# Para una distribución de Poisson, E(X) = lambda. Por lo tanto, podemos estimar lambda como la media de los datos.
# Primero, calculamos la media ponderada de los rayones, que será nuestra estimación de lambda.
lambda_estimado = np.sum(rayones * frecuencia) / np.sum(frecuencia)
print(f'Estimación de lambda: {lambda_estimado}')  # Esto responde al inciso a)

# b) Desviación estándar (error estándar) del estimador
# Para una distribución de Poisson, Var(X) = lambda. Por lo tanto, la desviación estándar es la raíz cuadrada de lambda.
std_estimado = np.sqrt(lambda_estimado)
print(f'Error estándar estimado: {std_estimado}')  # Esto responde al inciso b)

# Gráfico de la distribución de Poisson estimada
x = np.arange(poisson.ppf(0.01, lambda_estimado), poisson.ppf(0.99, lambda_estimado))
plt.plot(x, poisson.pmf(x, lambda_estimado), 'bo', ms=8, label='poisson pmf')
plt.vlines(x, 0, poisson.pmf(x, lambda_estimado), colors='b', lw=5, alpha=0.5)
plt.title('Distribución de Poisson estimada')
plt.xlabel('Número de rayones')
plt.ylabel('Probabilidad')
plt.show()  # Esto genera el gráfico