import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Función para crear el archivo .dzn con los datos de entrada
def crear_archivo_dzn():
    # Obtener los datos de la interfaz de entrada
    datos = entrada_texto.get("1.0", tk.END).strip()
    
    # Guardar los datos en el archivo DatosProyecto.dzn
    with open("DatosProyecto.dzn", "w") as f:
        f.write(datos)
    
    messagebox.showinfo("Archivo DZN", "Archivo DatosProyecto.dzn creado exitosamente")

# Función para ejecutar el modelo .mzn con el archivo .dzn y mostrar los resultados
def ejecutar_modelo():
    try:
        # Comando para ejecutar MiniZinc
        resultado = subprocess.check_output(
            ["minizinc", "Proyecto.mzn", "DatosProyecto.dzn"],
            universal_newlines=True
        )
        
        # Mostrar los resultados en la interfaz
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el modelo: {e}")

# Configuración de la interfaz principal
ventana = tk.Tk()
ventana.title("Configurador de Modelo MiniZinc")
ventana.geometry("500x600")

# Etiqueta y campo de entrada de datos
tk.Label(ventana, text="Ingrese los datos de entrada (formato DZN):").pack(pady=5)
entrada_texto = tk.Text(ventana, height=10, width=50)
entrada_texto.pack(pady=5)

# Botón para crear archivo DZN
boton_crear_dzn = tk.Button(ventana, text="Crear archivo DZN", command=crear_archivo_dzn)
boton_crear_dzn.pack(pady=10)

# Botón para ejecutar el modelo
boton_ejecutar_modelo = tk.Button(ventana, text="Ejecutar modelo", command=ejecutar_modelo)
boton_ejecutar_modelo.pack(pady=10)

# Etiqueta y campo de salida de datos
tk.Label(ventana, text="Salida del modelo:").pack(pady=5)
salida_texto = tk.Text(ventana, height=10, width=50)
salida_texto.pack(pady=5)

# Cerrar la ventana principal
ventana.mainloop()
