from estudiante import Estudiant
def verMenu():
    print("MENU MATRICULAS")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Matricularse")
    print("4. Pagar pensión")
    print("6. Verificar si es mayor de edad")
    print("5. Cambiar de institución")
    print("7. Salir")
def main():
    est=Estudiant()
    while True:
        verMenu()
        opcion=int(input("Seleccione una opción: "))
        if opcion==1:
            est.ingresarDatos()
        elif opcion==2:
            est.imprimirDatos()
        elif opcion==3:
            est.matricular()
        elif opcion==4:
            est.pagarPension()
        elif opcion==5:
            est.mayorEdad()
        elif opcion==6:
            est.cambiarInstitución()
        elif opcion==7:
            print("Saliendo")
            break
        else:
            print("Opción inválida")
if __name__=="__main__":
    main()

