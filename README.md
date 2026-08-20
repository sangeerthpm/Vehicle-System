# Vehicle-System

Setup Steps
1. Create the Project Folder
Create a dedicated folder for the project.

2. Create a Virtual Environment
Create a Python virtual environment inside the project folder:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

The virtual environment keeps the project's Python dependencies isolated from other projects.

3. Create the Django Project and Apps
Create the Django project and the required applications:

django-admin startproject <project_name>

Create the required Django app:

python manage.py startapp <app_name>

Replace <project_name> and <app_name> with the actual names used in your project.

4. Register the App and Configure URLs
Add the created app to INSTALLED_APPS in settings.py.

Configure the application's URL routes and include the app's urls.py in the main project's urls.py.

5. Implement the Application Code
Add the application logic to views.py.

Define the required database models in models.py using Django's model system.

The models contain the fields and relationships required for the project.

Installation Guide
1. Activate the Virtual Environment
Before installing the project dependencies, activate the virtual environment.

Windows:

venv\Scripts\activate
2. Install Django
Install Django inside the activated virtual environment:

pip install django
This installs Django only for this project environment.

3. Install python-dotenv
The project uses a .env file to store configuration values such as secret keys and other environment-specific settings.

Install the python-dotenv package:

pip install python-dotenv
4. Install restframework
uses command 'pip install restframework'

4. Create the .env File
Create a .env file in the project's root directory.

Example:

SECRET_KEY=your-secret-key
DEBUG=True
The .env file keeps configuration values separate from the main Django source code.

Important: Do not upload the real .env file to GitHub. Add .env to .gitignore and use .env.example to provide sample values.

🗄️ Database Migrations
After creating or modifying the models in models.py, run Django's migration commands to create and apply the corresponding database changes.

1. Create Migrations
Run:

python manage.py makemigrations
This command detects changes made to the Django models and creates migration files describing those changes.

2. Apply Migrations
Run:

python manage.py migrate
This command applies the migration files to the database and creates or updates the required database tables.

Migration Workflow
Whenever you make changes to your models, use:

python manage.py makemigrations
python manage.py migrate
How to Run the Project
1. Activate the Virtual Environment
Make sure the virtual environment is activated:

venv\Scripts\activate
2. Start the Django Development Server
Run the following command:

python manage.py runserver
After running the command, Django will display a local development URL in the terminal, for example:

http://127.0.0.1:8000/
3. Open the Application
Copy the URL displayed in the terminal and open it in your web browser, such as Google Chrome.

The Django application will then be available in the browser.

Note: The URL or port may be different if Django is configured to use another port.

How to Test APIs
The project's APIs can be tested using either Postman or the Django REST Framework Browsable API.

Option 1: Test APIs Using Postman
Start the Django development server:
python manage.py runserver
Open Postman.

Enter the API endpoint URL.

Select the appropriate HTTP method, such as:

GET
POST
PUT
PATCH
DELETE
For POST, PUT, or PATCH requests, provide the required data in JSON format under the request body.

Send the request and check the API response.

Option 2: Test Using Django REST Framework
If Django REST Framework is configured in the project, open the API endpoint URL directly in the browser.

The Django REST Framework Browsable API provides an interface where you can:

View API responses
Send GET requests
Submit POST requests
Enter JSON or form data
Test API endpoints directly from the browser
Example:

http://127.0.0.1:8000/api/
The exact URL depends on the API routes configured in the project.

🔗 API Endpoint List
The following API endpoints are available in the project:

Method	URL	Purpose
GET	/api/vehicles/	List all vehicles
POST	/api/vehicles/	Add a new vehicle
GET	/api/vehicles/1/	Get details of a specific vehicle
PUT	/api/vehicles/1/	Update a specific vehicle
DELETE	/api/vehicles/1/	Delete a specific vehicle
GET	/api/bookings/	List all bookings
POST	/api/bookings/	Create a new booking
GET	/api/bookings/1/	Get details of a specific booking
Note: Replace 1 with the actual vehicle or booking ID when requesting a specific record.

Example
To get details of vehicle with ID 5:

GET /api/vehicles/5/
To get details of booking with ID 3:

GET /api/bookings/3/
📦 Sample JSON
Vehicle Response
Example response from the vehicles API:

[
    {
        "id": 1,
        "name": "Fortuner",
        "brand": "Toyota",
        "year": 2025,
        "price_per_day": "2500.00",
        "fuel_type": "Diesel",
        "is_available": true
    }
]
The vehicle has a daily rental price of ₹2,500.00 and is currently available for booking.

Booking Request
To create a booking, send a POST request to:

/api/bookings/
Example booking JSON:

 {
        "id": 4,
        "customer_name": "sangeerth",
        "customer_phone": "8714334546",
        "start_date": "2026-08-21",
        "end_date": "2026-08-24",
        "total_amount": "3000.00",
        "vehicle": 5
    },
Here, "vehicle": 1 refers to the vehicle with ID 1.

The start_date and end_date specify the booking period, which can be used to calculate the total rental amount based on the vehicle's price_per_day.
