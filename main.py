import csv

products = []

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
    print("7. Exit")

def get_choice():
    choice=input(" Select an option:")
    return choice


    
def add_product():
    product_name = input("Product Name: ")
    category = input("Category: ")
    quantity = input("Quantity: ")
    price = input("Price: ")

    product={"name":product_name,"category":category,"quantity":quantity,"price":price}

    products.append(product)
    save_to_csv()
    print("Product added succesfully")


    
def show_products():
    if not products:
        print("No products found.")
        return

    print("="*30)

    for product in products:
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Price: {product['price']}")

    print("="*30)


def search_product():
        search_name = input("Enter product name: ")

        for product in products:
            if product["name"].lower() == search_name.lower():
                print("=" * 30)
                print(f"Name: {product['name']}")
                print(f"Category: {product['category']}")
                print(f"Quantity: {product['quantity']}")
                print(f"Price: {product['price']}")
                print("=" * 30)
                return
            
        print("Product not found.")


def delete_product():
    delete_name = input("Enter product name to delete: ")

    for product in products:
        if product["name"].lower() == delete_name.lower():
            products.remove(product)
            save_to_csv()
            print("Product deleted successfully.")
            return

    print("Product not found.")

def update_product():
    update_name = input("Enter product name to update:")

    for product in products:
        if product["name"].lower() == update_name.lower():
            new_quantity = input("Write new quantity")
            new_price = input("Write new price")
            product["quantity"] = new_quantity
            product["price"] = new_price

            save_to_csv()

            print("Product updated successfully.")
            return

    print("Product not found.")



def save_to_csv():
    print("SAVE FUNCTION STARTED")
    print("Number of products:", len(products))

    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "category", "quantity", "price"])

        for product in products:
            writer.writerow([
                product["name"],
                product["category"],
                product["quantity"],
                product["price"]
            ])
            


def load_from_csv():
    try:
        with open("products.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product = {
                    "name": row[0],
                    "category": row[1],
                    "quantity": row[2],
                    "price": row[3]
                }

                products.append(product)

    except FileNotFoundError:
        print("No CSV file found. Starting with an empty inventory.")
    

def show_summary():
    total_products = len(products)

    total_stock = 0
    total_value = 0

    for product in products:
        total_stock += int(product["quantity"])
        total_value += int(product["quantity"]) * float(product["price"])

    print("=" * 35)
    print("       INVENTORY SUMMARY")
    print("=" * 35)
    print(f"Total Products: {total_products}")
    print(f"Total Items in Stock: {total_stock}")
    print(f"Total Inventory Value: {total_value:.2f}")
    print("=" * 35)



def main():
    #save_to_csv()
    load_from_csv()

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
            print("Goodbye!")
            break
        
        else:
            print("Invalid option")
    
main()