#import json
import sqlite3

# conexion = sqlite3.connect(productos.db)
# cursor = conexion.cursor()

##CREAR LA TABLA

# def crearTabla():
#     cursor.execute('''
#                  CREATE TABLE IF NOT EXISTS productos( 
#                    ID INT PRIMARY KEY
#                    NOMBRE TEXT
#                    PRECIO REAL
#                    DESCRIPCION TEXT
#                    STOCK INTEGER
#                    ) 
#                    ''')
#     conexion.commit()

class Producto:
    def __init__(self, id, nombre, precio, descripcion, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
    
    # # Convert a diccionario par almacenat en .txt
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "nombre": self.nombre,
    #         "precio": self.precio,
    #         "descripcion": self.descripcion,
    #         "stock": self.stock
    #     }

productos = []

##FUNCION DE AGREGADO DE NUEVO PRODUCTO

def agregarProducto():
    id = input("Ingresa el ID del producto: ")
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    descripcion = input("Ingresa la descripción del producto: ")
    stock = int(input("Ingresa el stock del producto: "))
    producto = Producto(id, nombre, precio, descripcion, stock)
    productos.append(producto)


    #Instancia de clase
    producto = Producto(id, nombre, precio, descripcion, stock)
    
    # #Convertir a dict
    # producto_dict = producto.to_dict()
    
    # ##Usar el json importado, dump para guardar
    
    # with open('productos.txt', 'a') as file:
    #     json.dump(producto_dict, file)
    #     file.write('\n')

print("Producto agregado correctamente.")


##FUNCION DE ELIMINACION
def eliminarProducto():
    id = input("Ingresa el ID del producto a eliminar: ")
    for producto in productos:
        if producto.id == id:
            productos.remove(producto)
            print("Se ha eliminado el producto correctamente.")
            return
    print("No se ha encontrado el producto.")


##FUNCION DE ACTUALIZAR

def actualizarProducto():
    id = input("Ingresa el ID del producto a actualizar: ")
    for producto in productos:
        if producto.id == id:
            producto.nombre = input("Ingresa el nuevo nombre: ")
            producto.precio = float(input("Ingresa el nuevo precio: "))
            producto.descripcion = input("Ingresa la nueva descripción: ")
            producto.stock = int(input("Ingresa el nuevo stock: "))
            print("Se ha actualizado el producto correctamente.")
            return
    print("No se ha encontrado el producto.")

##LISTAR TODOS LOS PRODUCTOS

def mostrarProductos():
    if len(productos) == 0:
        print("No hay productos para mostrar.")
    for producto in productos:
        print("ID:", producto.id)
        print("Nombre:", producto.nombre)
        print("Precio:", producto.precio)
        print("Descripción:", producto.descripcion)
        print("Stock:", producto.stock)
       

##BUSCADOR POR ID DE PRODUCTO

def buscarProducto():
    id = input("Ingresa el ID del producto a buscar: ")
    
    for producto in productos:
        if producto.id == id:
            print("ID:", producto.id)
            print("Nombre:", producto.nombre)
            print("Precio:", producto.precio)
            print("Descripción:", producto.descripcion)
            print("Stock:", producto.stock)
            
        print("No se ha encontrado el producto.")
        
 ##Lanzar advertencia por bajo stock

def verificarBajoStock():
    limite = 5
    productosBajoStock = [producto for producto in productos if producto.stock <= limite]
    
    if productosBajoStock:
        print(f"Advertencia! quedan menos de 5 unidades")
        
    else:
        print("Productos con stock suficinete") 
        
           
## CARGAR nuevos productos cuando no haya

def reabastecerProducto():
    id = input("Ingresa el ID del producto a reabastecer: ")
    
    for producto in productos:
        if producto.id == id:
            cantidad = int(input("Ingresa la cantidad a reabastecer: "))
            producto.stock += cantidad
            print("Se ha reabastecido el producto correctamente.")
            verificarBajoStock()
            return

## simular la compra del producto restando cantidad 
def comprarProducto():
    id = input("Ingresa el ID del producto a comprar: ")
    for producto in productos:
        if producto.id == id:
            cantidad = int(input("Ingresa la cantidad a comprar: "))
            if cantidad <= producto.stock:
                producto.stock -= cantidad
                print("Se ha comprado el producto correctamente.")
                verificarBajoStock()
                return
            else:
                print("No hay suficiente stock para realizar la compra.")
                return
        print("No se ha encontrado el producto.")
 
  

##MENU DE OPCIONES

while True:
    print("******* MENU DE OPCIONES ********")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar productos")
    print("5. Buscar producto")
    print("6. Reabastecer producto")
    print("7. Comprar producto")
    print("8. Salir")

    try:
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            agregarProducto()

        elif opcion == 2:
            eliminarProducto()

        elif opcion == 3:
            actualizarProducto()

        elif opcion == 4:
            mostrarProductos()

        elif opcion == 5:
            buscarProducto()

        elif opcion == 6:
            reabastecerProducto()

        elif opcion == 7:
            comprarProducto()
            
        elif opcion == 8:
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")