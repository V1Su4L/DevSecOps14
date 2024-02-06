from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
db_params = {
    'dbname': 'flask_color_app',
    'user': 'flask_user',
    'password': 'flask_password',
    'host': 'postgres'
}

# Route to get data from the database


@app.route('/')
def get_data():
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Example query
        cursor.execute("SELECT * FROM colors")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(data)

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
