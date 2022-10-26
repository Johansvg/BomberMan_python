# BomberMan_python
Game inspired by the classic game BomberMan.

THE BOMBERMAN GAME (EL JUEGO DE BOMBERMAN)

Bomberman (el hombre bomba) vive en una cuadrícula rectangular conformada por R filas
y C columnas. Cada celda de la cuadrícula contiene ya sea una bomba o nada en absoluto.
Cada bomba puede ser plantada en cualquier celda de la cuadrícula, pero, una vez
plantada, esta será detonada exactamente 3 segundos después. Una vez que una bomba
es detonada, ésta es destruida – junto con cualquier cosa que haya en sus 4 celdas
vecinas. Esto significa que si una bomba detona en la celda (i, j), las celdas (i+1, j), (i-1, j),
(i, j+1) y (i, j-1) son destruidas o limpiadas (Note que las celdas en el borde de la cuadrícula
tienen menos de 4 celdas vecinas). Si hay una bomba en una celda vecina, la bomba
vecina es destruida sin detonar (es decir, no se produce ninguna reacción).
Bomberman es inmune a las bombas, entonces él puede moverse libremente a través de
la cuadrícula. Esto es lo que hace:
1. Inicialmente, Bomberman arbitrariamente planta bombas en algunas de las celdas.
2. Después de un segundo, Bomberman no hace nada
3. Después de un segundo más, Bomberman planta bombas en todas las celdas sin
bombas, llenando así toda la cuadrícula con bombas. Esto garantiza que las
bombas no detonan en este segundo.
4. Después de un segundo más, las bombas plantadas exactamente 3 segundos antes
detonan. Aquí, Bomberman retrocede y observa.
5. Bomberman repite los pasos 3 y 4 indefinidamente.
Note que durante cada segundo Bomberman planta bombas, las bombas son plantadas
simultáneamente (es decir, exactamente el mismo momento), y cualquier bomba
plantada en el mismo tiempo es detonadas al mismo tiempo.
Dando la configuración inicial de la cuadrícula con las ubicaciones del primer lote de
bombas colocadas por Bomberman, determina el estado de la cuadrícula después de N
segundos.

2

Formato de entrada
La primera línea contiene tres enteros separados por espacios denotando los valores
respectivos de R, C y N.
Cada línea i de la R siguientes líneas describe las filas i del estado inicial de la cuadrícula
como un solo String de C caracteres; el carácter “.” denota una celda vacía, y el carácter
“O” (ASCII 79) denota una bomba.
Restricciones
 1 &lt;= R, C &lt;= 200
 1 &lt;= N &lt;= 10 9

Subtarea
 1 &lt;= N &lt;= 200 para el 40% del puntaje máximo.

Formato de salida
Imprimir el estado final de la cuadrícula. Esto significa que las R líneas donde cada línea
contiene C caracteres, y cada carácter ya sea un “.” o un “O” (ASCII 79). Esta cuadrícula
debe representar el estado de la cuadrícula después de N segundos.
