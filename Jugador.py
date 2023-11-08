# Importando modulos.
from ListasDoblementeEnlazadas import *
from Tablero import *

# /////////////////////////////////////////////////////////

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nodo_actual = None
        self.fila_actual = None

    def colocar_bloqueo(self, tablero,fila,columna):
        jugador = self
        tablero.colocar_bloqueo(jugador,fila,columna)

    def mover(self, tablero,direccion):
        jugador = self
        tablero.mover_jugador(direccion,jugador)