from estudiante import Estudiante
def verMenu():
    print("MENU MATRICULAS")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Matricularse")
    print("4. Pagar pensión")
    print("5. Salir")
def main():
    est=Estudiante()
    while True:
        verMenu()
        opcion=int(input("Selecciones una opción: "))
        if opcion==1:
            est.ingresarDatos()
        elif opcion==2:
            est.imprimirDatos()
        elif opcion==3:
            est.matricular()
        elif opcion==4:
            est.pagarPension()
        elif opcion==5:
            print("Saliendo")
            break
        else:
            print("Opción inválida")
if __name__=="__main__":
    main()

