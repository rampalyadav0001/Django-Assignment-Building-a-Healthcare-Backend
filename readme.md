
# 🏥 Django Healthcare Backend

A fully‑featured REST API for a healthcare system built with **Django 5**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
The backend supports JWT‑secured registration & login, plus complete CRUD for **Patients**, **Doctors**, and their relationships.

---

## 🎯 Objective

> Provide a secure backend where users can  
> • **Register / Log in** (JWT)  
> • **Manage Patients** (per‑user)  
> • **Manage Doctors** (global)  
> • **Map Patients ↔ Doctors**

---

## 🗂️ Requirements

| Requirement | Status |
|-------------|--------|
| Django + DRF | ✅ |
| PostgreSQL | ✅ |
| JWT (`djangorestframework‑simplejwt`) | ✅ |
| RESTful endpoints for Patients & Doctors | ✅ |
| Environment variables for secrets | ✅ |
| Error handling & validation | ✅ |

---

## 🔧 Tech Stack

| Layer  | Technology |
|--------|------------|
| Backend | Django 5, DRF 3.15 |
| Auth    | SimpleJWT |
| DB      | PostgreSQL 15 (or SQLite for quick dev) |
| Testing | Postman / curl / DRF Browsable API |

---

## 📦 Quick Start

```bash
# 1 Clone repo
git clone https://github.com/your‑username/healthcare-backend.git
cd healthcare-backend

# 2 Virtual env
python -m venv venv
source venv/bin/activate  # Windows → venv\Scripts\activate

# 3 Install deps
pip install -r requirements.txt

# 4 Environment
cp .env.example .env        # then edit values
#   SECRET_KEY=xxx
#   PG_DB=healthcare
#   PG_USER=hc_user
#   PG_PASSWORD=hc_pass

# 5 Migrations
python manage.py migrate

# 6 Create admin
python manage.py createsuperuser

# 7 Run!
python manage.py runserver
```

---

## 🔐 Authentication Flow (JWT)

1. `POST /api/auth/register/` → `{ name, email, password }`  
2. `POST /api/auth/login/`    → returns `{ access, refresh }`  
3. Add header to **every** protected call:  
   ```http
   Authorization: Bearer <access token>
   ```
4. Refresh token: `POST /api/token/refresh/` with `{ refresh: <refresh token> }`

---

## 🔁 API Reference

| Group | Endpoint | Methods | Auth |
|-------|----------|---------|------|
| **Auth** | `/api/auth/register/` | POST | ❌ |
|  | `/api/auth/login/` | POST | ❌ |
| **Patients** | `/api/patients/` | GET · POST | ✅ |
|  | `/api/patients/{id}/` | GET · PUT · DELETE | ✅ |
| **Doctors** | `/api/doctors/` | GET · POST | ✅ |
|  | `/api/doctors/{id}/` | GET · PUT · DELETE | ✅ |
| **Mappings** | `/api/mappings/` | GET · POST | ✅ |
|  | `/api/mappings/{patient_id}/` | GET | ✅ |
|  | `/api/mappings/detail/{id}/` | DELETE | ✅ |

> **Note:** “Authenticated” means header `Authorization: Bearer <access>` is required.

---

## 🛡️ Permissions

* **IsAuthenticated** – all patient, doctor, mapping endpoints  
* **IsOwner** – ensures users only read/write *their* patients  
* Doctors can be global or per‑user (toggle in `views.py`)

---

## 🧪 Testing with cURL

```bash
# Login
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/api/auth/login/   -H "Content-Type: application/json"   -d '{"email":"me@example.com","password":"secret"}' | jq -r .access)

# Create patient
curl -X POST http://127.0.0.1:8000/api/patients/   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"name":"John Doe","age":34,"notes":"Diabetic"}'
```

---

## 🗃️ Database Models

```text
User (custom) 1─∞ Patient
User (custom) 1─∞ Doctor
Patient ∞─∞ Doctor  → PatientDoctor (mapping)
```

Fields include timestamps (`created_at`) and foreign keys (`created_by`) for ownership.

---

## 📁 Project Structure

```
healthcare-backend/
├── accounts/         # custom User + auth serializers/views
├── core/             # patients, doctors, mappings
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── healthcare/       # project settings
│   └── settings.py
├── manage.py
└── README.md
```

---

## 🔒 Environment Variables

| Key | Purpose |
|-----|---------|
| `SECRET_KEY` | Django secret |
| `PG_DB`, `PG_USER`, `PG_PASSWORD`, `PG_HOST`, `PG_PORT` | PostgreSQL |
| `DEBUG` | `True` for dev, `False` for prod |

---

## ✍️ Author

**Rampal Yadav** – SIH 2024 Finalist  
 *LinkedIn*: <https://www.linkedin.com/in/rampal-yadav/>

---

