from estudiante import Estudiant
lista=[]
for i in range(4):
    print("Registro estudiante ",i+1)
    est=Estudiant()
    est.ingresarDatos()
    lista.append(est)
print("ESTUDIANTES REGISTRADOS")
for est in lista:
    est.imprimirDatos()
