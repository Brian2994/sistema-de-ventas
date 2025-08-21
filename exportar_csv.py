import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('tienda.db')

# Exportar cada tabla a CSV
tablas = ['clientes', 'productos', 'ventas']
for tabla in tablas:
    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
    df.to_csv(f"{tabla}.csv", index=False)
    print(f"{tabla}.csv exportado.")

conn.close()