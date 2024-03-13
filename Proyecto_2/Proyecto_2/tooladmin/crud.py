import json


def crear_producto(producto, path):
    productos = {}
    with open(path, "r") as file:
        productos = json.load(file)

    for p in productos["data"]:
        if p["nombre"] == producto["nombre"]:
            print("El producto ya existe")
            return
        
    productos["data"].append(producto)

    with open(path, "w") as file:
        json.dump(productos, file, indent=4)  # Se escribe la lista actualizada en el archivo

def eliminar_producto(nombre_producto, path):
    with open(path, "r") as file:
        productos = json.load(file)
    
    for i, producto in enumerate(productos["data"]):
        if producto.get("nombre") == nombre_producto:
            del productos["data"][i]
            print(f"Producto {nombre_producto} eliminado del inventario.")
            break
    else:
        print(f"No se encontró ningún producto con el nombre {nombre_producto} en el inventario.")

    with open(path, "w") as file:
        json.dump(productos, file, indent=4)  # Se escribe la lista actualizada en el archivo

def buscar_producto(criterio, path):
    print(f"Buscando producto por criterio: {criterio}")
    with open(path, "r") as file:
        productos = json.load(file)
    
    productos_encontrados = []
    
    for producto in productos["data"]:
        if criterio.lower() in producto["nombre"].lower() or criterio.lower() in producto["categoria"].lower():
            productos_encontrados.append(producto)
    
    if productos_encontrados:
        print("Resultados de la búsqueda:")
        for producto in productos_encontrados:
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print("-----------------------")
    else:
        print("No se encontraron productos con el criterio de búsqueda.")

def actualizar_producto(nombre_producto, nueva_cantidad, nuevo_precio, path):
    print(f"Actualizando producto: {nombre_producto}")
    with open(path, "r") as file:
        productos = json.load(file)
    
    for producto in productos["data"]:
        if producto.get("nombre") == nombre_producto:
            producto["cantidad"] = nueva_cantidad
            producto["precio"] = nuevo_precio
            
            with open(path, "w") as file:
                json.dump(productos, file, indent=4)  # Se escribe la lista actualizada en el archivo
            
            print(f"Producto {nombre_producto} actualizado:")
            print(f"Nueva cantidad: {nueva_cantidad}")
            print(f"Nuevo precio: {nuevo_precio}")
            return
    
    print(f"Producto {nombre_producto} no encontrado. No se realizó ninguna actualización.")

def mostrar_inventario(path):
    print("Mostrando inventario:")
    with open(path, "r") as file:
        productos = json.load(file)
    
    for producto in productos["data"]:
        print(f"Nombre: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Cantidad en stock: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print("-----------------------")
