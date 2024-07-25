import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="new_user",  # Use the new MySQL user
        password="user_password",
        database="project_db"
    )

def create_user(name, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

def read_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()

def update_user(user_id, name, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_user('Ali', 'ali@gmail.com')
    read_users()
    update_user(1, 'Zaman', 'zamanpk@gmail.com')
    delete_user(2)
    read_users()
