import sqlite3

##conexion database

conexion = sqlite3.connect('anime.db')
cursor = conexion.cursor()

cursor.execute(
     
     '''
     CREATE TABLE IF NOT EXISTS anime(
     id INTEGER PRIMARY KEY AUTOINCREMENT,  
     titulo TEXT CHECK(length(titulo) <= 100),  
     resumen TEXT CHECK(length(resumen) <= 300),  
     director TEXT CHECK(length(director) <= 50), 
     categoria TEXT,
     año INTEGER,
     episodios INTEGER,
     rating REAL
);
     
     '''
)
conexion.commit()

##clase

class Anime:
    def __init__(self, id, titulo, resumen, director, categoria, año, episodios, rating):
        self.id = id
        self.titulo = titulo
        self.resumen = resumen
        self.director = director
        self.categoria = categoria
        self.año = año
        self.episodios = episodios
        self.rating = rating

    def __str__(self):
        return f"ID: {self.id} \nTitulo: {self.titulo} \nResumen: {self.resumen} \nDirector: {self.director} \nCategoria: {self.categoria} \nAño: {self.año} \nEpisodios: {self.episodios} \nRating: {self.rating}"

    def verInfo(self):
        print(f'''
        ID: {self.id}
        Titulo: {self.titulo}
        Resumen: {self.resumen}
        Director: {self.director}
        Categoria: {self.categoria}
        Año estreno: {self.año}
        Episodios: {self.episodios}
        Rating: {self.rating}
        ''')


listaAnime = []


def VerListado():
     cursor.execute('SELECT * FROM anime ')
     animes = cursor.fetchall()
     print("***** Lista de animes en la coleccion ***** \n")
     if not animes:
          print(print("No hay registros ingresados"))  
    
     else:
          for anime in animes:
               print(f"ID: {anime[0]}, Titulo: {anime[1]}, Resumen: {anime[2]}, Director: {anime[3]}, Categoria:  {anime[4]}, Año: {anime[5]}, Episodios: {anime[6]}, Rating: {anime[7]}\n")


def agregarAnime():
    
    titulo = input("Ingrese titulo: ")
    resumen = input("Ingrese resumen: ")
    director = input("Ingrese director: ")
    categoria = input("Ingrese categoria: ")
    año = int(input("Ingrese año de estreno: "))
    episodios = int(input("Ingrese cantidad de episodios: "))
    rating = float(input("Ingrese rating: "))

    cursor.execute("INSERT INTO anime (titulo, resumen, director, categoria, año, episodios, rating) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (titulo, resumen, director, categoria, año, episodios, rating))
    conexion.commit()
    
    print("Nuevo anime agregado exitosamente")

def listarCategorias():
     cursor.execute('SELECT categoria, COUNT(*) FROM anime GROUP BY categoria')
     categorias = cursor.fetchall()
     
     if categorias:
         
          print("****** Categorias y cantidad de animes en ellas **** \n")
          for categoria, cantidad in categorias:
               print(f"Categoria: {categoria} \nCantidad: {cantidad}") 
     else:
          print("No se encontraron categorias ")
                 
     
          
##Modifica registros       

def modificarAnime():
    animeABuscar = input("Ingrese el nombre del anime a modificar: ").lower()
    
    cursor.execute("SELECT * FROM anime WHERE LOWER(titulo) = ?", (animeABuscar,))
    anime = cursor.fetchone()
    
    if anime:
        print(f"Se ha encontrado anime con nombre {anime[1]}")
        nuevo_resumen = input("Modifique resumen: ")
        nuevo_director = input("Modifique nombre del director: ")
        nueva_categoria = input("Modifique categoria: ")
        nuevo_año = input("Modifique el año de estreno: ")
        nuevo_episodios = input("Modifique la cantidad de episodios: ")
        nuevo_rating = input("Modifique el rating: ")
        
        cursor.execute("""
            UPDATE anime SET resumen = ?, director = ?, categoria = ?, año = ?, episodios = ?, rating = ?
            WHERE id = ?
        """, (nuevo_resumen, nuevo_director, nueva_categoria, nuevo_año, nuevo_episodios, nuevo_rating, anime[0]))
        
        conexion.commit()
        print("Anime modificado exitosamente")
        
    else:
        print("No se ha encontrado anime con ese nombre")



def buscarAnime():

     animeBuscar = input(
         "Ingrese el titulo del anime que desea buscar: ").lower()
     encontrado = False
     for anime in listaAnime:
          if anime.titulo.lower() == animeBuscar:
              encontrado = True
              print("El anime buscado se encuentra en la coleccion")

     if not encontrado:
          print("No se encontro el anime")


def eliminarAnime():

     id = int(input("Ingrese el id del anime que desea eliminar: "))
     encontrado = False
     for anime in listaAnime:
          if id == anime.id:
               listaAnime.remove(id)
               print("El anime ha sido eliminado")
               encontrado = True
     if not encontrado:
          print("No se encontro el anime")


     
##Menu

while True:

     try:
          print(" ***** Menu de opciones ***** ")
          print("1. Agregar nuevo anime")
          print("2. Listar animes")
          print("3. Listar categorias")
          print("4. Buscar anime")
          print("5. Eliminar anime ")
          print("6. Modificar registro")
          print("7. Salir")

          opcion = int(input("Ingrese opcion:"))

          if opcion == 1:
               agregarAnime()
          elif opcion == 2:
               VerListado()
          elif opcion == 3:
               listarCategorias()
          elif opcion == 4:
               buscarAnime()
          elif opcion == 5:
               eliminarAnime()
          elif opcion == 6:
               modificarAnime()
          elif opcion == 7:
               print("Has salido del sistema. Adios.")
               conexion.close()
               exit()
          else:
               print("Opcion no valida")

     except (ValueError):
          print("Debe ingresar solo numeros enteros")
          

