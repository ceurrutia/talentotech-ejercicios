'''
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que
consume un coche por cada 100 km de recorrido,
el costo de cada litro de combustible y la longitud
del viaje realizado (en kilómetros), muestra un
detalle de los litros consumidos y el dinero
gastado.
'''

# cantLitros = float
# costoPorLitro = float
# distanciaViaje = float

# ##devolver

# listrosUsados = float
# dineroGastado = float

#Programa

consumoCombustible100 = float(input("Ingrese el consumo de combustible  cada 100 km: "))
costoPorLitro = float(input("Ingrese el precio por litro: "))
distanciaViaje = float(input("Ingrese la distancia a recorrer: "))

## 1lt --> 100 km
## distancia = x

listrosUsados =  (distanciaViaje * consumoCombustible100) /100
print(f"los litros usados seran: {listrosUsados}")

dineroGastado = listrosUsados  * costoPorLitro
print(f"Dinero gastado:  { dineroGastado}")