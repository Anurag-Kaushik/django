Project Setup

1. Setting Up the Environment

To set up this project on your local machine, follow the steps below:

Step 1: Install Virtualenv
Ensure you have virtualenv installed to create an isolated Python environment. If not, install it using the following command:

pip install virtualenv

Step 2: Create a Virtual Environment
Once virtualenv is installed, create a new virtual environment. You can name it venv or any other name you prefer:

python -m virtualenv venv

Step 3: Activate the Virtual Environment
Activate the virtual environment to isolate project dependencies:

On macOS/Linux:
source venv/bin/activate
On Windows:
venv\Scripts\activate

Step 4: Install Project Dependencies
Once the virtual environment is active, install the required dependencies from the requirements.txt file:

pip install -r requirements.txt

Step 5: Configure Environment Variables
Create a .env file in the root directory of the project to store your environment-specific variables (such as database credentials).

Important: Make sure to copy the contents of the .env.example file into .env and modify the values accordingly (e.g., database credentials, secret key).
Example:

DATABASE_USERNAME=your_database_username

2. Running Migrations

Before running the project, you need to apply the database migrations to create the necessary tables:

Step 1: Create Migrations
If migration files have not yet been created, run:

python manage.py makemigrations

Step 2: Apply Migrations
Apply the migrations to update the database schema:

python manage.py migrate

3. Starting Redis (macOS Example)

The application uses Redis as a message broker for Celery. Follow the steps below to install and start Redis on macOS. If you're using a different operating system, refer to your OS's documentation for the relevant Redis installation commands.

Step 1: Install Redis
Install Redis using Homebrew:

brew update
brew install redis

Step 2: Start Redis Server
Start the Redis server using the following command:

brew services start redis

4. Starting Celery

Step 1: Start Celery Worker
To run background tasks, you need to start a Celery worker. In the project root directory, use the following command to start the worker process:

celery -A catalyst_count worker --loglevel=info

This command tells Celery to use the celery.py configuration located at /catalyst_count/celery.py.

Running the Project

Once the environment is set up and all services are running, start the Django development server:

python manage.py runserver

The server will be accessible at http://localhost:8000/.

Application Overview

This application consists of several key web pages that serve different functionalities:

1. Login Page (/accounts/login/)
Purpose: Allows users to log in to the application using django-allauth.
Note: Users must be logged in before they can access other pages.
2. Upload Page (/)
Purpose: This page allows users to upload CSV files. A progress bar is displayed while the file is being processed.
Example File: Use the test_data.csv file as a sample for uploading.
3. Query Builder Page
Purpose: Users can use this page to query and filter the data in the system and view matching results.
Usage: After uploading data, users can query it and see the results based on the filters they apply.
Additional Information
Redis & Celery: Redis is used as the message broker for Celery to process background tasks such as file processing and querying large datasets asynchronously.
Django-allauth: This is used for user authentication and login management.
Make sure all services are running (Redis, Celery, and the Django server) to ensure smooth functionality of the application.

