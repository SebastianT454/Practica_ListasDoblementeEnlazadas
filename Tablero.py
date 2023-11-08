# Importando modulos.
from ListasDoblementeEnlazadas import *
import Jugador

import random

# /////////////////////////////////////////////////////////

class Tablero:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tablero = []
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(self.tamano):
            self.tablero.append(ListasDoblementeEnlazadas())
            for _ in range(self.tamano):
                self.tablero[fila].append("-")

        for i in range(len(self.tablero) - 1):
            head1 = self.tablero[i].head
            head2 = self.tablero[i + 1].head

            while(head1 and head2):
                head1.abajo = head2
                head2.arriba = head1

                head1 = head1.derecha
                head2 = head2.derecha


    def mostrar_tablero(self):
        head_tablero = self.tablero[0].head
        abajo_tablero = self.tablero[0].head.abajo

        lista_fila = []

        while(head_tablero):
            lista_fila.append(head_tablero.value)
            head_tablero = head_tablero.derecha

            if not head_tablero: 
                print(lista_fila)
                lista_fila = []
                head_tablero = abajo_tablero
                if head_tablero:
                    abajo_tablero = head_tablero.abajo

        print("---------")

    def recorrer_tablero(self,fila_requerida,columna_requerida):
        if (fila_requerida - 1 < self.tamano and columna_requerida - 1 < self.tamano):

            head_tablero = self.tablero[0].head
            abajo_tablero = self.tablero[0].head.abajo

            fila_actual = 0
            columna_actual = 0

            while(head_tablero):
                if ((fila_actual == fila_requerida - 1) and (columna_actual == columna_requerida - 1)):
                    return head_tablero

                columna_actual += 1

                head_tablero = head_tablero.derecha

                if not head_tablero: 
                    fila_actual += 1
                    columna_actual = 0

                    head_tablero = abajo_tablero
                    if head_tablero:
                        abajo_tablero = head_tablero.abajo
        else:
            print("La fila o la columna están fuera de los limites de la matriz.. Grave!")

    def verificar_movimiento(self,direccion,jugador):
        nodo_seleccionado = None
        jugador_puede_moverse = False

        if(direccion == "izquierda"):
            nodo_izquierda = jugador.nodo_actual.izquierda
            if(nodo_izquierda and nodo_izquierda.value == "-"):
                nodo_seleccionado = nodo_izquierda
                jugador_puede_moverse = True

        elif(direccion == "derecha"):
            nodo_derecha = jugador.nodo_actual.derecha
            if(nodo_derecha and nodo_derecha.value == "-"):
                nodo_seleccionado = nodo_derecha
                jugador_puede_moverse = True

        elif(direccion == "arriba"):
            nodo_arriba = jugador.nodo_actual.arriba
            if(nodo_arriba and nodo_arriba.value == "-"):
                nodo_seleccionado = nodo_arriba
                jugador.fila_actual -= 1
                jugador_puede_moverse = True

        elif(direccion == "abajo"):
            nodo_abajo = jugador.nodo_actual.abajo
            if(nodo_abajo and nodo_abajo.value == "-"):
                nodo_seleccionado = nodo_abajo
                jugador.fila_actual += 1
                jugador_puede_moverse = True

        else:
            print(f"Direccion incorrecta: {direccion}")

        return jugador_puede_moverse,nodo_seleccionado
    
    def mover_jugador(self,direccion,jugador):
        jugador_puede_moverse,nodo_seleccionado = self.verificar_movimiento(direccion, jugador)

        if jugador_puede_moverse:
            jugador.nodo_actual.value = "-"

            jugador.nodo_actual = nodo_seleccionado
            jugador.nodo_actual.value = jugador.nombre
            return True
        else:
            print("El jugador no puede moverse!")
            return False

    def asignar_jugadores(self):
        jugador_x = Jugador.Jugador("x")
        jugador_y = Jugador.Jugador("y")

        fila_jugador_x = 1
        columna_jugador_x = 2 #random.randint(1, self.tamano)

        jugador_x.nodo_actual = self.recorrer_tablero(fila_jugador_x,columna_jugador_x)

        #########################################################################

        fila_jugador_y = self.tamano
        columna_jugador_y = random.randint(1, self.tamano)

        jugador_y.nodo_actual = self.recorrer_tablero(fila_jugador_y,columna_jugador_y)

        #########################################################################

        jugador_x.nodo_actual.value = "x"
        jugador_y.nodo_actual.value = "y"

        jugador_x.fila_actual = fila_jugador_x
        jugador_y.fila_actual = fila_jugador_y

        return jugador_x, jugador_y

    def colocar_bloqueo(self, jugador, fila,columna):
        nodo_deseado = self.recorrer_tablero(fila, columna)

        if nodo_deseado.value == "-":
            nodo_deseado.value = "#"

            nodos_disponibles = self.verificar_casillas_disponibles(jugador.nombre)
            resultado_ruta = self.verificar_ruta(nodos_disponibles, jugador.nodo_actual)
            print(resultado_ruta)
            
            if (resultado_ruta is not None):
                #nodo_deseado.value = "#"
                print("Bloqueo colocado con éxito.")
            else:
                nodo_deseado.value = "-"
                print("No se puede colocar el bloqueo.")
            
        else:
            print("Ya existe algo en esta posición.")
        
    def verificar_ruta(self, posicion_deseada, nodo, visitados=[]):
         #None
        if nodo is None:
            return
        #visitado
        if nodo in visitados:
            return
        #bloqueo
        if nodo.value == "#":
            return
       
        if nodo in posicion_deseada:
            return True
        else:
            visitados.append(nodo)
            arriba = self.verificar_ruta(posicion_deseada, nodo.arriba, visitados)
            derecha = self.verificar_ruta(posicion_deseada, nodo.derecha, visitados)
            abajo = self.verificar_ruta(posicion_deseada, nodo.abajo, visitados)
            izquierda = self.verificar_ruta(posicion_deseada, nodo.izquierda, visitados)

            if(not arriba and not derecha and not abajo and not izquierda):
                del visitados[0]
                self.verificar_ruta(posicion_deseada, nodo, visitados)
            else:
                return arriba or derecha or abajo or izquierda
        
    def verificar_casillas_disponibles(self, jugador, nodos_disponibles = []):
        if jugador == "x":
            fila_deseada = self.tamano
            for i in range(1, self.tamano + 1):
                nodo = self.recorrer_tablero(fila_deseada, i)
                if (nodo.value != "#" and nodo.value != "y"):
                    nodos_disponibles.append(nodo)
                
        if jugador == "y":
            fila_deseada = 1
            for i in range(1, self.tamano + 1):
                nodo = self.recorrer_tablero(fila_deseada, i)
                if (nodo.value != "#" and nodo.value != "x"):
                    nodos_disponibles.append(nodo)
        
        return nodos_disponibles
                