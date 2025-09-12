from Clases import *
def menu_juego():
    print("............| Pelea contra el Brainrot |............")
    nombre = input("Ingrese el nombre de su personaje: ")
    jugador = Personaje(nombre, 120, 10)
    enemigoFinal=enemigosBrainrots("Brainrot Supremo",100,12)
    while True:
        print("1. Ver estadísticas del jugador")
        print("2. Asignar equipo")
        print("3. Añadir habilidades")
        print("4. Ver estadísticas del enemigo")
        print("5. Iniciar batalla")
        print("6. Salir")
        opcion=int(input("Seleccione una opción: "))
        if opcion==1:
            print("Estadísticas del jugador")
            print("Nombre: ",jugador.getNombre())
            print("Salud: ", jugador.getSalud())
            print("Fuerza: ", jugador.getfuerza())
            if jugador.equipo:
                print("Equipo:", jugador.equipo.nombre)
                print("Bonificación de fuerza:", jugador.equipo.bonificacion)
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
            bonif = int(input("Ingrese la bonificación de fuerza: "))
            nuevo_equipo = equipo(eq, bonif)
            jugador.asignar_equipo(nuevo_equipo)
        elif opcion == 3:
            hab = input("Ingrese el nombre de la habilidad: ")
            daño = int(input("Ingrese el daño de la habilidad: "))
            jugador.agregar_habilidades(habilidades(hab, daño))
            print("Habilidad añadida con éxito.")
        elif opcion == 4:
            print("\n--- Estadísticas del Enemigo ---")
            print("Nombre:", enemigoFinal.nombreEnemigo)
            print("Salud:", enemigoFinal.salud)
            print("Fuerza:", enemigoFinal.fuerza)
            if enemigoFinal.habilidades:
                print("Habilidades:", [h.nombre for h in enemigoFinal.habilidades])
            else:
                print("Habilidades: Ninguna")
        elif opcion == 5:
            batalla = Batalla(jugador, enemigoFinal)
            batalla.inicia()
        elif opcion == 6:
            print("Saliendo")
            break
        else:
            print("Opción inválida, intente de nuevo.")