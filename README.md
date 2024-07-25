# MySQL Python Project

This project demonstrates how to interact with a MySQL database using Python.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/mysql-python-project.git
    cd mysql-python-project
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Start MySQL and create the database, tables, and user:
    ```sql
    CREATE DATABASE project_db;
    USE project_db;

    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    );

    CREATE TABLE orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        product VARCHAR(100),
        amount DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    INSERT INTO users (name, email) VALUES ('Usama Abid', 'iusaamaabid@gmail.com');
    INSERT INTO users (name, email) VALUES ('Abdullah Abid', 'abdullahabid@gmail.com');

    INSERT INTO orders (user_id, product, amount) VALUES (1, 'Laptop', 999.99);
    INSERT INTO orders (user_id, product, amount) VALUES (2, 'Smartphone', 599.99);

    CREATE USER 'my_test_user'@'localhost' IDENTIFIED BY 'My@Test123';
    GRANT ALL PRIVILEGES ON project_db.* TO 'my_test_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

## Running the Script

1. Run the Python script:
    ```bash
    python main.py
    ```

## CRUD Operations

- **Create**: Adds a new user to the database.
- **Read**: Retrieves and displays all users from the database.
- **Update**: Updates an existing user's information.
- **Delete**: Deletes a user from the database.

## License

This project is licensed under the MIT License.
