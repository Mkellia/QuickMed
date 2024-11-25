---                                                                                                                                                                                                                                                                       # **QuickMed - Hospital Management System**                                                                                                                                                                                                                               QuickMed is a web-based hospital management system built with Flask. It provides tools to manage patients, staff, and appointments in a seamless and efficient way. The system features user authentication, data storage, and responsive design.

---

## **Features**
- **User Authentication**: Users can sign up, log in, and log out.
- **Patient Management**: Add, view, and update patient records.
- **Appointment Scheduling**: Schedule and view patient appointments.
- **Staff Management**: Add and manage staff details.
- **Responsive Design**: The UI is built to work across devices.

---

## **Frontend**
The frontend is built using **HTML5** and **CSS3**. It includes:

1. **Templates**:
   - The UI is structured with Flask templates (`.html` files) located in the `templates/` directory.
   - Templates are dynamic and render data passed from the Flask backend.

2. **Styling**:
   - The application uses CSS for styling, located in the `static/styles.css` file.                                                     - Each page (e.g., signup, login, appointments) has a clean, consistent layout with responsive design.                                                                                                                                                                 3. **Navigation**:                                                                                                                      - Easy navigation with links and buttons for all major operations, such as registering patients, managing staff, and viewing appointments.
  ---

## **Backend**
The backend is built using the **Flask** framework in Python. It handles:

1. **Routes**:
   - Each page and functionality has a corresponding route defined in the `app.py` file.
   - Example routes:
     - `/signup`: Handles user registration.
     - `/login`: Manages user login.
     - `/register-patient`: For adding patient records.
     - `/view-staff`: Displays staff details.

2. **Database**:
   - **SQLite** is used for data storage.
   - Tables include:
     - `users`: Stores user credentials and details.
     - `patients`: Manages patient information.
     - `appointments`: Keeps track of scheduled appointments.
     - `staff`: Stores staff details.

3. **Data Flow**:
   - Forms in the frontend send data to the backend using HTTP POST requests.
   - Data is processed in Python, stored in the database, and then displayed back on the UI.

4. **Security**:
   - Passwords are securely hashed using `werkzeug.security`.
   - Sessions are managed to authenticate and track logged-in users.

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
└── README.md                  # Documentation
```

---

## **How It Works**

1. **User Authentication**:
   - Users can sign up, log in, and log out using secure authentication.
   - Upon login, users are redirected to a dashboard for managing operations.

  2. **Patient Management**:
   - Add new patients through a form.
   - View all registered patients in a table format.
   - Update patient records when needed.

3. **Appointment Scheduling**:
   - Schedule appointments by selecting a patient and specifying a date and time.
   - View all scheduled appointments in a structured table.

4. **Staff Management**:
   - Add staff members with their roles.
   - View and manage all staff records.

---


