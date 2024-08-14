from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100));')
    cur.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');")
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
