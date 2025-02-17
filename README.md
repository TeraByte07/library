# e_library
Library Management System
This project is a Library Management System built using Django and Django REST Framework. It allows users to register, borrow, and return books, while admins can manage books and user activities.

Features
User Registration & Authentication: Users can register, login, and logout.
Borrowing Books: Users can borrow books, and the system keeps track of borrowed and available books.
Returning Books: Users can return books before or on the due date.
Admin Management: Admins can manage users, books, and view all borrowed books.
Filtering: Books can be filtered by category and publisher.
Unit Testing: Includes unit tests for user authentication, borrowing, and returning books.
Tech Stack
Backend: Django, Django REST Framework
Database: SQLite (default for development), but configurable to other databases (e.g., PostgreSQL, MySQL)
Authentication: Token-based authentication using Django REST Framework's Token Authentication.
Models
User: Custom user model (customUser) with additional fields like first name, last name, and email.
Book: Represents a book with fields like title, author, ISBN, category, publisher, etc.
Borrowed_books: Tracks the borrowing and returning of books by users, including return dates.
Installation
Prerequisites
Python 3.x
Django
Django REST Framework
Django Filter
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/library-management-system.git
Navigate to the project directory:

bash
Copy code
cd library-management-system
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run database migrations:

bash
Copy code
python manage.py migrate
Create a superuser (admin):

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Access the app at http://127.0.0.1:8000/ in your browser.

API Endpoints
User Authentication
Register: POST /signup/
Login: POST /login/
Logout: POST /logout/
Book Borrowing
Borrow Book: POST /books/borrow/<book_id>/
Return Book: POST /books/return/<book_id>/
Admin-only Endpoints
List All Borrowed Books: GET /borrowed_books/
Book Filtering
Filter books by category or publisher using query parameters:

bash
Copy code
GET /books/?category=fiction&publisher=test-publisher
Running Tests
The project includes unit tests to ensure the correct functionality of key components. To run the tests, use the following command:

bash
Copy code
python manage.py test
Future Improvements
Add frontend for easier access and usage of the system.
Enhance the admin dashboard with more analytics and insights.
Support notifications to users for overdue books.
Contributing
Feel free to fork this repository and submit pull requests if you'd like to contribute to the project.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit the changes (git commit -am 'Added a new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.# e_library
