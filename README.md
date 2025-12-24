Django Workshop: TaskMaster Project 🎓
Welcome to the Introduction to Django Framework workshop. This repository serves as the practical support for our 15-hour training session.

We will build TaskMaster, a collaborative task management tool that allows users to create tasks, assign them to people, and track their progress.

📚 Project Scope
The project focuses on the core concepts of Django through a simple but extensible domain model:

Person: Represents a user or an employee (Name, Email, Role).
Task: Represents a unit of work (Title, Description, Status, Due Date, Assigned To).
🛠 Prerequisites
Python 3.12+ installed.
Git installed.
Basic familiarity with terminal/command line.
Code Editor (VS Code or PyCharm).
🚀 Installation & Setup
You can set up the project using standard Python tools (pip) or the modern, high-speed installer (uv).

Option A: Standard Setup (pip)
Clone the repository:

git clone https://github.com/LindaOuer/DjangoWorkshop25.git
cd DjangoWorkshop25
Create a virtual environment:

# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Option B: Fast Setup (using uv)
If you want to test the speed of modern Python tooling:

Install uv (if not installed):

pip install uv
Create virtual environment:

uv init
uv venv
# Activate the environment (same as above)
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
Sync dependencies:

# Install packages instantly
uv sync
🆕 Manual Project Creation (Optional)
If you prefer to create the project structure from scratch to understand the initialization commands (instead of using the cloned starter code), follow these steps inside your active virtual environment:

Install Django:

pip install django
# OR if using uv
uv add django
Start the Project: We name the configuration folder config and create it in the current directory (.) to avoid nesting folders.

django-admin startproject config .
Create the Application: We will create an app named core to hold our models and logic.

python manage.py startapp core
Register the App: Open config/settings.py and add 'core' to the INSTALLED_APPS list so Django recognizes it:

INSTALLED_APPS = [
    # ... existing django apps ...
    'django.contrib.staticfiles',
    'core',  # <--- Add this line
]
⚙️ Running the Project
Once installed, perform the initial database migration and start the server:

Apply Migrations:

python manage.py migrate
Create a Superuser (Admin):

python manage.py createsuperuser
Run the Server:

python manage.py runserver
Access the App:

Website: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
🛤 Workshop Roadmap (Branches)
This repository is structured using Git branches to represent each step of the workshop. You can jump to any step using git checkout <branch-name>.

Branch	Description	Key Concepts
main	Initial setup and README	Environment, Git
step-01-setup	Django project structure created	django-admin, manage.py, settings.py
step-02-models	Task and Person models defined	ORM, Fields, ForeignKeys, Migrations
step-03-admin	Admin panel configuration	ModelAdmin, list_display, Filters
step-04-views	Basic Views and Templates	FBV, URL Routing, DTL (Templates)
step-05-forms	CRUD operations using Forms	ModelForm, CSRF, Validation
step-06-cbv	Refactoring to Class Based Views	ListView, CreateView, UpdateView, DeleteView
step-07-auth	User Authentication	Login/Logout, Permissions, Decorators
step-08-api	REST API with DRF	Serializers, JSON Endpoints
📝 Models Reference
For the workshop, we will be using the following schema in core/models.py:

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="tasks")

    def __str__(self):
        return self.title
