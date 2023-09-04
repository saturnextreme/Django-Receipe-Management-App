# Recipe Management Django Project

Welcome to the Recipe Management Django Project! This project is designed to help you manage and organize your favorite recipes. You can add, edit, and delete recipes, as well as search for recipes by ingredients or keywords.

## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- Python 3.x
- pip (Python package manager)
- Git

## Getting Started

Follow these steps to get the Recipe Management Django Project up and running on your localhost:

# 1. Clone the Repository
git clone https://github.com/your-username/recipe-management-project.git

# 2. Create a Virtual Environment
cd recipe-management-project
python -m venv venv
source venv/bin/activate  # On macOS and Linux; On Windows, use: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Perform Database Migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a Superuser (Admin Account)
python manage.py createsuperuser
# Follow the prompts to set a username, email, and password for the admin account.

# 6. Run the Development Server
python manage.py runserver
# The application will be accessible at http://localhost:8000/ in your web browser.

# 7. Access the Admin Panel
# You can access the admin panel at http://localhost:8000/admin/ and log in with the superuser credentials you created earlier.
