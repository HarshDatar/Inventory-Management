# Inventory Management System :chart_with_upwards_trend:

A simple command-line inventory management system implemented in Python, using MySQL database for storage.

## :computer: Prerequisites

- Python 3.x
- MySQL server

## :wrench: Setup

### Clone the repository:

   ```git clone https://github.com/dyrok/Inventory-Management```
   
##Configure the MySQL database connection in the script (main.py):

### Connect to MySQL database
```
db = mariadb.connect(
    host="localhost",
    user="your-username",
    password="your-password",
    database="invproj"
)
```
### Create the database:
```
    mysql -u your-username -p
    > CREATE DATABASE invproj;
    > USE invproj;
```

### :rocket: Usage Run the script:
```python main.py```

Follow the on-screen menu options to perform various actions such as adding products, modifying quantities, deleting products, and viewing the inventory. You can also plot a graph of the inventory by selecting the "Plot graph" option.

### :file_folder: Project Structure

```
├── main.py         # Main script file
└── README.md       # Project documentation
```
