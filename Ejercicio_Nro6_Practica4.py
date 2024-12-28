import numpy as np
import matplotlib.pyplot as plt

# a) Estimador de máxima verosimilitud de p
n = 20  # Número total de cascos
x = 3   # Número de cascos agrietados
p_hat = x / n  # Estimador de máxima verosimilitud de p
print(f'Estimación de p: {p_hat}')  # Esto responde al inciso a)

# b) Verificar si el estimador es insesgado
# Un estimador es insesgado si su valor esperado es igual al parámetro que está estimando.
# En este caso, E(p_hat) = p, por lo que el estimador es insesgado.
print(f'¿Es insesgado el estimador? Sí')  # Esto responde al inciso b)

# c) Estimador de máxima verosimilitud de la probabilidad (1 - p)^5
prob_hat = (1 - p_hat)**5
print(f'Estimación de la probabilidad (1 - p)^5: {prob_hat}')  # Esto responde al inciso c)

# Gráfico de la distribución binomial con p estimado
plt.figure(figsize=(10, 6))
r_values = list(range(n + 1))  # Todos los posibles números de cascos agrietados
dist = [np.math.comb(n, r) * (p_hat*r) * ((1 - p_hat)*(n - r)) for r in r_values]  # Distribución binomial
plt.bar(r_values, dist)
plt.title('Distribución binomial con p estimado')
plt.xlabel('Número de cascos agrietados')
plt.ylabel('Probabilidad')
plt.show()  # Esto genera el gráfico