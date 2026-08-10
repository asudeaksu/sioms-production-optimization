import csv
import sqlite3


connection = sqlite3.connect("sioms.db")
cursor = connection.cursor()


def show_title():
    print("=" * 35)
    print(" Smart Inventory Management System")
    print("=" * 35) 

def show_menu():
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Update Product")
    print("6. Inventory Summary")
    print("7. Export to CSV")
    print("8. Exit")

def get_choice():
    choice=input(" Select an option:")
    return choice


    
def add_product():
    product_name = input("Product Name: ")
    category = input("Category: ")

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
    except ValueError:
        print("Invalid input. Quantity must be an integer and price must be a number.")
        return
    if quantity < 0 or price < 0:
        print("Quantity and price cannot be negative.")
        return


    cursor.execute(
        """
        INSERT INTO products (name, category, quantity, price)
        VALUES (?, ?, ?, ?)
        """,
        (product_name, category, quantity, price)
    )

    connection.commit()

    print("Product added successfully.")


    
def show_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    if not rows:
        print("No products found.")
        return

    print("=" * 30)

    for row in rows:
        print(f"Name: {row[0]}")
        print(f"Category: {row[1]}")
        print(f"Quantity: {row[2]}")
        print(f"Price: {row[3]}")

    print("=" * 30)


def search_product():
    search_name = input("Enter product name: ")

    cursor.execute(
        "SELECT * FROM products WHERE LOWER(name) = LOWER(?)",
        (search_name,)
    )

    row = cursor.fetchone()

    if row:
        print("=" * 30)
        print(f"Name: {row[0]}")
        print(f"Category: {row[1]}")
        print(f"Quantity: {row[2]}")
        print(f"Price: {row[3]}")
        print("=" * 30)
    else:
        print("Product not found.")


def delete_product():
    delete_name = input("Enter product name to delete: ")

    cursor.execute(
        "DELETE FROM products WHERE LOWER(name) = LOWER(?)",
        (delete_name,)
    )

    if cursor.rowcount > 0:
        connection.commit()
        print("Product deleted successfully.")
    else:
        print("Product not found.")



def update_product():
    update_name = input("Enter product name to update: ")

    try:
        new_quantity = int(input("Write new quantity: "))
        new_price = float(input("Write new price: "))
    except ValueError:
        print("Invalid input. Quantity must be an integer and price must be a number.")
        return
    if new_quantity < 0 or new_price < 0:
        print("Quantity and price cannot be negative.")
        return      


    cursor.execute(
        """
        UPDATE products
        SET quantity = ?, price = ?
        WHERE LOWER(name) = LOWER(?)
        """,
        (new_quantity, new_price, update_name)
    )

    if cursor.rowcount > 0:
        connection.commit()
        print("Product updated successfully.")
    else:
        print("Product not found.")



def save_to_csv():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "category", "quantity", "price"])

        for row in rows:
            writer.writerow(row)

    print("Products exported to CSV successfully.")
            



def show_summary():
    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(quantity) FROM products")
    total_stock = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(quantity * price) FROM products")
    total_value = cursor.fetchone()[0]

    print("=" * 35)
    print("       INVENTORY SUMMARY")
    print("=" * 35)
    print(f"Total Products: {total_products}")
    print(f"Total Items in Stock: {total_stock}")
    print(f"Total Inventory Value: {total_value:.2f}")
    print("=" * 35)




def main():

    while True:
        show_title()
        show_menu()

        choice = get_choice()


        if choice == "1":
            add_product()

        elif choice == "2":
            show_products()

        elif choice == "3":            
            search_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            update_product()

        elif choice == "6":
            show_summary()

        elif choice == "7":
            save_to_csv()

        elif choice == "8":
            print("Goodbye!")
            connection.close()
            break

        else:
            print("Invalid option")
    
main()