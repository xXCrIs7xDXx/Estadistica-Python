import numpy as np
import matplotlib.pyplot as plt

# Datos de la cantidad mensual de accidentes
accidentes = np.array([1, 0, 2, 0, 1, 1, 0, 2, 1, 0, 1, 3])

# Estimador de máxima verosimilitud de lambda
# Para una distribución de Poisson, el estimador de máxima verosimilitud de lambda es la media de los datos.
lambda_hat = np.mean(accidentes)

print(f'Estimación de lambda: {lambda_hat}')  # Esto responde a tu pregunta

# Crear el histograma de los datos
plt.hist(accidentes, bins=np.arange(-0.5, max(accidentes)+1.5), rwidth=0.8)
plt.title('Histograma de accidentes mensuales')
plt.xlabel('Número de accidentes')
plt.ylabel('Frecuencia')
plt.xticks(np.arange(max(accidentes)+1))
plt.show()  # Esto genera el gráfico