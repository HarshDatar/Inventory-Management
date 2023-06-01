import mysql.connector as mariadbm
import matplotlib.pyplot as plt

print("hello")
# Connect to MySQL database
db = mariadb.connect(
    host="localhost",
    user=input("please enter the user name of your account"),
    password=input("please enter the password"),
    database="lol"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create inventory table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    price FLOAT
)
"""
cursor.execute(create_table_query)
db.commit()

# Function to display menu options
def display_menu():
    print("===== Inventory Management System =====")
    print("1. Add a product")
    print("2. Delete a product")
    print("3. Modify a product")
    print("4. View inventory")
    print("5. Plot graph")
    print("6. Exit")

# Function to add a product
def add_product():
    name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))

    add_product_query = """
    INSERT INTO inventory (product_name, quantity, price)
    VALUES (%s, %s, %s)
    """
    cursor.execute(add_product_query, (name, quantity, price))
    db.commit()
    print("Product added successfully!")

# Function to delete a product
def delete_product():
    product_id = int(input("Enter the product ID to delete: "))

    delete_product_query = "DELETE FROM inventory WHERE id = %s"
    cursor.execute(delete_product_query, (product_id,))
    db.commit()
    print("Product deleted successfully!")

# Function to modify a product
def modify_product():
    product_id = int(input("Enter the product ID to modify: "))

    # Check if the product exists
    check_product_query = "SELECT * FROM inventory WHERE id = %s"
    cursor.execute(check_product_query, (product_id,))
    product = cursor.fetchone()

    if product is None:
        print("Product not found!")
        return

    print("Current Product Details:")
    print("Product ID:", product[0])
    print("Product Name:", product[1])
    print("Quantity:", product[2])
    print("Price:", product[3])

    name = input("Enter the new product name (leave blank to keep current): ")
    quantity = input("Enter the new quantity (leave blank to keep current): ")
    price = input("Enter the new price (leave blank to keep current): ")

    update_product_query = "UPDATE inventory SET product_name = %s, quantity = %s, price = %s WHERE id = %s"

    if name == "":
        name = product[1]
    if quantity == "":
        quantity = product[2]
    if price == "":
        price = product[3]

    cursor.execute(update_product_query, (name, quantity, price, product_id))
    db.commit()
    print("Product modified successfully!")

# Function to view inventory
def view_inventory():
    view_inventory_query = "SELECT * FROM inventory ORDER BY id"
    cursor.execute(view_inventory_query)
    inventory = cursor.fetchall()

    if len(inventory) == 0:
        print("Inventory is empty!")
    else:
        print("===== Inventory =====")
        print("ID\tProduct Name\tQuantity\tPrice")
        for product in inventory:
            print(product[0], "\t", product[1], "\t\t", product[2], "\t\t", product[3])

# Function to plot a graph
def plot_graph():
    view_inventory_query = "SELECT * FROM inventory ORDER BY id"
    cursor.execute(view_inventory_query)
    inventory = cursor.fetchall()

    if len(inventory) == 0:
        print("Inventory is empty!")
    else:
        products = [product[1] for product in inventory]
        quantities = [product[2] for product in inventory]

        plt.bar(products, quantities)
        plt.xlabel("Product")
        plt.ylabel("Quantity")
        plt.title("Inventory")
        plt.xticks(rotation=45)
        plt.show()

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        delete_product()
    elif choice == "3":
        modify_product()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        plot_graph()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.close()
