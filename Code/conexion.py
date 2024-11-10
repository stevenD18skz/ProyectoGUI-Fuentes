from minizinc import Instance, Model, Solver

# Cargar el modelo de MiniZinc
model = Model("modelo1.mzn")
model.add_file("prueba1.dzn")

# Configurar el solver de MiniZinc, en este caso, Gecode
gecode = Solver.lookup("gecode")

# Crear una instancia del modelo con el solver configurado
instance = Instance(gecode, model)

# Resolver el problema
result = instance.solve()

# Verificar si se encontró una solución
if result.solution is not None:
    print("Solución encontrada:")
    print(result)
else:
    print("No se encontró solución.")
