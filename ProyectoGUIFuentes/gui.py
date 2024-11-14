from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter as ctk
import time  # Asegúrate de importar time en la parte superior
from minizinc import Instance, Model, Solver  # Asegúrate de tener minizinc-python instalado


class InterfazMPL:
    def __init__(self, root):
        self.root = root
        self.root.title('GUI PROYECTO ADA II')
        self.root.geometry('800x500')
        self.root.resizable(False, False)
        self.configurar_ventana()
        self.crear_elementos()

        # Inicializar los botones y outputs en sus estados
        self.btn_Cargar.configure(state="normal")
        self.btn_Crear.configure(state="disabled")
        self.btn_Ejecutar.configure(state="disabled")
        self.diccionario_resultado = None

        
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

        self.btn_ver_movs = ctk.CTkButton(self.root, text="Ver Movimientos", command=self.ver_movimientos, width=40, height=30)
        self.btn_ver_movs.place(x=320, y=330)
        self.btn_ver_movs.configure(state="disabled")

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

        self.label_polarización = ctk.CTkLabel(master=self.root, text="Polarizacion final")
        self.label_polarización.place(x=50, y=300)
        self.entry_polarización = ctk.CTkEntry(master=self.root, width=100, state="readonly")
        self.entry_polarización.place(x=190, y=300)

        self.label_distribucion = ctk.CTkLabel(master=self.root, text="Movimientos totales")
        self.label_distribucion.place(x=50, y=340)
        self.entry_distribucion = ctk.CTkEntry(master=self.root, width=100, state="readonly")
        self.entry_distribucion.place(x=190, y=340)

        self.label_costo_final = ctk.CTkLabel(master=self.root, text="Costo utilizado")
        self.label_costo_final.place(x=50, y=380)
        self.entry_costo_final = ctk.CTkEntry(master=self.root, width=100, state="readonly")
        self.entry_costo_final.place(x=190, y=380)

        self.label_movs_final = ctk.CTkLabel(master=self.root, text="Distribucion final")
        self.label_movs_final.place(x=50, y=420)
        self.entry_movs_final = ctk.CTkEntry(master=self.root, width=200, state="readonly")
        self.entry_movs_final.place(x=190, y=420)

        self.label_matriz_final = ctk.CTkLabel(master=self.root, text="Matriz de movimientos")
        self.label_matriz_final.place(x=315, y=300)
        self.textbox_matriz_final = ctk.CTkTextbox(master=self.root, width=300, height=150)
        self.textbox_matriz_final.place(x=450, y=300)
        self.textbox_matriz_final.configure(state="disabled")



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
        matriz_texto.configure(state=DISABLED)  # Para evitar edición de la matriz



    def ver_movimientos(self):
        # Crear una nueva ventana para mostrar la matriz de movimientos
        movimientos_ventana = Toplevel(self.root)
        movimientos_ventana.title("Movimientos")
        movimientos_ventana.geometry("600x400")

        # Crear un campo de texto para mostrar la matriz en la nueva ventana
        movimientos_texto = Text(movimientos_ventana, wrap=WORD, width=120, height=20)
        movimientos_texto.pack(pady=10)

        # Obtener y procesar la matriz de movimientos
        Movimientos = self.diccionario_resultado.get("Matriz de movimientos", [])
        m = int(len(Movimientos) ** 0.5)
        matriz_mxm = [Movimientos[i * m:(i + 1) * m] for i in range(m)]

        # Generar la explicación de los movimientos
        explicacion = []
        for i in range(0, m):
            for j in range(0, m):
                if matriz_mxm[i][j] == 0:
                    continue
                explicacion.append(f"Se ha(n) movido {matriz_mxm[i][j]} persona(s) de la opinión({i+1}) a la opinión({j+1})")

        # Mostrar la explicación en el campo de texto
        movimientos_texto.insert(END, "\n".join(explicacion))
        movimientos_texto.configure(state=DISABLED)  # Para evitar edición de la matriz        



    def habilitar_boton(self, boton):
        if boton == "crear":
            self.btn_Crear.configure(state="normal")
            self.btn_ver_movs.configure(state = "disabled")
        elif boton == "ejecutar":
            self.btn_Ejecutar.configure(state="normal")
        elif boton == "reiniciar":
            self.btn_Cargar.configure(state="normal")
            self.btn_Crear.configure(state="disabled")
            self.btn_Ejecutar.configure(state="disabled")
            self.btn_ver_movs.configure(state = "normal")



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
                self.habilitar_boton("crear")  # Habilitar botón de crear archivo DZN
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
        self.habilitar_boton("ejecutar")  # Habilitar botón de ejecutar modelo



    def ejecutar_modelo(self):
        try:
            # Configuración del modelo y solución
            start_time = time.time()

            modelo = Model("Proyecto.mzn")
            solver = Solver.lookup("gecode")
            instance = Instance(solver, modelo)
            instance.add_file("ProyectoGUIFuentes/DatosProyecto.dzn")

            # Resolver el modelo
            result = instance.solve()
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Convertir el resultado en un diccionario
            dividir = str(result).split("\n")
            self.diccionario_resultado = {}

            for linea in dividir:
                if ": " in linea:  # Verificar que la línea contenga el separador ": "
                    clave, valor = linea.split(": ", 1)  # Divide en clave y valor usando ": " como separador
                    # Convertir el valor a su tipo correspondiente si es posible (float, int, lista, etc.)
                    if valor.startswith("[") and valor.endswith("]"):
                        valor = eval(valor)  # Convierte la cadena de lista a lista real (usa con precaución)
                    elif valor.replace('.', '', 1).isdigit():
                        valor = float(valor) if '.' in valor else int(valor)
                    self.diccionario_resultado[clave] = valor


            # Llenar los entrys del output con los valores del diccionario
            self.entry_polarización.configure(state="normal")
            self.entry_polarización.delete(0, END)
            self.entry_polarización.insert(0, self.diccionario_resultado.get("POL", ""))
            self.entry_polarización.configure(state="readonly")

            self.entry_distribucion.configure(state="normal")
            self.entry_distribucion.delete(0, END)
            self.entry_distribucion.insert(0, self.diccionario_resultado.get("Movimientos", ""))
            self.entry_distribucion.configure(state="readonly")

            self.entry_costo_final.configure(state="normal")
            self.entry_costo_final.delete(0, END)
            self.entry_costo_final.insert(0, self.diccionario_resultado.get("Costo", ""))
            self.entry_costo_final.configure(state="readonly")

            self.entry_movs_final.configure(state="normal")
            self.entry_movs_final.delete(0, END)
            self.entry_movs_final.insert(0, self.diccionario_resultado.get("Nueva distribuccion de personas", ""))
            self.entry_movs_final.configure(state="readonly")
            
            # Llenar el textbox de la matriz final
            matriz_movimientos = self.diccionario_resultado.get("Matriz de movimientos", [])
            if isinstance(matriz_movimientos, list):
            # Limpiar el textbox antes de insertar los nuevos datos
                self.textbox_matriz_final.configure(state="normal")  # Habilitar temporalmente para insertar los datos
                self.textbox_matriz_final.delete("1.0", END)
                
                # Convertir la lista en una cadena formateada y agregar al textbox
                matriz_texto = "\n".join(
                    str(matriz_movimientos[i:i + int(self.entry_opiniones.get())]) 
                    for i in range(0, len(matriz_movimientos), int(self.entry_opiniones.get()))
                )
                self.textbox_matriz_final.insert("1.0", matriz_texto)
                
                # Deshabilitar nuevamente para evitar edición
                self.textbox_matriz_final.configure(state="disabled")



            # Mostrar el diccionario en la consola para verificar 
            messagebox.showinfo("Ejecución", "Modelo ejecutado correctamente")
            self.habilitar_boton("reiniciar")  # Reinicia el flujo habilitando solo el botón de cargar archivo

        
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el modelo: {e}")



# Ejecutar la aplicación
if __name__ == "__main__":
    root = ctk.CTk()
    app = InterfazMPL(root)
    root.mainloop()