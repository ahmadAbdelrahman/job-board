# 🏗️ JobBoard — Django & React Job Portal

## 📌 Project Overview
**JobBoard** is a job posting and application management system built using Django (backend), React (frontend), and PostgreSQL (database). This project provides a functional job board where employers can post vacancies and candidates can apply.

## 🚀 Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Frontend:** React
- **Database:** PostgreSQL
- **Authentication:** Token-based authentication via DRF

## 🔧 Features
- **User Roles**: Candidates & Employers
- **Authentication**: Secure login via token-based authentication
- **Job Listings**: CRUD functionality for employers
- **Applications**: Candidates can apply to job postings
- **REST API**: Endpoints available for frontend communication

## 🛠️ Setup Instructions
### **Backend (Django)**
1. Clone the repository:
```bash
git clone https://github.com/ahmadAbdelrahman/job-board.git
cd jobboard_backend
```
2. Create a virtual environment & install dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```
3. Configure PostgreSQL:
```bash
# Open PostgreSQL shell
psql -U postgres

# Create database
CREATE DATABASE jobboard_db;

# Create user & grant privileges
CREATE USER jobboard_user WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE jobboard_db TO jobboard_user;
```
4. Generate .env file:
```bash
NAME=your_database_name
USER=your_username
PASSWORD=your_password
HOST=localhost
PORT=5432
```
5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Start the Django server:
```bash
python manage.py runserver
```

### **Frontend (React)**
To be implemented in the next milestone.


## 🎯 Roadmap
- ✅ Backend API Development (Django, PostgreSQL, DRF)
- 🔄 Frontend Integration (React)
- 🔄 UI Improvements & Job Search Filters
- 🔄 Deployment & Scalability Enhancements

## 📝 License
This project is open-source. Feel free to contribute and improve it!

## 💡 Contributions Welcome!
pen a pull request or raise issues if you want to enhance functionality. Happy coding! 🚀
