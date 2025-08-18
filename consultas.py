import sqlite3
import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect('tienda.db')

# Función para ejecutar y mostrar consultas
def ejecutar_consulta(query, descripcion):
    print(f"\n🔹 {descripcion}")
    df = pd.read_sql_query(query, conn)
    print(df.head(10))  # Muestra los primeros 10 resultados
    print("-" * 50)

# 1. Ver los primeros clientes
ejecutar_consulta("SELECT * FROM clientes", "Primeros clientes")

# 2. Ver los productos
ejecutar_consulta("SELECT * FROM productos", "Lista de productos")

# 3. Ver algunas ventas
ejecutar_consulta("SELECT * FROM ventas", "Primeras ventas registradas")

# 4. Ventas por cliente (con nombre)
query_ventas_cliente = """
SELECT c.nombre, COUNT(v.id_venta) AS total_ventas
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.nombre
ORDER BY total_ventas DESC
LIMIT 10
"""
ejecutar_consulta(query_ventas_cliente, "Clientes con más ventas")

# 5. Ingresos por producto
query_ingresos_producto = """
SELECT p.nombre AS producto, 
       SUM(v.cantidad) AS total_vendido,
       SUM(v.cantidad * p.precio) AS ingresos
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.nombre
ORDER BY ingresos DESC
"""
ejecutar_consulta(query_ingresos_producto, "Ingresos por producto")

# 6. Ingresos por día (últimos 10 días)
query_ingresos_fecha = """
SELECT fecha, 
       SUM(v.cantidad * p.precio) AS ingresos_dia
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY fecha
ORDER BY fecha DESC
LIMIT 10
"""
ejecutar_consulta(query_ingresos_fecha, "Ingresos por fecha (últimos 10 días)")

# Cerrar conexión
conn.close()