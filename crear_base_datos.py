import sqlite3

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()

# Crear tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    email TEXT
)
''')

# Crear tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT,
    precio DECIMAL
)
''')

# Crear tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY,
    fecha TEXT,
    id_cliente INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
)
''')

# Guardar cambios y cerrar
conn.commit()
conn.close()

print("Base de datos y tablas creadas correctamente.")