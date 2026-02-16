# 🏦 NextGen Bank API

> A robust, production-ready banking system API built with Django REST Framework.

Welcome to the **Bank Server** repository! This project is a comprehensive backend simulation of a modern banking platform. It handles everything from secure user authentication and KYC verification to complex financial transactions and background interest calculations.

---

## 🚀 Key Features

### 🔐 **Authentication & Security**
* **Role-Based Access:** Distinct roles for Customers, Tellers, Account Executives, and Branch Managers.
* **Secure Login:** JWT Authentication (via Djoser) with cookie-based security.
* **Account Protection:** Auto-locking accounts after failed login attempts and OTP verification.
* **Security Questions:** Extra layer of security for user recovery.

### 👤 **User Profiles & KYC**
* **Detailed Profiles:** Manages employment history, identification documents (Passport/ID), and Next of Kin details.
* **Media Handling:** Integration with **Cloudinary** for storing profile pictures and signature uploads.
* **KYC Workflow:** Tracks if a user has submitted KYC and verification status.

### 💰 **Banking Operations**
* **Multi-Currency Support:** Accounts available in **USD**, **GBP**, and **KES** (Kenya Shilling).
* **Account Types:** Support for **Savings** (with interest) and **Current** accounts.
* **Daily Interest:** An automated **Celery Beat** task calculates and applies interest to savings accounts daily based on balance tiers.

### 💳 **Cards & Transactions**
* **Virtual Cards:** Generate and manage virtual debit cards with CVV and expiry dates.
* **Transactions:** Full ledger for Deposits, Withdrawals, and Transfers.
* **PDF Generation:** (Ready for) generating statements and transaction receipts.

---

## 🛠️ Tech Stack

* **Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Async Tasks:** Celery + RabbitMQ + Redis (for caching & message brokering)
* **Containerization:** Docker & Docker Compose
* **Documentation:** DRF Spectacular (Swagger/Redoc)
* **Utilities:** Mailpit (Email testing), Flower (Celery monitoring)

---

## 🐳 Getting Started

This project relies heavily on **Docker** to keep the development environment clean and consistent.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.
* **Make** (optional, but makes running commands much easier).

### 1. Clone the Repo
```bash
git clone [https://github.com/talin12/bank-server.git](https://github.com/talin12/bank-server.git)
cd bank-server
2. Environment Variables
Create your local environment files. You will need a .envs/.env.local file inside the root directory.

3. Build & Run
We use a Makefile to simplify common Docker commands.

Build and start the containers:

Bash
make build
This handles building the Django image, setting up Postgres, Redis, RabbitMQ, and the Celery workers.

Run migrations:
Once the containers are up, apply the database schema:

Bash
make migrate
4. Create a Superuser
To access the Django Admin panel:

Bash
make superuser
🎮 Usage
Accessing the API
The API is exposed via Nginx.

API Root: http://localhost:8080/api/v1/

Admin Panel: http://localhost:8080/supersecret/

API Documentation 📖
Don't guess the endpoints! We use Swagger for interactive documentation.

Swagger UI: http://localhost:8080/api/v1/schema/swagger-ui/

Redoc: http://localhost:8080/api/v1/schema/redoc/

Monitoring Tasks 🕵️
Since we use Celery for background tasks (like the daily interest calculation), you can monitor them using Flower:

Flower Dashboard: http://localhost:5555

Testing Emails 📧
We use Mailpit to catch emails locally so you don't spam real addresses.

Mailpit Interface: http://localhost:8025

📂 Project Structure
The project follows a "Core Apps" structure to keep things organized:

bank-server/
├── config/             # Project settings (base, local, production)
├── core_apps/          # The heart of the application
│   ├── accounts/       # Bank accounts, transactions, currency logic
│   ├── cards/          # Virtual card management
│   ├── common/         # Shared utilities (TimeStampedModel, etc.)
│   ├── user_auth/      # Custom User model, login, security questions
│   └── user_profile/   # Extended profiles, Next of Kin, Photos
├── docker/             # Dockerfiles and entry scripts
└── requirements/       # Python dependencies
