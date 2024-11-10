%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR EL PROBLEMA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
int: n = 14; % cantidad de personas

int: m = 3;  % Cantidad de opiniones

array[1..m] of int: opiniones_iniciales = [12, 1, 1];  % Distribución de personas en cada opinión inicial

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
    sum(i in 1..m, j in 1..m) (movimientos[i, j] * abs(i - j)) <= maxMovs;  % Limitar la suma total de la matriz de movimientos
    


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR OONTRUCCION EN BASE DE MOVIMIENTOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Suma de cada fila y cada columna de la matriz movimientos
array[1..m] of var int: suma_filas = [sum(j in 1..m)(movimientos[i, j]) | i in 1..m];
array[1..m] of var int: suma_columnas = [sum(i in 1..m)(movimientos[i, j]) | j in 1..m];


% Creación del nuevo array aplicando la fórmula
array[1..m] of var int: opiniones_nuevas = [opiniones_iniciales[i] - suma_filas[i] + suma_columnas[i] | i in 1..m];



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CALCULAR LA POLARIZACION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% =MEDIANA=========================================================================================================
% SACAR DISTRIBUCION
array[1..n] of var float: expandir;


% SACAR DISTRIBUCION
constraint
  forall(i in 1..m, j in 1..opiniones_nuevas[i]) (
    expandir[sum(opiniones_nuevas[1..i-1]) + j] = valores_opiniones[i]
  );


array[1..m] of float: valores_opiniones_ordenados = sort(valores_opiniones);

int: mitad = n div 2 + 1;
array[1..m] of var int: cuenta_menores = [sum(i in 1..n) (if expandir[i] <= valores_opiniones_ordenados[j] then 1 else 0 endif) | j in 1..m]; 


var 1..m: indice_median;

constraint
  % Encuentra el primer índice donde cuenta_menores[j] >= mitad
  exists(j in 1..m) (
    cuenta_menores[j] >= mitad /\ indice_median = j /\
    forall(k in 1..j-1) (cuenta_menores[k] < mitad)
  );

var float: median = valores_opiniones_ordenados[indice_median];

% Definir la mediana 
var float: mediana = 0;


% =============================================================================================================



% Calculamos el valor de Pol(p, v) según la fórmula
var float: Pol = sum(i in 1..m) (opiniones_nuevas[i] * abs(valores_opiniones[i] - mediana));
 

solve minimize Pol;


output [
    show(opiniones_iniciales), "\n",
    show(movimientos), "\n===\n",
    show(opiniones_nuevas), "\n",
    show(valores_opiniones), "\n",
    "costo: ", show(sum(i in 1..m, j in 1..m) (movimientos[i, j] * costos_desplazamiento[i, j])), "\n",
    "movimientos: ", show(sum(i in 1..m, j in 1..m) (movimientos[i, j] * abs(i - j))), "\n",
    "POL", show(Pol), "\n\n\n",
    show(expandir), "\n",
    show(valores_opiniones_ordenados), "\n",
    show(cuenta_menores), "\n",
    show(indice_median), "\n",
    "MEDIANA HP ", show(median), "\n"
];



