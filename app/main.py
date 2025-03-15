from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(
        database="mydb",
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432"
    )
    return conn

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps!"}

@app.get("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"users": users}
