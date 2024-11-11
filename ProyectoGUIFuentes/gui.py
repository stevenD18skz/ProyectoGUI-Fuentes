import time
import tkinter as tk
from tkinter import messagebox, filedialog

from conexion import MiniZincSolver

class MiniZincConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurador de Modelo MiniZinc")
        self.root.geometry("500x600")

        # Variable para almacenar la ruta del archivo cargado
        self.archivo_mpl = None

        # Crear interfaz
        self.create_widgets()


    def create_widgets(self):
        # Etiqueta y campo de entrada de datos
        tk.Label(self.root, text="Ingrese los datos de entrada (formato DZN):").pack(pady=5)
        self.entrada_texto = tk.Text(self.root, height=10, width=50)
        self.entrada_texto.pack(pady=5)

        # Botón para cargar archivo .mpl
        boton_cargar_archivo = tk.Button(self.root, text="Cargar archivo .mpl", command=self.cargar_archivo)
        boton_cargar_archivo.pack(pady=10)

        # Botón para crear archivo DZN
        boton_crear_dzn = tk.Button(self.root, text="Crear archivo DZN", command=lambda: self.crear_archivo_dzn(self.archivo_mpl))
        boton_crear_dzn.pack(pady=10)

        # Botón para ejecutar el modelo
        boton_ejecutar_modelo = tk.Button(self.root, text="Ejecutar modelo", command=self.ejecutar_modelo)
        boton_ejecutar_modelo.pack(pady=10)

        # Etiqueta y campo de salida de datos
        tk.Label(self.root, text="Salida del modelo:").pack(pady=5)
        self.salida_texto = tk.Text(self.root, height=10, width=50)
        self.salida_texto.pack(pady=5)



    def cargar_archivo(self):
        # Abrir un selector de archivos para elegir el archivo .mpl
        self.archivo_mpl = filedialog.askopenfilename(
            title="Seleccionar archivo .mpl",
            filetypes=[("Archivos MPL", "*.mpl"), ("Todos los archivos", "*.*")]
        )
        

        if self.archivo_mpl:
            messagebox.showinfo("Archivo Cargado", f"Archivo cargado: {self.archivo_mpl}")
            print(self.archivo_mpl)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")



    def crear_archivo_dzn(self, nombre_archivo):
        if not nombre_archivo:
            messagebox.showerror("Error", "No se ha cargado ningún archivo .mpl.")
            return
        
        with open(nombre_archivo, "r") as archivo:
            # Leer los datos del archivo .mpl
            n = int(archivo.readline().strip())  # Número de personas
            m = int(archivo.readline().strip())  # Número de opiniones
            
            opiniones_iniciales = list(map(int, archivo.readline().strip().split(',')))
            valores_opiniones = list(map(float, archivo.readline().strip().split(',')))
            costos_extras = list(map(float, archivo.readline().strip().split(',')))
            
            # Leer la matriz de costos de desplazamiento
            costos_desplazamiento = []
            for _ in range(m):
                fila = list(map(float, archivo.readline().strip().split(',')))
                costos_desplazamiento.append(fila)
            
            # Leer ct y maxMovs
            ct = float(archivo.readline().strip())
            maxMovs = int(archivo.readline().strip())
        
        # Crear el contenido del archivo .dzn
        contenido_dzn = (
            f"n = {n};\n"
            f"m = {m};\n\n"
            f"opiniones_iniciales = {opiniones_iniciales};\n\n"
            f"valores_opiniones = {valores_opiniones};\n\n"
            f"costos_extras = {costos_extras};\n\n"
            f"costos_desplazamiento = [|"
        )
        
        # Agregar la matriz de costos de desplazamiento con formato
        contenido_dzn += "\n    | ".join(
            ", ".join(map(str, fila)) for fila in costos_desplazamiento
        )
        contenido_dzn += " |];\n\n"
        
        contenido_dzn += f"ct = {ct};\n\n"
        contenido_dzn += f"maxMovs = {maxMovs};\n"
        
        # Guardar en el archivo DatosProyecto.dzn
        with open("ProyectoGUIFuentes/DatosProyecto.dzn", "w") as archivo_dzn:
            archivo_dzn.write(contenido_dzn)
        
        messagebox.showinfo("Archivo DZN", "Archivo DatosProyecto.dzn creado exitosamente")



    def ejecutar_modelo(self):
        try:
            print(f"\n\nresolviendo:......")
    
            start_time = time.time()

            solver = MiniZincSolver("Proyecto.mzn", "ProyectoGUIFuentes/DatosProyecto.dzn")
            solver.load_model()
            solver.configure_solver()
            result = solver.solve()
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tiempo transcurrido: {elapsed_time:2f} segundos")
                    
            # Mostrar los resultados en la interfaz
            self.salida_texto.delete("1.0", tk.END)
            self.salida_texto.insert(tk.END, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el modelo: {e}")

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniZincConfigurator(root)
    root.mainloop()
