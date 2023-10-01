import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='inventory'
)
cursor = conn.cursor()

# Create inventory table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    )
''')

def add_item(name, quantity, price):
    # Add a new item to the inventory
    sql = 'INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)'
    values = (name, quantity, price)
    cursor.execute(sql, values)
    conn.commit()
    print('Item added to the inventory.')

def sell_item(item_id, quantity):
    # Sell a specific quantity of an item from the inventory
    sql = 'SELECT quantity FROM inventory WHERE id = %s'
    values = (item_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        current_quantity = result[0]
        if current_quantity >= quantity:
            new_quantity = current_quantity - quantity
            sql = 'UPDATE inventory SET quantity = %s WHERE id = %s'
            values = (new_quantity, item_id)
            cursor.execute(sql, values)
            conn.commit()
            print(f'Sold {quantity} units of item {item_id}.')
        else:
            print('Insufficient quantity in the inventory.')
    else:
        print('Item not found in the inventory.')

def display_inventory():
    # Display the current inventory
    cursor.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print('Inventory is empty.')

def calculate_total_value():
    # Calculate the total value of the inventory
    cursor.execute('SELECT SUM(quantity * price) FROM inventory')
    result = cursor.fetchone()

    if result[0]:
        total_value = result[0]
        print(f'Total inventory value: ${total_value:.2f}')
    else:
        print('Inventory is empty.')

# Main menu
while True:
    print('\n==== Shop Inventory System ====')
    print('1. Add Item')
    print('2. Sell Item')
    print('3. Display Inventory')
    print('4. Calculate Total Value')
    print('5. Quit')

    choice = input('Enter your choice (1-5): ')

    if choice == '1':
        name = input('Enter the item name: ')
        quantity = int(input('Enter the quantity: '))
        price = float(input('Enter the price: '))
        add_item(name, quantity, price)
    elif choice == '2':
        item_id = int(input('Enter the item ID: '))
        quantity = int(input('Enter the quantity to sell: '))
        sell_item(item_id, quantity)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        calculate_total_value()
    elif choice == '5':
        break
    else:
        print('Invalid choice. Please try again.')

# Close the database connection
cursor.close()
conn.close()