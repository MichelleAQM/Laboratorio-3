from Clases import *

def menu_juego():
    print("............| Pelea contra el Brainrot |............")

    jugador = Personaje()
    jugador.agregar_habilidades(habilidades("Golpe fuertesini", -15))
    jugador.agregar_habilidades(habilidades("Congelar", -8))
    jugador.agregar_habilidades(habilidades("Golpe con espada arcoiris", -25))
    jugador.agregar_habilidades(habilidades("Centinela", -10))

    enemigoFinal = enemigosBrainrots()
    enemigoFinal.agregar_habilidades(habilidades("Golpe fuertesini", -15))
    enemigoFinal.agregar_habilidades(habilidades("Congelar", -8))
    enemigoFinal.agregar_habilidades(habilidades("Golpe con espada arcoiris", -25))
    enemigoFinal.agregar_habilidades(habilidades("Centinela", -10))

    while True:
        print("MENÚ DEL JUEGO")
        print("1. Ver estadísticas del jugador")
        print("2. Asignar equipo")
        print("3. Ver estadísticas del enemigo")
        print("4. Iniciar batalla")
        print("5. Salir")
        opcion = int(put("Seleccione una opción: "))
        if opcion == 1:
            print("Estadísticas del Jugador")
            print("Nombre:", jugador.getNombre())
            print("Salud:", jugador.getSalud())
            print("Fuerza:", jugador.getfuerza())
            if jugador.equipo:
                print("Equipo:", jugador.equipo.nombre)
                print("Bonificación de fuerza:", jugador.equipo.bonificacion + 10)
            else:
                print("Equipo: Ninguno")

            if jugador.habilidades:
                print("Habilidades:")
                for h in jugador.habilidades:
                    print(" -", h.nombre, "(Daño:", h.daño, ")")
            else:
                print("Habilidades: Ninguna")
        elif opcion == 2:
            eq = input("Ingrese el nombre del equipo: ")
            bonif = int(input("Ingrese la bonificación base del equipo: "))
            nuevo_equipo = equipo(eq, bonif)
            jugador.asignar_equipo(nuevo_equipo)
        elif opcion == "3":
            print("Estadísticas del Enemigo")
            print("Nombre:", enemigoFinal.nombreEnemigo)
            print("Salud:", enemigoFinal.salud)
            print("Fuerza:", enemigoFinal.fuerza)
            if enemigoFinal.habilidades:
                print("Habilidades:")
                for h in enemigoFinal.habilidades:
                    print(" -", h.nombre, "(Daño:", h.daño, ")")
            else:
                print("Habilidades: Ninguna")
        elif opcion == "4":
            batalla = Batalla(jugador, enemigoFinal)
            batalla.inicia()
        elif opcion == "5":
            print("Saliendo del juego...")
            break
        else:
            print("Opción inválida, intente de nuevo.")