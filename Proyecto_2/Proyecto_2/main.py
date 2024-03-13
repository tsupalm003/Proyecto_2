from tooladmin.crud import crear_producto, eliminar_producto, buscar_producto, actualizar_producto, mostrar_inventario

# Definimos la ruta del archivo de base de datos
path = "database.json"

print("------------------------------------------------------------")
print("Sistema de Administración de Inventario para una Farmacia")
print("------------------------------------------------------------")

# Bucle principal del programa
while True:
    # Menú de opciones
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Actualizar cantidad y precio de un producto")
    print("6. Salir")

    # Solicitar al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Opción 1: Agregar producto
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        cantidad_en_stock = int(input("Ingrese la cantidad en stock: "))  # Modificado
        precio = float(input("Ingrese el precio del producto: "))

        nuevo_producto = {
            'nombre': nombre,
            'categoria': categoria,
            'cantidad_en_stock': cantidad_en_stock,  # Modificado
            'precio': precio
        }

        crear_producto(nuevo_producto, path)
        print(f"Producto {nombre} agregado al inventario.")

    # Opción 2: Mostrar inventario
    elif opcion == "2":
        mostrar_inventario(path)

    # Opción 3: Eliminar producto
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre, path)

    # Opción 4: Buscar producto
    elif opcion == "4":
        criterio = input("Ingrese el nombre o categoría a buscar: ")
        buscar_producto(criterio, path)

    # Opción 5: Actualizar cantidad y precio de un producto
    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        # Llamar a la función para actualizar la cantidad y precio del producto en el inventario
        actualizar_producto(nombre, nueva_cantidad, nuevo_precio, path)
        # Imprimir mensaje de confirmación
        print(f"Cantidad de {nombre} actualizada en el inventario.")



    # Opción 6: Salir
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Manejo de opciones no válidas
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
