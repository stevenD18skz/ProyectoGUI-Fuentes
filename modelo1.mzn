%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INICIAR EL PROBLEMA %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
int: n; % cantidad de personas

int: m;  % Cantidad de opiniones

array[1..m] of int: opiniones_iniciales;  % Distribución de personas en cada opinión inicial

array[1..m] of float: valores_opiniones;            % lista de float: lista de m valores correspondiente al valor de cada posible opinión 

array[1..m] of float: costos_extras;

array[1..m, 1..m] of int: costos_desplazamiento;
      
int: ct;                                          % float: costo total máximo permitido

int: maxMovs;                                       % entero: máximo de movimientos


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
array[1..n] of var float: expandir;

% Variable auxiliar para llevar el índice acumulado de la opinión
array[1..m] of var int: acumulado;  % Para cada i, acumulado[i] será el índice de la primera persona de ese grupo

% Restricción de asignación de valores
constraint
  acumulado[1] = 1 /\  % El primer grupo comienza en la persona 1
  forall(i in 2..m) (
    acumulado[i] = acumulado[i-1] + opiniones_nuevas[i-1]  % Se calcula el inicio de la siguiente opinión
  ) /\  
  forall(i in 1..m, j in 1..opiniones_nuevas[i]) (
    expandir[acumulado[i] + j - 1] = valores_opiniones[i]
  );



int: mitad = n div 2 + 1;

var 1..m: k = 1;

var int: cuenta_menores_5 = sum(i in 1..n) (if expandir[i] <= valores_opiniones[k] then 1 else 0 endif);
var bool: v = cuenta_menores_5 >= mitad; 
var float: mediana = if v then valores_opiniones[k] else 0 endif;

constraint v == true;



var float: mediana_valores_opiniones = 0; %aqui toca calcular la mediana con los valores de lo que da la matriz "opiniones_nuevas"
% =============================================================================================================



% Calculamos el valor de Pol(p, v) según la fórmula
var float: Pol = sum(i in 1..m)(opiniones_nuevas[i] * abs(valores_opiniones[i] - mediana));
 

solve minimize Pol;


output [
    show(opiniones_iniciales), "\n",
    show(movimientos), "\n===\n",
    show(opiniones_nuevas), "\n",
    show(valores_opiniones), "\n",
    "costo: ", show(sum(i in 1..m, j in 1..m) (movimientos[i, j] * costos_desplazamiento[i, j])), "\n",
    "movimientos: ", show(sum(i in 1..m, j in 1..m) (movimientos[i, j])), "\n",
    show(Pol), "\n\n\n",
    show(expandir), "\n",
    show(mediana), "\n"
];