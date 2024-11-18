# Parking Management System
## This project is a Parking Management System developed with Django that allows users to manage parking areas and vehicle statuses.

### Requirements
 - Python 3.10 or later
 - Django 5.0.3 or later
 - MySQL or MariaDB database
 - Other dependencies can be installed via requirements.txt

## Installation
### 1. Clone the repository :
       git clone https://github.com/yourusername/parking_management.git
       cd parking_management
### 2. Create a virtual environment (optional but recommended) :
        python -m venv venv
        source venv/bin/activate  # For Linux/Mac
        venv\Scripts\activate     # For Windows
### 3. Install dependencies :
       pip install -r requirements.txt
### 4. Set up the database :
- Update your database settings in settings.py under the DATABASES section.
- Ensure the MySQL or MariaDB database is running.
### 5. Apply migrations : 
       python manage.py migrate
### 6. Create a superuser to access the admin panel :
       python manage.py createsuperuser
- Follow the prompts to set the username, email, and password for the superuser.

## How to Log In
### 1. Run the development server :
      python manage.py runserver
### 2. Open your browser and go to :
      http://127.0.0.1:8000/admin
### 3. Log in using the superuser credentials you created in the previous step (username and password).
### 4. You will now have access to the Django admin panel to manage parking areas, vehicles, and other data.
- Example Credentials (for development):
- Username: admin
- Password: password123

## License
- This project is licensed under the MIT License - see the LICENSE file for details.


       
