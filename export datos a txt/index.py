import json

##Crear un diccionario

midict = {
   1: {
        "titulo": "Catnip, why cats loves it",
        "author": "Karen",
        "year": 2020   
    },
   2: {
        "titulo": "Okisanante Kankenayou",
        "author": "Aki Kurokawa",
        "year": 2016   
    },
   3: {
        "titulo": "Los dias",
        "author": "Natalya Ruanova",
        "year": 1996   
    }
   }

print(midict[1])

##CUsar metodo dump de json de escritura para guardar

with open('midict.txt', 'w') as archivo:
    json.dump(midict, archivo)
    
print("Libritos guardados en un txt")

##Levantarlo de nuevo para leer

with open('midict.txt', 'r') as archivo:
    cargaLibros = json.load(archivo)
    
print(cargaLibros)