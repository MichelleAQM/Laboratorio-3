from estudiante import Estudiant
def verMenu():
    print("MENU MATRICULAS")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("3. Matricularse")
    print("4. Pagar pensión")
    print("5. Verificar si es mayor de edad")
    print("6. Cambiar de institución")
    print("7. Calcular promedio")
    print("8. Verificar correo")    
    print("9. Salir")
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
            est.mayorEdad(est.edad)
        elif opcion==6:
            est.cambiarInstitución()
        elif opcion==7:
            est.promedio_notas()
        elif opcion==8:
            est.verificarCorreo()
        elif opcion==9:
            print("Saliendo")
            break
        else:
            print("Opción inválida")
if __name__=="__main__":
    main()

