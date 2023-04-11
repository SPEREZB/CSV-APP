import csv
import sqlite3



# Lee el archivo CSV y guarda los datos en una lista
with open('datos.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Salta la primera fila si contiene encabezados
    data = [row for row in reader]



# Crea una conexión a la base de datos
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Crea una tabla en la base de datos
c.execute('''CREATE TABLE IF NOT EXISTS registros (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, isregistered BIT)''')



# Recorre los datos del archivo CSV y guarda cada registro en la base de datos
for row in data:
    id = row[0]
    name = row[1]
    isregistered = None  # Deja el campo "isregistered" como nulo
    c.execute('''INSERT INTO registros (id, name, isregistered) VALUES (?, ?, ?)''', (id, name, isregistered))



# Cierra la conexión a la base de datos
conn.commit()
conn.close()