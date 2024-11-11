import numpy as np
from itertools import product

# Lista de ejemplo
v = np.array([0.011,0.214,0.29,0.829,0.944])

# Generar todas las combinaciones de p que suman 5
def generate_combinations(n, total):
    return [comb for comb in product(range(total + 1), repeat=n) if sum(comb) == total]

# Función para calcular POL
def calculate_pol(p, v):
    lista = np.repeat(v, p)
    mediana = np.median(lista)
    return np.sum(p * np.abs(v - mediana))

# Generar combinaciones para p
combinations = generate_combinations(len(v), 10)

# Calcular y mostrar el POL para cada combinación de p
for p in combinations:
    p_array = np.array(p)
    pol = calculate_pol(p_array, v)
    print(f"p: {p_array} -> POL: {pol}")

"""
p: [0 4 1 0 0] -> POL: 0.08999999999999997
p: [0 1 4 0 0] -> POL: 0.08999999999999997
"""
"""
pol = 0.09
DatosProyecto1": {
    "timestamp": "2024-11-10T04:59:34.706Z",
    "result": "Optimal Solution:\r\n---------------\r\nPolarization = 0.08999999999999997\r\nMedian = 0.481\r\n\r\nMovements (from -> to : amount):\r\n  1 -> 3 : 1\r\n  4 -> 3 : 1\r\n  5 -> 3 : 1\r\n\r\nFinal distribution:\r\nOpinion\tValue\tPopulation\tInitially Empty?\r\n1\t0.109\t0\t\"No\"\r\n2\t0.391\t1\t\"No\"\r\n3\t0.481\t4\t\"No\"\r\n4\t0.789\t0\t\"No\"\r\n5\t0.976\t0\t\"No\"\r\n\r\nTotal cost: 6.5988\r\nTotal movements: 3\r\n----------\r\n==========\r\n",
    "isError": false,
    "inputFile": "DatosProyecto1.dzn"
  },
"""