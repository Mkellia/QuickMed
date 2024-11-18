from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database initialization
def init_db():
    conn = sqlite3.connect('quickmed.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        dob DATE NOT NULL,
                        contact TEXT NOT NULL,
                        medical_history TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER NOT NULL,
                        date DATE NOT NULL,
                        time TIME NOT NULL,
                        FOREIGN KEY (patient_id) REFERENCES patients(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS staff (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register-patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        contact = request.form['contact']
        medical_history = request.form['medical-history']

        conn = sqlite3.connect('quickmed.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, dob, contact, medical_history) VALUES (?, ?, ?, ?)",
                       (name, dob, contact, medical_history))
        conn.commit()
        conn.close()

        flash('Patient registered successfully!', 'success')
        return redirect(url_for('patient_list'))

    return render_template('patient-registration.html')

@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        patient_id = request.form['patient-id']
        date = request.form['date']
        time = request.form['time']

        conn = sqlite3.connect('quickmed.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (patient_id, date, time) VALUES (?, ?, ?)",
                       (patient_id, date, time))
        conn.commit()
        conn.close()

        flash('Appointment scheduled successfully!', 'success')
        return redirect(url_for('appointments'))

    return render_template('appointments.html')

@app.route('/patient-list')
def patient_list():
    conn = sqlite3.connect('quickmed.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()

    return render_template('patient-list.html', patients=patients)

@app.route('/staff-management', methods=['GET', 'POST'])
def staff_management():
    if request.method == 'POST':
        name = request.form['staff-name']
        role = request.form['role']

        conn = sqlite3.connect('quickmed.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO staff (name, role) VALUES (?, ?)", (name, role))
        conn.commit()
        conn.close()

        flash('Staff member added successfully!', 'success')
        return redirect(url_for('staff_management'))

    return render_template('staff-management.html')

# New route to view scheduled appointments
@app.route('/view-appointments')
def view_appointments():
    conn = sqlite3.connect('quickmed.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT a.id, p.name, a.date, a.time FROM appointments a
                      JOIN patients p ON a.patient_id = p.id''')
    appointments = cursor.fetchall()
    conn.close()

    return render_template('view-appointments.html', appointments=appointments)

# New route to view registered staff members
@app.route('/view-staff')
def view_staff():
    conn = sqlite3.connect('quickmed.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM staff')
    staff = cursor.fetchall()
    conn.close()

    return render_template('view-staff.html', staff=staff)

if __name__ == '__main__':
    app.run(debug=True)

