from tkinter import *
from tkinter import filedialog
import customtkinter as ctk

def cargar_archivo():
    # Abre un cuadro de diálogo para seleccionar el archivo .mpl
    file_path = filedialog.askopenfilename(filetypes=[("MPL files", "*.mpl")])
    if not file_path:
        return  # Si no se selecciona un archivo, termina la función

    # Lee el archivo y llena los campos correspondientes
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Asigna cada línea a su campo correspondiente
            entry_personas.delete(0, END)
            entry_personas.insert(0, lines[0].strip())

            entry_opiniones.delete(0, END)
            entry_opiniones.insert(0, lines[1].strip())

            entry_opinion_personas.delete(0, END)
            entry_opinion_personas.insert(0, lines[2].strip())

            entry_valor_opinion.delete(0, END)
            entry_valor_opinion.insert(0, lines[3].strip())

            entry_costo_opinion.delete(0, END)
            entry_costo_opinion.insert(0, lines[4].strip())

            # Cargar la "Matriz de costo" en el Textbox
            textbox_costo_desplazamiento.delete("1.0", END)
            for i in range(5, 5 + int(lines[1].strip())):  # m filas de la matriz
                textbox_costo_desplazamiento.insert(END, lines[i])

            entry_costo_maximo.delete(0, END)
            entry_costo_maximo.insert(0, lines[5 + int(lines[1].strip())].strip())

            entry_max_movs.delete(0, END)
            entry_max_movs.insert(0, lines[6 + int(lines[1].strip())].strip())
            
            # Indica que se ha cargado exitosamente
            textbox_output.delete("1.0", END)
            textbox_output.insert("1.0", "Archivo cargado exitosamente.")
    except Exception as e:
        textbox_output.delete("1.0", END)
        textbox_output.insert("1.0", f"Error al cargar el archivo: {e}")

# Configuración de la interfaz
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('Prueba customtkinter')
root.geometry('600x500')

# Etiquetas y campos de entrada
label_personas = ctk.CTkLabel(master=root, text="Numero de personas")
label_personas.place(x=50, y=20)
entry_personas = ctk.CTkEntry(master=root, width=100)
entry_personas.place(x=180, y=20)

label_opiniones = ctk.CTkLabel(master=root, text="Posibles opiniones")
label_opiniones.place(x=50, y=60)
entry_opiniones = ctk.CTkEntry(master=root, width=100)
entry_opiniones.place(x=180, y=60)

label_opinion_personas = ctk.CTkLabel(master=root, text="Opiniones por persona")
label_opinion_personas.place(x=50, y=100)
entry_opinion_personas = ctk.CTkEntry(master=root, width=100)
entry_opinion_personas.place(x=180, y=100)

label_valor_opinion = ctk.CTkLabel(master=root, text="Valor de opiniones")
label_valor_opinion.place(x=50, y=140)
entry_valor_opinion = ctk.CTkEntry(master=root, width=100)
entry_valor_opinion.place(x=180, y=140)

label_costo_opinion = ctk.CTkLabel(master=root, text="Costos extra")
label_costo_opinion.place(x=50, y=180)
entry_costo_opinion = ctk.CTkEntry(master=root, width=100)
entry_costo_opinion.place(x=180, y=180)

label_costo_desplazamiento = ctk.CTkLabel(master=root, text="Matriz de costo")
label_costo_desplazamiento.place(x=300, y=20)
textbox_costo_desplazamiento = ctk.CTkTextbox(master=root, width=150, height=100)
textbox_costo_desplazamiento.place(x=400, y=20)

label_costo_maximo = ctk.CTkLabel(master=root, text="Costo total permitido")
label_costo_maximo.place(x=300, y=140)
entry_costo_maximo = ctk.CTkEntry(master=root, width=100)
entry_costo_maximo.place(x=450, y=140)

label_max_movs = ctk.CTkLabel(master=root, text="Movimientos permitidos")
label_max_movs.place(x=300, y=180)
entry_max_movs = ctk.CTkEntry(master=root, width=100)
entry_max_movs.place(x=450, y=180)

# Botones
btn_Crear = ctk.CTkButton(root, text="Crear archivo DZN")
btn_Crear.place(x=50, y=250)

btn_Cargar = ctk.CTkButton(root, text="Cargar archivo .mpl", command=cargar_archivo)
btn_Cargar.place(x=225, y=250)

btn_Ejecutar = ctk.CTkButton(root, text="Ejecutar modelo")
btn_Ejecutar.place(x=400, y=250)

# Textbox para salida de mensajes
textbox_output = ctk.CTkTextbox(master=root, width=490, height=150)
textbox_output.place(x=50, y=300)

root.mainloop()
