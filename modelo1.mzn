%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR EL PROBLEMA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

int: n = 6; % cantidad de personas

int: m = 3;  % Cantidad de opiniones

array[1..m] of int: opiniones_iniciales = [1, 3, 2];  % Distribución de personas en cada opinión inicial

array[1..m] of float: valores_opiniones = [3, 6, 1];            % lista de float: lista de m valores correspondiente al valor de cada posible opinión 


array[1..m, 1..m] of int: costos_desplazamiento = 
    array2d(1..m, 1..m, 
    [ 0, 2, 4,
      1, 0, 3,
      3, 2, 0]);
      
int: ct = 20;                                          % float: costo total máximo permitido

int: maxMovs = 18;                                       % entero: máximo de movimientos


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR LA MATRIZ DE MOVIMIENTOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Definir matriz de variables para representar el número de personas movidas de una opinión a cada otra
array[1..m, 1..m] of var 0..max(opiniones_iniciales): movimientos;

% Restricciones para cada fila i de la matriz de movimientos
constraint
    forall(i in 1..m) (
        sum(j in 1..m) (movimientos[i, j]) <= opiniones_iniciales[i]   % La suma de movimientos en cada fila debe igualar o ser menor a la cantidad de personas en la opinión i
    );

% Restricción para el costo total de movimientos en toda la matriz
constraint
    sum(i in 1..m, j in 1..m) (movimientos[i, j] * costos_desplazamiento[i, j]) <= ct /\  % Limitar el costo total de movimientos en toda la matriz
    sum(i in 1..m, j in 1..m) (movimientos[i, j]) <= maxMovs;  % Limitar la suma total de la matriz de movimientos
    
    
    
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR OONTRUCCION EN BASE DE MOVIMIENTOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Suma de cada fila y cada columna de la matriz movimientos
array[1..m] of var int: suma_filas = [sum(j in 1..m)(movimientos[i, j]) | i in 1..m];
array[1..m] of var int: suma_columnas = [sum(i in 1..m)(movimientos[i, j]) | j in 1..m];


% Creación del nuevo array aplicando la fórmula
array[1..m] of var int: opiniones_nuevas = [opiniones_iniciales[i] - suma_filas[i] + suma_columnas[i] | i in 1..m];




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CALCULAR LA POLARIZACION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% =MEDIANA=========================================================================================================
% SACAR DISTRIBUCION


  


%ORDENAR



  
  

% indice del medio
int: indice_medio = ceil(n / 2);

% Obtiene el valor en el índice calculado
var float: mediana_valores_opiniones2 = resultado[indice_medio];
% =============================================================================================================
  
  
  
% Obtiene el valor en el índice calculado
var float: mediana_valores_opiniones = 0;


% Calculamos el valor de Pol(p, v) según la fórmula
var float: Pol = sum(i in 1..m)(opiniones_nuevas[i] * abs(valores_opiniones[i] - mediana_valores_opiniones));
 

% solve maximize Pol;


output [
    "Matriz de movimientos:\n",
    show(opiniones_iniciales), "\n",
    show(movimientos), "\n",
    show(suma_filas), "\n",
    show(suma_columnas), "\n===\n",
    show(opiniones_nuevas), "\n",
    show(valores_opiniones), "\n",
    show(resultado), "\n",
    show(Pol), "\n"
];
















