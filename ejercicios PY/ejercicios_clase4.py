##Calcular promedio de 3

trim1 = float(input("Ingresa promedio primer trimestre: "))
trim2 = float(input("Ingresa promedio segundo trimestre: "))
trim3 = float(input("Ingresa promedio tercer trimestre: "))

prom_general = (trim1 + trim2 + trim3) / 3
print(f"El promedio general anual es de {prom_general}")

##Tu peso en la luna

pesoUsuario = float(input("Ingrese su peso en kg: "))
pesoLuna = 1.8

pesoEnLaLuna = pesoUsuario / pesoLuna
print(f"Tu peso en la luna es de {pesoEnLaLuna} kg.")

##Permiso para beber alcohol

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("Puedes beber")
else:
    print("No puedes beber")

##Es positivo o no

num = int(input("Ingresa un numero para saber si es positivo: "))

def esPositivo(num):
    if num > 0:
        return f"El numero {num} es positivo"
    else: 
        return f"El numero {num} es negativo"
print(esPositivo(num))

##Clase por meet

alumnos = int(input("Indique el numero de alumnos: "))
limite = 100
if alumnos > limite:
    print(f"Busque otra alternativa, el numero de alumos es {alumnos}, sobrapasa el limite de {limite}")
else:
    print(f"Reunase por meet que permite menos de {limite} alumnos")
    
##Una persona trabaja de martes a domingo, colectivo tarda mucho dias de semana
##trenes tardan mucho los fines de semana, dado dia, indicar si conviene tren o colectivo

diaTrabaja = input("INgrese que dia trabaja: ").lower()
dias = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]


if diaTrabaja == "lunes" or diaTrabaja == "Martes" or diaTrabaja == "Miercoles" or diaTrabaja == "Jueves"  or diaTrabaja == "Viernes":
    print("Toma colectivo aunque tarda por trafico")
else:
    print("Tome tren aunque tarda porque no hay unidades")

##contrasenia segura

passwordUsuario = input("Ingrese su contrasenia: ")

passCantidad = passwordUsuario.len()

def PassSecure(passCantidad):
    if passCantidad <=8 and passCantidad <= 16:
        return ("Su contrasenia ha sido creada")
    else:
        return("Su password debe tener entre 8 y 16 caracteres")
print(PassSecure(passwordUsuario))