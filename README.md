# Department
Assignment.

## Project Overview

Assignment

## Getting Started

Explain how to set up and run the project on a local development environment.

### Prerequisites

List the prerequisites required to run the project. This may include things like:

- Python Python 3.10.12
- Django 4.2.5
- DjangoRestFramework 3.14.0

### Database

Default Datbase: No outsid requirement, sqlite will for for now.

# Clone the repository
git clone https://github.com/deepakbartwal/department.git

# Change into the project directory
cd department

# Install dependencies
pip install -r requirements.txt

# Perform database migrations
python manage.py makemigrations
python manage.py migrate

# Create sample data
open shell using following commands
- python manage.py shell
run following python code in the shell
- form core.create_data import create_data
- crearte_data()
- exit()

# Start the development server
python manage.py runserver
