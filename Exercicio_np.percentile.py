import numpy as np

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 150])

print(dados)

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 100)
q3 = np.percentile(dados, 15)

print(q1)
print(q2)
print(q3)






