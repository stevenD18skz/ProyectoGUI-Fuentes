from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter as ctk

class InterfazMPL:
    def __init__(self, root):
        self.root = root
        self.root.title('Prueba customtkinter')
        self.root.geometry('800x500')
        self.root.resizable(False, False)  # Hace la ventana fija
        self.configurar_ventana()
        self.crear_elementos()

        
    def configurar_ventana(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

    def crear_elementos(self):

        # Crear etiquetas y campos de entrada
        self.label_personas = ctk.CTkLabel(master=self.root, text="Numero de personas")
        self.label_personas.place(x=50, y=20)
        self.entry_personas = ctk.CTkEntry(master=self.root, width=100)
        self.entry_personas.place(x=190, y=20)

        self.label_opiniones = ctk.CTkLabel(master=self.root, text="Posibles opiniones")
        self.label_opiniones.place(x=50, y=60)
        self.entry_opiniones = ctk.CTkEntry(master=self.root, width=100)
        self.entry_opiniones.place(x=190, y=60)

        self.label_opinion_personas = ctk.CTkLabel(master=self.root, text="Opiniones por persona")
        self.label_opinion_personas.place(x=50, y=100)
        self.entry_opinion_personas = ctk.CTkEntry(master=self.root, width=100)
        self.entry_opinion_personas.place(x=190, y=100)

        self.label_costo_maximo = ctk.CTkLabel(master=self.root, text="Costo total permitido")
        self.label_costo_maximo.place(x=50, y=140)
        self.entry_costo_maximo = ctk.CTkEntry(master=self.root, width=100)
        self.entry_costo_maximo.place(x=190, y=140)

        self.label_max_movs = ctk.CTkLabel(master=self.root, text="Movimientos permitidos")
        self.label_max_movs.place(x=50, y=180)
        self.entry_max_movs = ctk.CTkEntry(master=self.root, width=100)
        self.entry_max_movs.place(x=190, y=180)

        self.label_valor_opinion = ctk.CTkLabel(master=self.root, text="Valor de opiniones")
        self.label_valor_opinion.place(x=50, y=220)
        self.entry_valor_opinion = ctk.CTkEntry(master=self.root, width=350)
        self.entry_valor_opinion.place(x=190, y=220)

        # Textbox para matriz de costo
        self.label_costo_desplazamiento = ctk.CTkLabel(master=self.root, text="Matriz de costo")
        self.label_costo_desplazamiento.place(x=300, y=20)
        self.textbox_costo_desplazamiento = ctk.CTkTextbox(master=self.root, width=350, height=150)
        self.textbox_costo_desplazamiento.place(x=400, y=20)

        # Crear botón para ver la matriz de desplazamiento
        self.btn_ver_matriz = ctk.CTkButton(self.root, text="Ver", command=self.ver_matriz, width=40, height=20)
        self.btn_ver_matriz.place(x=300, y=50)

        self.label_costo_opinion = ctk.CTkLabel(master=self.root, text="Costos extra")
        self.label_costo_opinion.place(x=315, y=180)
        self.entry_costo_opinion = ctk.CTkEntry(master=self.root, width=350)
        self.entry_costo_opinion.place(x=400, y=180)

        # Crear botones

        self.btn_Cargar = ctk.CTkButton(self.root, text="Cargar archivo .mpl", command=self.cargar_archivo)
        self.btn_Cargar.place(x=150, y=260)

        self.btn_Crear = ctk.CTkButton(self.root, text="Crear archivo DZN", command=self.crear_archivo_dzn)
        self.btn_Crear.place(x=325, y=260)

        self.btn_Ejecutar = ctk.CTkButton(self.root, text="Ejecutar modelo", command=self.ejecutar_modelo)
        self.btn_Ejecutar.place(x=500, y=260)

        # Textbox para salida de mensajes
        self.textbox_output = ctk.CTkTextbox(master=self.root, width=490, height=170)
        self.textbox_output.place(x=150, y=300)

    def ver_matriz(self):
        # Crear una nueva ventana para mostrar la matriz de desplazamiento
        matriz_ventana = Toplevel(self.root)
        matriz_ventana.title("Matriz de Desplazamiento")
        matriz_ventana.geometry("1000x400")

        # Crear un campo de texto para mostrar la matriz en la nueva ventana
        matriz_texto = Text(matriz_ventana, wrap=WORD, width=120, height=20)
        matriz_texto.pack(pady=10)

        # Agregar la matriz de desplazamiento (esto debe ser cargado desde el archivo previamente)
        matriz_texto.insert(END, self.textbox_costo_desplazamiento.get("1.0", END))
        matriz_texto.config(state=DISABLED)  # Para evitar edición de la matriz

    def cargar_archivo(self):
        # Abre un cuadro de diálogo para seleccionar el archivo .mpl
        file_path = filedialog.askopenfilename(filetypes=[("MPL files", "*.mpl")])
        if not file_path:
            return  # Si no se selecciona un archivo, termina la función

        # Lee el archivo y llena los campos correspondientes
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Asigna cada línea a su campo correspondiente
                self.entry_personas.delete(0, END)
                self.entry_personas.insert(0, lines[0].strip())

                self.entry_opiniones.delete(0, END)
                self.entry_opiniones.insert(0, lines[1].strip())

                self.entry_opinion_personas.delete(0, END)
                self.entry_opinion_personas.insert(0, lines[2].strip())

                self.entry_valor_opinion.delete(0, END)
                self.entry_valor_opinion.insert(0, lines[3].strip())

                self.entry_costo_opinion.delete(0, END)
                self.entry_costo_opinion.insert(0, lines[4].strip())

                # Cargar la "Matriz de costo" en el Textbox
                self.textbox_costo_desplazamiento.delete("1.0", END)
                for i in range(5, 5 + int(lines[1].strip())):  # m filas de la matriz
                    self.textbox_costo_desplazamiento.insert(END, lines[i])

                self.entry_costo_maximo.delete(0, END)
                self.entry_costo_maximo.insert(0, lines[5 + int(lines[1].strip())].strip())

                self.entry_max_movs.delete(0, END)
                self.entry_max_movs.insert(0, lines[6 + int(lines[1].strip())].strip())
                
                # Mostrar mensaje de éxito
                messagebox.showinfo("Éxito", "El archivo se cargó correctamente.")
        except Exception as e:
            # Si ocurre algún error, muestra un mensaje de error
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

    def crear_archivo_dzn(self):

        # Obtener datos de la interfaz
        n = int(self.entry_personas.get())
        m = int(self.entry_opiniones.get())
        opiniones_iniciales = list(map(int, self.entry_opinion_personas.get().split(',')))
        valores_opiniones = list(map(float, self.entry_valor_opinion.get().split(',')))
        costos_extras = list(map(float, self.entry_costo_opinion.get().split(',')))
        matriz_desplazamiento = self.textbox_costo_desplazamiento.get("1.0", END).strip().splitlines()
        matriz_costos = [list(map(float, row.split(','))) for row in matriz_desplazamiento]

        ct = float(self.entry_costo_maximo.get())
        max_movs = int(self.entry_max_movs.get())

        # Crear el contenido del archivo .dzn con formato ajustado
        contenido_dzn = (
            f"n = {n};\n"
            f"m = {m};\n\n"
            f"opiniones_iniciales = {opiniones_iniciales};\n\n"
            f"valores_opiniones = {valores_opiniones};\n\n"
            f"costos_extras = {costos_extras};\n\n"
            f"costos_desplazamiento = [|"
        )

        # Agregar la matriz de costos de desplazamiento en el formato correcto
        contenido_dzn += "\n    " + "\n    | ".join(
            ", ".join(map(str, fila)) for fila in matriz_costos
        ) + " |];\n\n"
        
        contenido_dzn += f"ct = {ct};\n\n"
        contenido_dzn += f"maxMovs = {max_movs};\n"

        # Guardar el archivo .dzn
        with open("ProyectoGUIFuentes/DatosProyecto.dzn", "w") as archivo_dzn:
            archivo_dzn.write(contenido_dzn)
        
        messagebox.showinfo("Archivo DZN", "Archivo .dzn creado exitosamente")


    def ejecutar_modelo(self):
        try:
            import time  # Asegúrate de importar time en la parte superior
            from minizinc import Instance, Model, Solver  # Asegúrate de tener minizinc-python instalado

            # Configuración del modelo y solución
            print(f"\n\nresolviendo:......")
            start_time = time.time()

            modelo = Model("Proyecto.mzn")
            solver = Solver.lookup("gecode")
            instance = Instance(solver, modelo)
            instance.add_file("ProyectoGUIFuentes/DatosProyecto.dzn")

            # Resolver el modelo
            result = instance.solve()
            end_time = time.time()
            elapsed_time = end_time - start_time

            dividir = str(result).split("\n")

            diccionario_resultado = {}

            for linea in dividir:
                clave, valor = linea.split(": ", 1)  # Divide en clave y valor usando ": " como separador
                # Convertir el valor a su tipo correspondiente si es posible (float, int, lista, etc.)
                if valor.startswith("[") and valor.endswith("]"):
                    valor = eval(valor)  # Convierte la cadena de lista a lista real (usa con precaución)
                elif valor.replace('.', '', 1).isdigit():
                    valor = float(valor) if '.' in valor else int(valor)
                diccionario_resultado[clave] = valor

            # Imprimir el diccionario final
            print(diccionario_resultado)

            """
            {'POL': 0.08999999999999997, 'Matriz de movimientos': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 'Nueva distribuccion de personas': [0, 1, 4, 0, 0], 'Costo': 5.499, 'Movimientos': 5}
            diccionario_resultado['Matriz de movimientos']
            """




            # Mostrar el tiempo de ejecución y resultados en la interfaz
            self.textbox_output.delete("1.0", END)
            self.textbox_output.insert(END, f"Tiempo transcurrido: {elapsed_time:.2f} segundos\n")
            self.textbox_output.insert(END, str(result))


            """
            -> la polarizacion
            -> la matriz de movimientos
            -> la nueva distribuccion de personas
            -> costo
            -> movimientos
            -> extra (explicacion matriz)

            output [
                "POL: ", show(Pol),
                "\nMatriz de movimientos", show(movimientos),
                "\nNueva distribuccion de personas", show(opiniones_nuevas),
                "\nCosto", show(sum(i in 1..m, j in 1..m) (movimientos[i, j] * costos_desplazamiento[i, j])),
                "\nMovimientos", show(sum(i in 1..m, j in 1..m) (movimientos[i, j] * abs(i - j))),
            ];


            """
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el modelo: {e}")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = ctk.CTk()
    app = InterfazMPL(root)
    root.mainloop()