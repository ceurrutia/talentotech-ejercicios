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


##Crear un nuevo producto

def createProduct():
    id = int(input("Enter product ID: "))
    name = str(input("Enter product name: "))
    description = str(input("Enter description: "))
    price = float(input("Enter single price: "))
    stock = int(input("Enter stock: "))
    newProduct = Product(id, name, description, price, stock)
    productList.append(newProduct)
    print("Product add successfully")


##Listar todos los productos

def listProducts():
    if len(productList) == 0:
        print("Nothing in this list")
    else:
        for product in productList:
            product.showData()


##Remover por ID

def removeProduct():
    idRemover = int(input("Enter product ID to remove: "))
    for product in productList:
        if idRemover == product.id:
            productList.remove(product)
            print("Product remove successfully")
            print(f"Id product: {product.id}, {product.name} was removed")
        else:
            print("Not found")


##Actualizar datos de producto

def updateProduct():
    IdToUpdate = int(input("Enter the ID of the product to update description or price:"))

    for product in productList:
        if IdToUpdate == product.id:
            product.description = str(input("Enter new description: "))
            product.price = float(input("Enter new price: "))
            print("Product update successfully")
            print(f"Id product: {product.id}, {product.name} was updated")

    print("ID not found")
    
##Buscar un producto por ID

def searchProduct():
    IDToSearch = int(input("Enter the product ID: "))
    found = False
    
    for product in productList:
        if IDToSearch == product.id:
            found: True
            print(f"The Product with ID: {product.id}, name: {product.name}, description: {product.description} is in the list")
        
    print("Product not found")


##Comprar producto y que tenga stock
    
def byProduct():
    found = False
    id = int(input("Enter the product ID: "))
    userCant = int(input("Enter qantity: "))
    
    for product in productList:
        if id == product.id:
            found = True
            if userCant <= product.stock:
                product.stock -= userCant
                print("You bougth the product correctly")
                print("Total value: ", product.price * userCant)
            else:
                print("Not enough stock for this product. Try with other!")
            
##Recargar stock

def updateStock():
    id = int(input("Enter product id to update stock: "))
    cantStock = int(input("Enter cantity to update: "))
    found = False      
    
    for product in productList:
        if id == product.id:
            found = True
            product.stock += cantStock
            print("Good! Now you have ",product.stock, "unities in product ID: ", product.id)
            break
        
        else:
            print("ID not found")

##MENU####

while True:
    try:
        print("Select option")
        print("1. Add a new product")
        print("2. List products")
        print("3. Update a description or price of the product by ID")
        print("4. Remove product by ID")
        print("5. Update stock")
        print("6. Search product by ID or name")
        print("7. Buy a product")
        print("8. Exit")

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
            updateStock()
            
        elif option == 6:
            searchProduct()
            
        elif option == 7:    
            byProduct()

        elif option == 8:
            print("Exit the program... Bye!")
            break
        else:
            print("Invalid option")
    except (ValueError):
        print("You must enter a number")