# 🎓 EduTrackX - Student Result Management System

EduTrackX is a modern, responsive, and robust Student Result Management System built using Python (Flask) and MySQL. It features a premium 3D login interface, a secure admin dashboard, and an easy-to-use portal for students to check their academic results.

## 🌟 Features

- **Premium 3D Login Interface:** An engaging, pixel-perfect, and modern login screen for both students and administrators.
- **Admin Dashboard:** A secure panel for administrators to manage the system.
- **Student Management:** Easily add new students, update their details, and manage their marks securely.
- **Result Portal:** Students can effortlessly search and view their academic results using their roll number and Date of Birth.
- **Secure Authentication:** Role-based access control ensuring data privacy.
- **Responsive Design:** Works flawlessly on desktops, tablets, and mobile devices.

## 🛠️ Technology Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Design:** Custom CSS with modern 3D UI elements, glassmorphism, and animations.

## 📋 Prerequisites

To run this project locally, you need to have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/installer/)

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/jantyking74-gif/antigravity-project.git
cd antigravity-project
```

**2. Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install the dependencies**
```bash
pip install -r requirements.txt
```

**4. Database Setup**
- Open your MySQL command line or a GUI tool like MySQL Workbench/XAMPP.
- Create a new database (e.g., `edutrackx`).
- Run the SQL queries found in the `database.sql` file to create the necessary tables and insert initial admin credentials.
- Update the database connection credentials (username, password, database name) in your `app.py` file to match your local MySQL setup.

**5. Run the Application**
```bash
python app.py
```

**6. Access the Web App**
Open your web browser and navigate to:
`http://127.0.0.1:5000/`

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
