int: n;                                             % entero: cantidad n de personas
int: m;                                             % entero: numero m de posibles opiniones

array[1..m] of int: opiniones_iniciales;            % lista de enteros: lista de m valores según la opinión inicial de cada persona (la suma da $n$)

array[1..m] of float: valores_opiniones;            % lista de float: lista de m valores correspondiente al valor de cada posible opinión 

array[1..m] of float: costos_extras;                % # float positivo: lista de m valores correspondientes a los costos extras de las opiniones (cuando ninguna persona compartía dicha opinión)

array[1..m, 1..m] of int: costos_desplazamiento;    % listas de enteros: m listas de m valores correspondientes a los costos de desplazarse de una opinión $i$ a cada una de las $m$ opiniones

float: ct;                                          % float: costo total máximo permitido
int: maxMovs;                                       % entero: máximo de movimientos


float: mediana = 1;

















%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
int: n = 22; % cantidad de personas

int: m = 5;  % Cantidad de opiniones

array[1..m] of int: opiniones_iniciales = [12, 4, 1, 4, 1];  % Distribución de personas en cada opinión inicial

array[1..m] of float: valores_opiniones = [0, 0.35, 0.5, 0.75, 1];            % lista de float: lista de m valores correspondiente al valor de cada posible opinión 

array[1..m, 1..m] of int: costos_desplazamiento = 
    array2d(1..m, 1..m, 
    [ 0, 2, 4, 5, 7,
      1, 0, 3, 4, 6,
      3, 2, 0, 2, 4,
      4, 2, 1, 0, 2,
      8, 5, 3, 2, 0 ]);
      
float: ct = 20;                                          % float: costo total máximo permitido

int: maxMovs = 18;                                       % entero: máximo de movimientos


% Definir matriz de variables para representar el número de personas movidas de una opinión a cada otra
array[1..m, 1..m] of var 0..max(opiniones_iniciales): movimientos;

% Restricciones para cada fila i de la matriz de movimientos
constraint
    forall(i in 1..m) (
        sum(j in 1..m) (movimientos[i, j]) <= opiniones_iniciales[i]  % La suma de movimientos en cada fila debe igualar la cantidad de personas en la opinión i
    );

% Restricción para el costo total de movimientos en toda la matriz
constraint
    sum(i in 1..m, j in 1..m) (movimientos[i, j] * costos_desplazamiento[i, j]) <= ct /\  % Limitar el costo total de movimientos en toda la matriz
    sum(i in 1..m, j in 1..m) (movimientos[i, j]) <= maxMovs;  % Limitar la suma total de la matriz de movimientos a ser menor o igual que 30


solve satisfy;

output [
    "Matriz de movimientos:\n",
    show(movimientos), "\n"
];





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

int: m = 5;  % Cantidad de opiniones

array[1..3] of int: opiniones_iniciales = [1, 3, 2];  % Distribución de personas en cada opinión inicial
array[1..3] of float: valores_opiniones = [3.0, 6.0, 1.0];  % Lista de valores correspondientes a cada posible opinión

array[1..sum(opiniones_iniciales)] of float: opiniones_expandidas = 
    array1d(1..sum(opiniones_iniciales),
            [valores_opiniones[i] | i in 1..3, j in 1..opiniones_iniciales[i]]
    );

array[1..sum(opiniones_iniciales)] of float: opiniones_ordenadas = 
    sort(opiniones_expandidas);

% Para verificar el resultado
output ["Opiniones expandidas: \(opiniones_expandidas)\n"];
output ["Opiniones ordenadas: \(opiniones_ordenadas)"];
