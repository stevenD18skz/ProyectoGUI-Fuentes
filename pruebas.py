from conexion import *
import time


def crear_archivo_dzn(nombre_archivo):
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
    with open("DatosProyecto.dzn", "w") as archivo_dzn:
        archivo_dzn.write(contenido_dzn)



for i in range(1, 2):
    crear_archivo_dzn(f'C:/Users/braya/Desktop/PROYECOTS/ProyectoGUI-Fuentes/batería/MinPol{i}.mpl')
    print("resolviendo.....\n\n")
    
    start_time = time.time()


    # Ejemplo de uso
    solver = MiniZincSolver("modelo1.mzn", "DatosProyecto.dzn")
    solver.load_model()
    solver.configure_solver()
    result = solver.solve()
    print(solver.get_solution())


    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido: {elapsed_time} segundos")





#mover una persona de la opinion(i) a la opinio(j) es |i-j|







