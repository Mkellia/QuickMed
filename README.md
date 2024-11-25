---

# **QuickMed - Hospital Management System**

QuickMed is a web-based hospital management system built with Flask. It helps manage patients, staff, appointments, and more. The application includes authentication, data storage, and user-friendly interfaces for easy management.

---

## **Features**
- **User Authentication**: Sign up, login, and logout functionality.
- **Patient Management**: Add, view, and manage patient records.
- **Appointment Scheduling**: Schedule and view patient appointments.
- **Staff Management**: Manage staff records and roles.
- **Responsive UI**: Simple, responsive design for ease of use.

---

## **Tools and Technologies Used**
1. **Programming Language**: Python
2. **Web Framework**: Flask
3. **Database**: SQLite
4. **Frontend**:
   - HTML5
   - CSS3
5. **Testing Tool**: Selenium (for automated testing)

---

## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/quickmed.git
cd quickmed
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install flask werkzeug selenium
```

### 4. Initialize the Database
Run the app to automatically create the SQLite database:
```bash
python app.py
```

The `quickmed.db` file will be created automatically in the project directory.

### 5. Run the Application
```bash
python app.py
```

Visit the app in your browser at `http://127.0.0.1:5000`.

---

## **Project Structure**
```
quickmed/
├── app/
│   ├── app.py                 # Main Flask application
│   ├── templates/             # HTML templates
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── patient-registration.html
│   │   ├── appointments.html
│   │   ├── staff-management.html
│   │   ├── view-appointments.html
│   │   ├── view-staff.html
│   │   └── home.html
│   ├── static/                # Static files (CSS, images)
│   │   ├── styles.css
│   └── quickmed.db            # SQLite database file (auto-created)
├── requirements.txt           # Project dependencies
├── Procfile                   # For deployment (Heroku)
└── README.md                  # Documentation
```

---

## **Testing with Selenium**
We used Selenium for automated testing of the application.

### Prerequisites
- Install Selenium:
  ```bash
  pip install selenium
  ```

### Run the Test
Save the script (e.g., `test_login.py`) and run it:
```bash
python test_login.py
```

---

---

## **Contributing**
Contributions are welcome! Feel free to fork this project, create a new branch, and submit a pull request.

---
