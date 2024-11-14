## Descripción del Proyecto
Este proyecto implementa un modelo de optimización y una interfaz gráfica para resolver un problema específico. La estructura de archivos y directorios es la siguiente:

# Estructura de Archivos
Informe ADA II - Proyecto II.pdf: Documento de informe que detalla la metodología, los resultados y el análisis del proyecto, acorde a la Sección 3.2. Incluye un link al video explicatorio sobre el funcionamiento del proyecto.

# Proyecto.mzn: 
Archivo que contiene la implementación del modelo en MiniZinc. Este archivo define las restricciones y el modelo matemático para resolver el problema.

#  proyecto2-2024-II.pdf: 
Documento adicional de referencia que incluye los detalles específicos del proyecto y sus requisitos.

# README.md: 
Este archivo, que proporciona una descripción de la estructura del proyecto y las instrucciones de ejecución.

## Directorios
# DatosProyecto: 
Contiene los datos de prueba con los que fue verificado el modelo. Estos datos se utilizan como entrada para el archivo de modelo Proyecto.mzn.

# MisInstancias: 
Carpeta que incluye cinco instancias generadas por el equipo de trabajo para desafiar otros proyectos que aborden el mismo problema. Cada instancia representa un conjunto diferente de datos de entrada.

# ProyectoGUIFuentes: 
Contiene todos los archivos fuente de la implementación de la interfaz gráfica en Python. Este directorio incluye:

# conexion.py: 
Script que gestiona la conexión entre Python y MiniZinc. Permite enviar los datos y ejecutar el modelo desde la interfaz gráfica.

# DatosProyecto.dzn: 
Archivo de datos en formato .dzn utilizado por MiniZinc para recibir los parámetros necesarios en el modelo.

# gui.py: 
Archivo que contiene el código para la construcción de la interfaz gráfica de usuario.

# main.py: 
Archivo principal que inicia la aplicación. Ejecutando este archivo, se lanza la interfaz gráfica y se establece la conexión con MiniZinc para resolver el problema.


## Instrucciones de Ejecución
1. Asegúrese de tener Python y MiniZinc instalados en su sistema.

2. Ejecute el archivo main.py ubicado en el directorio ProyectoGUIFuentes. Esto iniciará la interfaz gráfica y cargará el modelo de optimización.

python ProyectoGUIFuentes/main.py


3. En la interfaz gráfica, cargue los datos necesarios (disponibles en el directorio DatosProyecto) y ejecute el modelo. Los resultados se mostrarán en la interfaz.