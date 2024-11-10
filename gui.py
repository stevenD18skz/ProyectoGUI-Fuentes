import tkinter as tk
from tkinter import messagebox
import subprocess

class MiniZincConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurador de Modelo MiniZinc")
        self.root.geometry("500x600")

        # Crear interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de entrada de datos
        tk.Label(self.root, text="Ingrese los datos de entrada (formato DZN):").pack(pady=5)
        self.entrada_texto = tk.Text(self.root, height=10, width=50)
        self.entrada_texto.pack(pady=5)

        # Botón para crear archivo DZN
        boton_crear_dzn = tk.Button(self.root, text="Crear archivo DZN", command=self.crear_archivo_dzn)
        boton_crear_dzn.pack(pady=10)

        # Botón para ejecutar el modelo
        boton_ejecutar_modelo = tk.Button(self.root, text="Ejecutar modelo", command=self.ejecutar_modelo)
        boton_ejecutar_modelo.pack(pady=10)

        # Etiqueta y campo de salida de datos
        tk.Label(self.root, text="Salida del modelo:").pack(pady=5)
        self.salida_texto = tk.Text(self.root, height=10, width=50)
        self.salida_texto.pack(pady=5)

    def crear_archivo_dzn(self, nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            # Leer los datos del archivo .mpl
            n = int(archivo.readline().strip())  # Número de personas
            m = int(archivo.readline().strip())  # Número de opiniones
            
            opiniones_iniciales = list(map(int, archivo.readline().strip().split(',')))
            valores_opiniones = list(map(float, archivo.readline().strip().split(',')))
            costos_extras = list(map(int, archivo.readline().strip().split(',')))
            
            # Leer la matriz de costos de desplazamiento
            costos_desplazamiento = []
            for _ in range(m):
                fila = list(map(int, archivo.readline().strip().split(',')))
                costos_desplazamiento.append(fila)
            
            # Leer ct y maxMovs
            ct = int(archivo.readline().strip())
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
        with open("DatosProyecto.dzn", "w") as archivo_dzn:
            archivo_dzn.write(contenido_dzn)
        
        print("Archivo DatosProyecto.dzn creado exitosamente")
            
        messagebox.showinfo("Archivo DZN", "Archivo DatosProyecto.dzn creado exitosamente")

    def ejecutar_modelo(self):
        try:
            # Comando para ejecutar MiniZinc
            resultado = subprocess.check_output(
                ["minizinc", "Proyecto.mzn", "DatosProyecto.dzn"],
                universal_newlines=True
            )
            
            # Mostrar los resultados en la interfaz
            self.salida_texto.delete("1.0", tk.END)
            self.salida_texto.insert(tk.END, resultado)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el modelo: {e}")

