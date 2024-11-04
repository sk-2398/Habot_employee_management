# Habot Employee Management

A Django-based web application for managing employees.

## Features

- User Authentication (Login/Signup)
- CRUD operations for employees

## Prerequisites

- Python 3.x
- Django
- Virtualenv

## Installation

### Clone the Repository

```bash
git clone https://github.com/sk-2398/Habot_employee_management
cd employee_management
```
### Create and Activate a Virtual Environment
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the Server
```bash
python manage.py runserver
```
It will run this project on localhost.
Visit http://127.0.0.1:8000/ to access the apis.
