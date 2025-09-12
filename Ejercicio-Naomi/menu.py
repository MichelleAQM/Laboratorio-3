from Producto import Producto
from Cliente import Cliente
from Venta import Venta
productos = []
clientes = []
ventas = []
def verMenu():
    print("SISTEMA DE VENTAS")
    print("1. Ingresar producto")
    print("2. Registrar cliente")
    print("3. Registrar venta")
    print("4. Mostrar productos")
    print("5. Mostrar clientes")
    print("6. Mostrar ventas")
    print("7. Salir")
def ejecutar_menu():
    while True:
        verMenu()
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            productos.append(Producto(nombre, precio))
        elif opcion == 2:
            dni = input("Ingrese DNI: ")
            nombre = input("Ingrese su nombre: ")
            clientes.append(Cliente(dni, nombre))
        elif opcion == 3:
            if not clientes or not productos:
                print("No hay clientes o productos registrados")
            else:
                print("CLIENTES")
                for a, b in enumerate(clientes):
                    print(f"{a+1}. {b.mostrar()}")
                cliente_sel = int(input("Seleccione cliente: ")) - 1
                cliente = clientes[cliente_sel]
                print("PRODUCTOS")
                for a, n in enumerate(productos):
                    print(f"{a+1}. {n.mostrar()}")
                producto_sel = int(input("Seleccione producto: ")) - 1
                producto = productos[producto_sel]
                cantidad = int(input("Cantidad a comprar: "))
                v = Venta(cliente, producto, cantidad)
                ventas.append(v)
        elif opcion == 4:
            print("LISTA DE PRODUCTOS")
            for n in productos:
                print(n.mostrar())
        elif opcion == 5:
            print("LISTA DE CLIENTES")
            for b in clientes:
                print(b.mostrar())
        elif opcion == 6:
            print("LISTA DE VENTAS")
            for v in ventas:
                print(v.mostrar())
        elif opcion == 7:
            print("Saliendo")
            break
        else:
            print("Opción inválida")


            