int: n;                                             % entero: cantidad n de personas
int: m;                                             % entero: numero m de posibles opiniones

array[1..m] of int: opiniones_iniciales;            % lista de enteros: lista de m valores según la opinión inicial de cada persona (la suma da $n$)

array[1..m] of float: valores_opiniones;            % lista de float: lista de m valores correspondiente al valor de cada posible opinión 

array[1..m] of float: costos_extras;                % # float positivo: lista de m valores correspondientes a los costos extras de las opiniones (cuando ninguna persona compartía dicha opinión)

array[1..m, 1..m] of int: costos_desplazamiento;    % listas de enteros: m listas de m valores correspondientes a los costos de desplazarse de una opinión $i$ a cada una de las $m$ opiniones

float: ct;                                          % float: costo total máximo permitido
int: maxMovs;                                       % entero: máximo de movimientos

float: mediana = 1;