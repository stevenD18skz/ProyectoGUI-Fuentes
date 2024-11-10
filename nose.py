import numpy as np

# Lista de ejemplo
p = np.array([1, 1, 1, 1, 1])
v = np.array([0.109, 0.391, 0.481, 0.789, 0.976])


lista = np.repeat(v, p)
mediana = np.median(lista)


pol = np.sum(p * np.abs(v - mediana))



print(f"POL {pol}")

"""
pol = 0.09
DatosProyecto1": {
    "timestamp": "2024-11-10T04:59:34.706Z",
    "result": "Optimal Solution:\r\n---------------\r\nPolarization = 0.08999999999999997\r\nMedian = 0.481\r\n\r\nMovements (from -> to : amount):\r\n  1 -> 3 : 1\r\n  4 -> 3 : 1\r\n  5 -> 3 : 1\r\n\r\nFinal distribution:\r\nOpinion\tValue\tPopulation\tInitially Empty?\r\n1\t0.109\t0\t\"No\"\r\n2\t0.391\t1\t\"No\"\r\n3\t0.481\t4\t\"No\"\r\n4\t0.789\t0\t\"No\"\r\n5\t0.976\t0\t\"No\"\r\n\r\nTotal cost: 6.5988\r\nTotal movements: 3\r\n----------\r\n==========\r\n",
    "isError": false,
    "inputFile": "DatosProyecto1.dzn"
  },
"""