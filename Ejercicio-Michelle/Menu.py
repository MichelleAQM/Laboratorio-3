from Clases import *
productos = [Producto("Pan", 50, 2.5),
            Producto("Leche", 30, 4.0),
            Producto("Huevos", 100, 0.8),
            Producto("Arroz", 40, 6.0),
            Producto("Azúcar", 25, 3.5),
            Producto("Aceite", 20, 8.0),
            Producto("Queso", 15, 12.0),
            Producto("Jugo", 60, 3.0),
            Producto("Yogur", 50, 2.0),
            Producto("Mantequilla", 10, 7.0)]
def menu_real():
    cliente = None
    venta = None
    opcion = 1
    while opcion != 4:
        print("-------Tienda-------")
        print("1. Mostrar productos")
        print("2. Registrar cliente")
        print("3. Realizar la venta")
        print("4. Salir")
        opcion = int(input("Elija una opción:"))
        if opcion == 1:
            Producto.mostrar_todos_productos()
        elif opcion == 2:
            nombre = input("Ingrese nombre del cliente: ")
            edad = int(input("Ingrese edad del cliente: "))
            dni = input("Ingrese DNI del cliente: ")
            cliente = Cliente(nombre, edad, dni)
            print("Cliente registrado correctamente.")
        elif opcion == 3:
            if cliente is None:
                print("Primero registre un cliente.")
                continue
            metodo_pago = input("Ingrese método de pago (Efectivo/Tarjeta): ")
            venta = Venta(cliente, metodo_pago)
            seguir = "S"
            while seguir == "S":
                Producto.mostrar_todos_productos()
                prod_num = int(input("Seleccione número del producto: ")) - 1
                if 0 <= prod_num < len(Producto.productos_disponibles):
                    cantidad = int(input("Ingrese cantidad a comprar: "))
                    venta.agregar_producto(Producto.productos_disponibles[prod_num], cantidad)
                else:
                    print("Producto inválido.")
                seguir = input("¿Desea agregar otro producto? (S/N): ") 
            venta.mostrar_factura()
        elif opcion == 4:
            print("Gracias por usar el sistema de ventas.")
        else:
            print("Opción inválida.")