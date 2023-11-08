# Importando modulos.
from ListasDoblementeEnlazadas import *
from Jugador import *
from Tablero import *

# /////////////////////////////////////////////////////////

def main():
    jugador_x = None
    jugador_y = None

    while True:
        print("Menú:")
        print("1. Iniciar partida")
        print("2. Parar")
        opcion = input("Elija una opción: ")

        if opcion == '1':
            size = int(input("Ingrese el tamaño del tablero: "))
            tablero = Tablero(size)
            jugador_x, jugador_y = tablero.asignar_jugadores()
            print("Tablero creado y jugadores ubicados.")
            print("-------------------------------------")

            jugador_actual = jugador_x  # Empieza Jugador X
            while True:
                tablero.mostrar_tablero()
                print(f"Turno de {jugador_actual.nombre}")
                print("1. Mover")
                print("2. Colocar bloqueo")
                accion = input("Elija una acción: ")

                if accion == '1':
                    print("Movimientos posibles:")
                    print("1. Izquierda")
                    print("2. Derecha")
                    print("3. Arriba")
                    print("4. Abajo")
                    direccion = input("Elija una dirección: ")
                    if direccion == '1':
                        jugador_actual.mover(tablero, 'izquierda')
                    elif direccion == '2':
                        jugador_actual.mover(tablero, 'derecha')
                    elif direccion == '3':
                        jugador_actual.mover(tablero, 'arriba')
                    elif direccion == '4':
                        jugador_actual.mover(tablero, 'abajo')

                elif accion == '2':
                    fila = int(input("Ingrese la fila para colocar el bloqueo: "))
                    columna = int(input("Ingrese la columna para colocar el bloqueo: "))

                    jugador_actual.colocar_bloqueo(tablero, fila, columna)

                if jugador_y.fila_actual == 1:
                    print("¡Jugador Y ha ganado la partida!")
                    tablero.mostrar_tablero()
                    break
                if jugador_x.fila_actual == tablero.tamano:
                    print("¡Jugador X ha ganado la partida!")
                    tablero.mostrar_tablero()
                    break

                # Cambiar al siguiente jugador
                if jugador_actual == jugador_x:
                    jugador_actual = jugador_y
                else:
                    jugador_actual = jugador_x

        elif opcion == '2':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()