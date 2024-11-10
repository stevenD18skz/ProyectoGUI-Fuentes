from minizinc import Instance, Model, Solver

class MiniZincSolver:
    def __init__(self, model_file: str, data_file: str, solver_name: str = "gecode"):
        self.model_file = model_file
        self.data_file = data_file
        self.solver_name = solver_name
        self.model = None
        self.instance = None
        self.result = None

    def load_model(self):
        # Cargar el modelo de MiniZinc y el archivo de datos
        self.model = Model(self.model_file)
        self.model.add_file(self.data_file)

    def configure_solver(self):
        # Configurar el solver de MiniZinc
        solver = Solver.lookup(self.solver_name)
        if solver is None:
            raise ValueError(f"Solver '{self.solver_name}' no encontrado.")
        self.instance = Instance(solver, self.model)

    def solve(self):
        # Resolver el problema y almacenar el resultado
        self.result = self.instance.solve()
        return self.result

    def get_solution(self):
        # Verificar si se encontró una solución y devolverla
        if self.result and self.result.solution is not None:
            return self.result
        else:
            return "No se encontró solución."