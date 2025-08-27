import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Activar soporte de claves foráneas
cursor.execute("PRAGMA foreign_keys = ON")

# Crear tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Crear tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')

# Crear tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY,
    fecha TEXT NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
)
''')

# Guardar cambios y cerrar
conn.commit()
conn.close()

print("Base de datos y tablas creadas correctamente.")