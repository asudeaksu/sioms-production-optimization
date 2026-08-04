products= [  { "name": "Keyboard",
        "category": "Electronics",
        "quantity": "5",
        "price": "1200" } ,
    {
        "name": "Mouse",
        "category": "Electronics",
        "quantity": "10",
        "price": "500"
    }]

def show_title():
    print("=" * 35)
    print(" Smart Inventory Management System")
    print("=" * 35)

def show_menu():
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

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
    print("Product added succesfully")


    
def show_products():
    print ("=" * 30)
    if not products:
        print("No products found.")
        return

    for product in products:
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Price: {product['price']}")
    print ("=" * 30)

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
            print("Search product")

        elif choice == "4":
            print("Delete product")

        elif choice == "5":
            print(" Goodbye!")
            break
        
        else:
            print("Invalid option")
    
main()
