# 💼 Job Portal API – FastAPI + PostgreSQL

A modern, high-performance REST API backend for a Job Portal application, built with **FastAPI** and **PostgreSQL**. This backend supports features like job postings, user registration, job applications, and more — with clean architecture and secure JWT authentication.

---

## 🚀 Features

- ✅ User Registration & Login (JWT Authentication)
- 👤 Role-based access (Job Seeker / Recruiter)
- 📢 Recruiters can post, update, and delete jobs
- 🔍 Job Seekers can search and apply for jobs
- 📄 Resume upload and application tracking
- 🛡️ Password hashing and secure token handling
- 🧪 Auto-generated API Docs with Swagger & ReDoc

---

## 🧰 Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Auth**: OAuth2 Password Flow + JWT
- **Env Config**: python-dotenv

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

DATABASE_URL = postgresql://username:password@localhost:5432/jobportaldb

SECRET_KEY = your_secret_key
ALGORITHM=HS256

default_sender = <yoursenderemail@gmail.com>
default_receiver = <yourreceiveremail@gmail.com>
app_password= default_sender's gmail_app password

---

## 🛠️ Setup Instructions

1. **Clone the repository**:

   ```
   git clone https://github.com/Shekh-Taukir/Job_Portal.git
   cd job-portal-api
   ```

2. **Create a virtual environment**:

   ````python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows```
   ````

3. **Install dependencies:**:

   `pip install -r requirements.txt`

🧑‍💻 Author
Taukir Shekh
