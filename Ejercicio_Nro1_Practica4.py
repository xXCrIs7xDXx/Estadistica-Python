import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Definir la distribución
distribucion = t(df=8)

# Generar muestras aleatorias
muestras = distribucion.rvs(size=1000)

# Definir los estimadores
X = 1/2*muestras[:500] + 1/2*muestras[500:]  # Estimador X
Y = 1/4*muestras[:500] + 3/4*muestras[500:]  # Estimador Y
Z = 1/3*muestras[:500] + 2/3*muestras[500:]  # Estimador Z

# Calcular las medias y las varianzas
media_X, var_X = np.mean(X), np.var(X)  # Media y varianza de X
media_Y, var_Y = np.mean(Y), np.var(Y)  # Media y varianza de Y
media_Z, var_Z = np.mean(Z), np.var(Z)  # Media y varianza de Z

# Imprimir los resultados
print(f'Media de X: {media_X}, Varianza de X: {var_X}')  # Resultados para X
print(f'Media de Y: {media_Y}, Varianza de Y: {var_Y}')  # Resultados para Y
print(f'Media de Z: {media_Z}, Varianza de Z: {var_Z}')  # Resultados para Z

# Calcular las eficiencias relativas
ER_Y = var_Y / var_X  # Eficiencia relativa de X respecto a Y
ER_Z = var_Z / var_X  # Eficiencia relativa de X respecto a Z

# Imprimir las eficiencias relativas
print(f'Eficiencia relativa de X respecto a Y: {ER_Y}')
print(f'Eficiencia relativa de X respecto a Z: {ER_Z}')

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.hist(X, bins=30, alpha=0.5, label='X')  # Histograma para X
plt.hist(Y, bins=30, alpha=0.5, label='Y')  # Histograma para Y
plt.hist(Z, bins=30, alpha=0.5, label='Z')  # Histograma para Z
plt.title('Distribuciones de los estimadores X, Y, Z')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend(loc='best')
plt.grid(True)
plt.show()