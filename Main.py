# Importando modulos.
from ListasDoblementeEnlazadas import *
from Jugador import *
from Tablero import *

# /////////////////////////////////////////////////////////

board = Tablero(3)
jugador_x, jugador_y = board.asignar_jugadores()
board.mostrar_tablero()
#board.mover_jugador("arriba",jugador_x)
board.colocar_bloqueo(1,1)
board.colocar_bloqueo(2,2)
board.colocar_bloqueo(1,3)
valor = board.verificar_rutas(jugador_x.nodo_actual)
print(valor)
board.mostrar_tablero()