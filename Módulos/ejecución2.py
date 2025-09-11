from estudiante import Estudiant
lista=[]
n = int(input("¿Cuántos estudiantes registrará?: "))
for i in range(n):
    print("Registro estudiante ",i+1)
    est=Estudiant()
    est.ingresarDatos()
    lista.append(est)
print("ESTUDIANTES REGISTRADOS")
for est in lista:
    est.imprimirDatos()
