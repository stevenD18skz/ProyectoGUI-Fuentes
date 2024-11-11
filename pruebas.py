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

validas = [1,4,6,7,8,10,14,15,16,17,19,21,22,23,24,25,28,29,]



valores_malos = [
0.09,
0.000,
-1,
0.000,
1.751,
0.005,
3.085,
5.675,
5.373,
9.686,
15.596,
5.865,
28.909,
-1,
10.313,
18.786,
15.699,
22.216,
20.04,
23.824,
31.848,
-1,
7.876,
-1,
28.034,
30.943,
25.021,
18.903,
36.25,
0
]



valores_buenos = [
0.09,
0.000,
0.000,
0.000,
0.482,
0.003,
3.085,
4.323,
5.373,
9.686,
10.349,
3.721,
12.417,
6.549,
10.313,
18.786,
14.171,
17.897,
19.603,
23.566,
24.175,
31.135,
3.822,
29.902,
24.775,
30.748,
25.021,
14.683,
29.999,
0




]


for i in range(5, 6):
    crear_archivo_dzn(f'C:/Users/braya/Desktop/PROYECOTS/ProyectoGUI-Fuentes/batería/MinPol{i}.mpl')
    print("\n\nresolviendo......")
    
    start_time = time.time()


    # Ejemplo de uso
    solver = MiniZincSolver("modelo1.mzn", "DatosProyecto.dzn")
    solver.load_model()
    solver.configure_solver()
    result = solver.solve()
    print(f" {"✅✅✅" if i in validas else "⭕⭕⭕"} {i} ===> {solver.get_solution()}")
    print(f"            mala {valores_malos[i-1]} ==== buenos {valores_buenos[i-1]}")


    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido: {elapsed_time:2f} segundos")







