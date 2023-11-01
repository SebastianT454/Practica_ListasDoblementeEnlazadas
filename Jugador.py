# Importando modulos.
from ListasDoblementeEnlazadas import *
from Tablero import *

# /////////////////////////////////////////////////////////

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nodo_actual = None
        self.posicion_emulada = []

    def colocar_bloqueo(self, tablero,fila,columna):
        nodo_deseado = Tablero.recorrer_tablero(tablero,fila,columna)
        nodo_deseado.value = "#"