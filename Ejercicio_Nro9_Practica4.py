import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Datos de resistencia al esfuerzo cortante
resistencia = np.array([392, 376, 401, 367, 389, 362, 409, 415, 358, 375])

# a) Estimador de máxima verosimilitud de la media y la desviación estándar
# Para una distribución normal, el estimador de máxima verosimilitud de la media es la media de la muestra,
# y el estimador de máxima verosimilitud de la desviación estándar es la desviación estándar de la muestra.
media_muestral = np.mean(resistencia)
desviacion_estandar_muestral = np.std(resistencia, ddof=1)
print(f'Media muestral: {media_muestral}')  # Esto responde al inciso a)
print(f'Desviación estándar muestral: {desviacion_estandar_muestral}')  # Esto responde al inciso a)

# b) Valor de resistencia por debajo del cual 95% de todas las soldaduras tendrán sus resistencias
# Esto es equivalente al percentil 95 de la distribución.
percentil_95 = norm.ppf(0.95, loc=media_muestral, scale=desviacion_estandar_muestral)
print(f'Percentil 95: {percentil_95}')  # Esto responde al inciso b)

# Gráfico de la distribución normal estimada
x = np.linspace(norm.ppf(0.01, loc=media_muestral, scale=desviacion_estandar_muestral),
norm.ppf(0.99, loc=media_muestral, scale=desviacion_estandar_muestral), 100)
plt.plot(x, norm.pdf(x, loc=media_muestral, scale=desviacion_estandar_muestral),
         'r-', lw=5, alpha=0.6, label='norm pdf')
plt.hist(resistencia, density=True, histtype='stepfilled', alpha=0.2)
plt.legend(loc='best', frameon=False)
plt.show()