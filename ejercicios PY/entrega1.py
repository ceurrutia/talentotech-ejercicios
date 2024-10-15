##Creo la clase producto
class Product():

    def __init__(self, id, name, description, price, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def showData(self):
        print(f"""
        ID: {self.id}
        Name: {self.name}
        Description: {self.description}
        Price: {self.price}
        Stock: {self.stock}
        """)


productList = []


##Crear
def createProduct():
    id = int(input("Enter product ID: "))
    name = str(input("Enter product name: "))
    description = str(input("Enter description: "))
    price = float(input("Enter single price: "))
    stock = int(input("Enter stock: "))
    newProduct = Product(id, name, description, price, stock)
    productList.append(newProduct)
    print("Product add successfully")


##Listar
def listProducts():
    if len(productList) == 0:
        print("Nothing in this list")
    else:
        for product in productList:
            product.showData()


##Remover
def removeProduct():
    idRemover = int(input("Enter product ID to remove: "))
    for product in productList:
        if idRemover == product.id:
            productList.remove(product)
            print("Product remove successfully")
            print(f"Id product: {product.id}, {product.name} was removed")
        else:
            print("Not found")


##Actualizar


def updateProduct():
    IdToUpdate = int(input("Enter the ID of the product to update:"))

    for product in productList:
        if IdToUpdate == product.id:
            product.name = str(input("Enter new name: "))
            product.description = str(input("Enter new description: "))
            product.price = float(input("Enter new price: "))
            product.stock = int(input("Enter new stock: "))
            print("Product update successfully")
            print(f"Id product: {product.id}, {product.name} was updated")

    print("ID not found")


##MENU####

while True:
    try:
        print("Select option")
        print("1. Add a new product")
        print("2. List products")
        print("3. Update a product by ID")
        print("4. Remove product by ID")
        print("5. Update stock")
        print("6. Exit")

        option = int(input("Select an option: "))
        if option == 1:
            createProduct()

        elif option == 2:
                print("### Products List ###")
                listProducts()

        elif option == 3:
            updateProduct()

        elif option == 4:
            removeProduct()

        elif option == 5:
            print("Updating stock...")

        elif option == 6:
            print("Exit the program...")
            break
        else:
            print("Invalid option")
    except (ValueError):
        print("You must enter a number")