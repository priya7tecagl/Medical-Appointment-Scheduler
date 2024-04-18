from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('html_file.html')


@app.route('/appointments', methods=['GET'])
def get_appointments():
    conn = sqlite3.connect('medical.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    conn.close()
    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    patient = data.get('patient')
    date = data.get('date')
    conn = sqlite3.connect('medical.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (patient, date) VALUES (?, ?)', (patient, date))
    conn.commit()
    conn.close()
    return jsonify(data), 201

@app.route('/patients', methods=['GET'])
def get_patients():
    conn = sqlite3.connect('medical.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    conn = sqlite3.connect('medical.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO patients (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)
