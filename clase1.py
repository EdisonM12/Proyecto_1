import sqlite3
import os


def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS inventory (itemID TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)')
    conn.close()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\n=== INVENTARIO ===")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def show_inventory():
    clear_screen()
    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT * FROM inventory")
    products = cursor.fetchall()

    if not products:
        print("No hay productos")
    else:
        print(f"{'ID':<5} {'Nombre':<15} {'Precio':<10} {'Cantidad':<8}")
        print("-" * 40)
        for p in products:
            print(f"{p[0]:<5} {p[1]:<15} ${p[2]:<9} {p[3]:<8}")

    conn.close()
    input("\nEnter para continuar...")


def insert_data():
    print("\n--- AGREGAR PRODUCTO ---")
    item_id = input("ID: ")
    name = input("Nombre: ")
    price = input("Precio: ")
    quantity = input("Cantidad: ")

    if not all([item_id, name, price, quantity]):
        print("Error: Todos los campos son obligatorios")
        return

    conn = sqlite3.connect('data.db')
    try:
        conn.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)", (item_id, name, price, quantity))
        conn.commit()
        print("Producto agregado exitosamente")
    except sqlite3.IntegrityError:
        print("Error: ID ya existe")
    finally:
        conn.close()

def update_data():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    item_id = input("ID del producto a actualizar: ")

    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT * FROM inventory WHERE itemID = ?", (item_id,))
    product = cursor.fetchone()

    if not product:
        print("Producto no encontrado")
        conn.close()
        return

    print(f"Producto actual: {product[1]} - ${product[2]} - {product[3]} unidades")

    name = input(f"Nuevo nombre ({product[1]}): ") or product[1]
    price = input(f"Nuevo precio ({product[2]}): ") or product[2]
    quantity = input(f"Nueva cantidad ({product[3]}): ") or product[3]

    conn.execute("UPDATE inventory SET itemName=?, itemPrice=?, itemQuantity=? WHERE itemID=?",
                 (name, price, quantity, item_id))
    conn.commit()
    conn.close()
    print("Producto actualizado")


def delete_data():
    print("\n--- ELIMINAR PRODUCTO ---")
    item_id = input("ID del producto a eliminar: ")

    conn = sqlite3.connect('data.db')
    cursor = conn.execute("SELECT * FROM inventory WHERE itemID = ?", (item_id,))
    product = cursor.fetchone()

    if not product:
        print("Producto no encontrado")
        conn.close()
        return

    print(f"Producto: {product[1]}")
    confirm = input("¿Confirmar eliminación? (s/n): ")

    if confirm.lower() == 's':
        conn.execute("DELETE FROM inventory WHERE itemID = ?", (item_id,))
        conn.commit()
        print("Producto eliminado")

    conn.close()

def main():
    init_db()

    while True:
        show_menu()
        choice = input("\nOpción: ")

        if choice == '1':
            show_inventory()
        elif choice == '2':
            insert_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

if _name_ == "_main_":
    main()