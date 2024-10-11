a = int(input("Ingrese un valor numerico: "))
b = int(input("Ingrese otro valor numerico: "))

def sumar(a,b):
    return a + b

print(f"El resultado de la suma es: {sumar(a,b)}")

def restar(a,b):
    return a - b

print(f"El resultado de la resta es: {(restar(a,b))}" )

def multiplicar(a,b):
    return a * b

print(f"El resultado de la multiplicacion es: {multiplicar(a,b)}")

def dividir(a,b):
    if (b == 0):
        return "No dividas por 0"
    else:
       return a / b
        
print(f"El resultado de la division es: {dividir(a,b)}") 

##encuentra una ciudad en una lista
##Aplica que sea insensible a mayuscula y minuscula

ciudadUsuario = input("Ingresa una ciudad: ")

listaCiudades = ["paris", "madrid", "Roma", "Bruselles"]
listaCiudades = [ciudad.lower() for ciudad in listaCiudades]

if (ciudadUsuario in listaCiudades):
    
    print("Esta en la lista")
else:
    print("No esta en la lista ")
    