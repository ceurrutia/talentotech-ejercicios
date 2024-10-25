import sqlite3

connection = sqlite3.connect('dbproductos.db')

cursor = connection.cursor()

cursor.execute(
    '''
    create table if not exists products (
        id integer primary key autoincrement not null,
        name text not null,
        description text not null,
        price real,
        stock integer   
    )
    '''
)
cursor.execute(
    '''
    insert into products (name, description, price, stock)
    values ('shirt', 'pink', 3500.67, 8  
    )
    ''' 
)

cursor.execute('select * from products')
rows = cursor.fetchall()

for row in rows:
    print(row)
    
connection.close()
print("Programa finalizado. Adios")