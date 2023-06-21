
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MongoDB_URL = "mongodb+srv://academia:QA93DNruRfIc7X7K@cluster0.vigzmaf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(MongoDB_URL, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

from pymongo import MongoClient

MongoDB_URL = "mongodb+srv://academia:QA93DNruRfIc7X7K@cluster0.vigzmaf.mongodb.net/?retryWrites=true&w=majority"

# Conectar a la base de datos
def connect_to_db():
    client = MongoClient(MongoDB_URL)
    return client["academia"]

# Insertar datos
def insert_data(items):
    db = connect_to_db()
    db.inventory.insert_many(items)

# Obtener datos
def get_data(filter):
    db = connect_to_db()
    results = db.inventory.find(filter)
    for item in results:
        print(item)

# Actualizar datos
def update_data(filter, updates):
    db = connect_to_db()
    db.inventory.update_one(filter, updates)

# Borrar datos
def delete_data(filter):
    db = connect_to_db()
    results = db.inventory.delete_many(filter)
    print(f"Se han borrado {results.deleted_count} documentos")

# Menú principal
def main_menu():
    print("Por favor, selecciona el número del tipo de consulta:")
    print("1. Ingresar")
    print("2. Consultar")
    print("3. Actualizar")
    print("4. Borrar")
    opc = int(input("Selecciona la sentencia que deseas ejecutar: "))
    return opc

# Lógica principal
def main():
    opc = main_menu()

    if opc == 1:
        items = [
            {
                "name": input("Escribe el nombre: "),
                "category": input("Escribe la categoría: "),
                "quantify": int(input("Escribe la cantidad: ")),
                "price": int(input("Escribe el precio: ")),
            }
        ]
        insert_data(items)

    elif opc == 2:
        filter = {"category": input("Ingresa la categoría del producto: ")}
        get_data(filter)

    elif opc == 3:
        filter = {"name": input("Ingresa el nombre del producto a actualizar: ")}
        updates = {
            "$set": {
                "name": input("Escribe el nuevo nombre: "),
                "category": input("Ingresa la nueva categoría: "),
                "quantify": int(input("Escribe la nueva cantidad: ")),
                "price": int(input("Escribe el nuevo precio: ")),
            }
        }
        update_data(filter, updates)

    elif opc == 4:
        filter = {"name": input("Ingresa el nombre del producto a borrar: ")}
        delete_data(filter)

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()

    