# Importando modulos.
from ListasDoblementeEnlazadas import *
from Jugador import *
from Tablero import *

# /////////////////////////////////////////////////////////

board = Tablero(3)
jugador_x, jugador_y = board.asignar_jugadores()
board.mostrar_tablero()
#board.mover_jugador("arriba",jugador_x)
#board.colocar_bloqueo(jugador_x, 1,3)
board.colocar_bloqueo(jugador_x, 2,1)
board.colocar_bloqueo(jugador_x, 2,1)
board.mostrar_tablero()