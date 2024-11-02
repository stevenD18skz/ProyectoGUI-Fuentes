from minizinc import Instance, Model, Solver

# Load n-Queens model from file
model = Model("././modelo1.mzn")
model.add_file("././prueba1.dzn")

# Find the MiniZinc solver configuration for Gecode
gecode = Solver.lookup("gecode")
# Create an Instance of the n-Queens model for Gecode
instance = Instance(gecode, model)

result = instance.solve()
# Output the array q
print("oaw")

# Procesar y mostrar los resultados
""" if result.success:
    print("Solución encontrada:")
    for solution in result.solutions:
        print(solution)  # Muestra cada variable de la solución
else:
    print("No se encontró solución.") """