# Library Management System

## Project Overview
This is a **Library Management System** built using Django and Django REST Framework (DRF). It allows users to browse books, borrow available books, return borrowed books, and manage user authentication.

## Features
- **User Authentication** (Signup, Login, Logout)
- **Role-based Access Control** (Admin, Librarian, Member)
- **Book Management** (Add, Update, Delete, View books)
- **Borrow & Return System**
- **Book Reviews & Ratings**
- **Cart & Order Management**
- **API Documentation** using Swagger

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd library-management
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the server:
   ```sh
   python manage.py runserver
   ```
7. Access the API documentation at:
   ```
   http://127.0.0.1:8000/swagger/
   ```

## API Endpoints

### Authentication
- `POST /auth/users/` - Register a new user
- `POST /auth/token/login/` - Login and get JWT token
- `POST /auth/token/logout/` - Logout user

### User Management
- `GET /users/` - List all users
- `GET /users/{id}/` - Retrieve user details

### Book Management
- `GET /books/` - List all books
- `GET /books/{id}/` - Retrieve a book
- `POST /books/` - Add a new book (Admin/Librarian)
- `PUT /books/{id}/` - Update book details (Admin/Librarian)
- `DELETE /books/{id}/` - Delete a book (Admin/Librarian)

### Borrow & Return
- `POST /borrow/` - Borrow a book
- `POST /return-book/` - Return a borrowed book
- `GET /borrow/` - View borrowed books

### Reviews
- `POST /reviews/` - Add a review
- `GET /reviews/` - List all reviews

## Usage Guide
1. **User Registration & Login**
   - Use `/auth/users/` to register a new account.
   - Use `/auth/token/login/` to get a JWT token.
   - Include the token in headers for authentication: `Authorization: Bearer <token>`.

2. **Borrowing a Book**
   - Find an available book from `/books/`.
   - Send a `POST` request to `/borrow/` with the book ID.

3. **Returning a Book**
   - Send a `POST` request to `/return-book/` with the book ID.

4. **Managing Books**
   - Admins and Librarians can add, update, or delete books.

## Models Overview

### Users
- **CustomUser**: Extends Django's `AbstractUser`, adding roles (Admin, Librarian, Member).

### Books
- **Book**: Stores book information (title, author, genre, price, availability).
- **Genre & Author**: Categorization models.
- **BooksImage**: Stores book images.

### Borrowing System
- **Borrow**: Tracks book borrow status, due dates, and fines.
- **Return**: Manages book return dates and overdue fines.

### Reviews
- **Review**: Users can rate and comment on books.

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF), Djoser
- **Database**: PostgreSQL / SQLite
- **Authentication**: JWT (Djoser & SimpleJWT)
- **API Documentation**: DRF-YASG (Swagger)

## Dependencies
```sh
asgiref==3.7.2
certifi==44.0.2
cffi==1.15.1
charset-normalizer==3.1.0
cryptography==44.0.2
defusedxml==0.7.1
Django==5.1.7
django-debug-toolbar==5.0.1
django-filter==25.1
djangorestframework==3.15.2
djangorestframework_simplejwt==5.5.0
djoser==2.3.1
drf-nested-routers==0.94.1
drf-yasg==1.21.10
idna==3.10
inflection==0.5.1
Markdown==3.7
oauthlib==3.2.2
packaging==24.2
pillow==11.1.0
pip==25.0.1
pycparser==2.22
PyJWT==2.9.0
python3-openid==3.2.0
pytz==2025.1
PyYAML==6.0.2
requests==2.32.3
requests-oauthlib==2.0.0
social-auth-app-django==5.4.3
social-auth-core==4.5.6
sqlparse==0.5.3
tzdata==2025.1
uritemplate==4.1.1
urllib3==2.3.0
```

## License
This project is open-source and available for modification.

