import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Conexión a la base de datos
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

fake = Faker()

# Insertar clientes
clientes = []
for i in range(1, 51):  # 50 clientes
    nombre = fake.name()
    email = fake.email()
    clientes.append((i, nombre, email))

cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?)", clientes)

# Insertar productos
productos = [
    (1, 'Laptop', 1200),
    (2, 'Mouse', 25),
    (3, 'Teclado', 45),
    (4, 'Monitor', 300),
    (5, 'Audífonos', 85)
]

cursor.executemany("INSERT INTO productos VALUES (?, ?, ?)", productos)

# Insertar ventas
ventas = []
id_venta = 1
for _ in range(200):  # 200 ventas
    fecha = fake.date_between(start_date='-6M', end_date='today').strftime("%Y-%m-%d")
    id_cliente = random.randint(1, 50)
    id_producto = random.randint(1, 5)
    cantidad = random.randint(1, 5)
    ventas.append((id_venta, fecha, id_cliente, id_producto, cantidad))
    id_venta += 1

cursor.executemany("INSERT INTO ventas VALUES (?, ?, ?, ?, ?)", ventas)

# Guardar y cerrar
conn.commit()
conn.close()

print("Datos insertados correctamente.")