# Memo API - HFP Backend 🏥

This is the backend API for the **Health First Priority (HFP)** system. It is built with **Django** and serves as the central data storage and management hub, allowing the frontend to store and retrieve health records via RESTful API endpoints.

## 🚀 Features

* **API Endpoints:** Provides secure access points for storing health data.
* **Data Persistence:** Manages patient/user records using a relational database.
* **Admin Interface:** Built-in Django Admin for managing data directly.
* **Scalable Architecture:** Modular design using Django apps (e.g., `memos`).

## 🛠️ Tech Stack

* **Framework:** [Django](https://www.djangoproject.com/) (Python)
* **Database:** SQLite (Default) / PostgreSQL (Recommended for production)
* **API:** Django REST Framework (DRF) *[Assumed based on API usage]*

## ⚙️ Getting Started

Follow these instructions to get the backend running locally.

### Prerequisites

* Python 3.8+
* pip (Python package manager)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/waqar741/memo_api.git](https://github.com/waqar741/memo_api.git)
    cd memo_api
    ```

2.  **Create a Virtual Environment**
    It is best practice to keep dependencies isolated.
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**
    Set up the local database structure.
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin)**
    Access the admin panel to view data.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/`.

## 📖 API Documentation

* **Admin Panel:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* **API Root:** [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) *(Adjust route based on your `urls.py`)*

## 📂 Project Structure

```text
memo_api/
├── manage.py           # Django command-line utility
├── db.sqlite3          # Local development database
├── requirements.txt    # Python dependencies
├── memo_api/           # Project configuration settings
└── memos/              # Main application logic (models, views)

🤝 Contributing
Fork the repository.
Create a feature branch.
Commit your changes.
Push to the branch and open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Made with ❤️ by Waqar
