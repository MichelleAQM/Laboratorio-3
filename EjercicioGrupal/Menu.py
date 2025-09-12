from Clases import *
def menu_juego():
    print("............| Pelea contra el Brainrot |............")
    jugador = Personaje("", 120, 10)
    jugador.asignar_equipo(equipo("", 5))
    jugador.agregar_habilidades(habilidades("", 10))
    jugador.agregar_habilidades(habilidades("", 15))
    jugador.agregar_habilidades(habilidades("", 5))

    enemigoFinal = enemigosBrainrots("", 100, 12)
    enemigoFinal.agregar_habilidades(habilidades("", 8))
    enemigoFinal.agregar_habilidades(habilidades("", 12))
    enemigoFinal.agregar_habilidades(habilidades("", 10))
    Batalla(jugador,enemigoFinal)
