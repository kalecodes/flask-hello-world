from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Kalen Wiley in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://kalecodes_flask_hello_world_user:zJUIuYJGjYiF3UjwZKTtA5ZcKW46WKmn@dpg-d4bt760gjchc73d0ceag-a/kalecodes_flask_hello_world")
    conn.close()
    return "Database Connection Successful"