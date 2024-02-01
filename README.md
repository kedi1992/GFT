# User Management SPA

This project for user management, built with Django (backend) and JavaScript (frontend).

## Technologies Used

- **Django:** Web framework for the backend.
- **Open API Specification:** Defines the backend REST APIs.
- **Docker:** Used for containerizing the application.
- **GitHub:** Source code repository.

## Getting Started

### Prerequisites

- Docker installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kedi1992/GFT.git
    cd services
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose down
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose up --build
    ```

3. Visit http://localhost:8000 in your browser.

## API Endpoints

### 1. User Registration

- **Endpoint:** `http://127.0.0.1:8000/user/api/register/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "user name",
    "email": "test@example.com",
    "password": "your_secure_password",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "phone_number": "1234567890"
  }
- **Response:** 
1. Successful registration returns a JSON response with the user details.
2. In case of any validation errors (e.g., duplicate username, invalid email), appropriate error messages are returned.

### 2. Get Token

- **Endpoint:** `http://127.0.0.1:8000/user/api/token/`
- **Method:** `GET`
- **Request Body:**
  ```json
  {
    "username": "user name",
    "password": "your_secure_password",
  }
- **Response:** 
1.Successful login returns a JSON response with an access token.
2.In case of invalid credentials or other issues, appropriate error messages are returned.

### 2. User Logout

- **Endpoint:** `http://127.0.0.1:8000/user/api/logout/`
- **Method:** `POST`
- **Request Body:**
  (No request body is required for logout)
- **Response:** 
1. Successful logout returns a JSON response indicating the successful logout.
2. In case of any issues (e.g., user not authenticated), appropriate error messages are returned.
