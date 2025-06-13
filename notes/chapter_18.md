# Getting Started with Django

## Setting Up a Project

- Creating and activating a virtual environment

  ```bash
    $ python -m venv env # creates a virtual env
    $ source env/Scripts/activate # activates the env
  ```

  A virtual environment is an solated Python workspace for project-specific dependencies.

- Creating a project in Django

  ```bash
  $ django-admin startproject projectname .
  ```

  The command creates a new Django project in the current directiory (the `.` means "current directory."):

  ```bash
    current_dir/
    ├── manage.py       <- Command-line tool for interacting with the project
    └── projectname/
        ├── __init__.py  <- Marks project as a Python package
        ├── settings.py  <- Contains all project configurations
        ├── urls.py      <- Defines URL routes for the entire project
        ├── asgi.py      <- ASGI config for async web servers
        └── wsgi.py      <- WSGI config for traditional servers
  ```

- Creating/Modifying a database

  ```bash
  $ python manage.py migrate
  ```

  Issuing the `migrate` command for the first creates a `db.sqlite3` file in the project root and sets up the default database tables.

- Creating an app in Django

  ```bash
  $ python manage.py startapp appname
  ```

  The command creates a new Django app—a self-contained, reusable module for specific functionality—with boilerplate files in the project's root directory.

  ```bash
  root_dir/
  └── appname/
      ├── __init__.py      ← Marks the folder as a Python package.
      ├── admin.py         ← Register models for Django’s admin panel.
      ├── apps.py          ← Contain app-specific configurations
      ├── models.py        ← Define database tables (models).
      ├── tests.py         ← Write unit tests for the app.
      ├── views.py         ← Handle HTTP requests.
      └── migrations/      ← Stores database migration files.
  ```

- To integrate an app into a Django project, it must be added to the `INSTALLED_APPS` list in the project's `settings.py` file.

- Activating Models

  ```bash
  $ python manage.py makemigrations appname # Create migrations
  $ python manage.py migrate # Apply to DB
  ```

  The `makemigrations` command creates files in` appname/migrations/` that record changes made to the models, so the database can be updated to match.

  The `migrate` command then reads those migration files and executes the necessary SQL commands to apply the changes to the project's database.

- Setting Up a Superuser

  ```bash
  $ python manage.py createsuperuser
  ```

  The command creates a superuser—admin account with full control over the entire Django project—for Django’s admin panel.

- The Django shell

  The Django shell is an interactive Python environment pre-loaded with a Django project's settings, models, and configurations.

  - Lauching the Django shell

    ```bash
    $ python manage.py shell
    ```

  - Acessing model objects

    ```bash
    >>> modelname.objects.get(id=n) # Returns model object of id 'n'
    >>> modelname.objects.all() # Returns all modelname objects
    ```

  - Acessing related model objects

    ```bash
    >>> ModelA.ModelB_set.all()
    ```

    The command retrives all related `ModelB` objects linked to a `ModelA` instance through a reverse foreign key relationship

- Making web pages with Django consists of three stages: defining URLs, writing views, and writing templates.

  Defining URLs involve mapping a web address (URL pattern) to a specific view function in `urls.py`.

  ```python
  urlpatterns = [
  path('', views.index), # maps 'mysite/' to the `index` view function
  ]
  ```

  Views are functions or classes that handle requests and returns responses (HTML, JSON, etc)

  ```python
  def index(request):
    """return the 'index.html' template"""
    return render(request, 'templates/index.html')
  ```

  Templates are HTML files with placeholders user to render dynamic content from the views.