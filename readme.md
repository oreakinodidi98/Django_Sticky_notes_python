# Django part 2

## Agenda

Create a Django Project
2. Create a Django app
3. Implement Model and Logic
4. Implement forms, data handling
5. Retrieve data from both Template view

## process

- python -m venv venv
- . .\venv\Scripts\Activate
- pip install django
- pip list
- pip freeze > requirements.txt
- **create DJANGO project ->** django-admin startproject sticky_notes .
- run server -> python manage.py runserver
- folder structure
  - settings.py -> settings of application
  - urls.py ->  path
- **create DJANGO app ->**django-admin startapp sticky_notes_app
- in project -> settings -> INSTALLED_APPS -> add name of application E.G sticky_notes

## run project

- start Project:
```py project_name.py runserver```
```python manage.py makemigrations```
```python manage.py migrate```

- add urls.py to apps folder
  - import views.py from app directory
- modify views.py in apps folder
- modify urls.py in project folder
- add models.py in app folder
- add forms.py in app folder

## default user model

![default user model](image.png)
![auth backend](image-1.png)
![settings.py file](image-2.png)
![registration view](image-3.png)

``` py
from django.contrib.auth.models import User

# creeating a new user 
user = User.object.create_user(username='ore', password='password123')

# updating user infformation 
user.email ='ore@example.com'
user.saave()
```
## set up URLs

- creat URLS.py in app folder
- import include, path
- Add a URL to urlpatterns as shown in example
- this URL will be for the APP

## creeate templates

- create templates folder in app folder
- create auth app
  - inside create partials folder -> HTML that not a full page
  - e.g. header and footer

## create forms

- in app folder create forms.py

## create views

- in app folder create views
- import forms

## URL

- import url for registration page
- import from.views

## Make migrations

- ```python manage.py makemigrations```
- ```python manage.py migrate```
- create super user
- ```python manage.py createsuperuser```
- start Project:
```py manage.py runserver```

## create artifact

- pip install build
- pthon -m build
- python setup.py sdist bdist_wheel
- create a .pypirc file
- create a .toml file
- create a setup.py & setup.cfg file
  
- [packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [configuration](https://pip.pypa.io/en/latest/topics/configuration/)
- [toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml)
- [pip](https://pip.pypa.io/en/stable/cli/pip_install/)

## Unit Testing

- Unit testing is a software-testing approach that focuses on testing individual components (such as classes, functions, or modules) in isolation to ensure they perform as intended
- A unit = class, function or a module
- Unit tests are automated, executed frequently during development, and provide early detection of defects.
- The primary goal is to detect defects early in the development process by automating tests and executing them frequently.
- **TDD = Test-Driven Development**

## Principles of Unit Testing

- **Arrange-Act-Assert (AAA)**
- AAA is a pattern for organising and structuring unit tests.It is sometimes also called “Given-When-Then”.
- Components:
- **Arrange**: Set up the necessary preconditions and inputs.
  - arrange values that i want to test
  - these values are repeted and reinitialised for every test
- **Act**: Perform the action or behaviour being tested.
  - store result in variables
- **Assert**: Verify that the outcome is as expected.
  - expected behaviur occured
- Given -> when -> then
- **FIRST** Principle :  acronym representing the key principles of effective unit tests
- Components:
- **Fast**: Tests should run quickly to provide rapid feedback
- **Isolated/Independent**: Tests should not depend on each other to ensure isolation.
- **Repeatable**: Tests should produce consistent results when executed repeatedly.
- **Self-Validating**: Tests should have a clear pass/fail outcome without manual interpretation.
- **Timely**: Tests should be written in a timely manner, preferably before the code.

Example:

``` py
# todo_list.py
class TodoList:

    def __init__(self):
        # Initialise an empty list to store tasks
        self.tasks = []
    
    def add_task(self, task):
        # Add a new task to the list
        self.tasks.append(task)
        
    def update_task(self, old_task, new_task):
        # Update an existing task in the list
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
    
    def remove_task(self, task):
        # Remove a task from the list
        if task in self.tasks:
            self.tasks.remove(task)
```

Test cases:

```py
import unittest
#The TodoList class, which represents the functionality to be tested, is in a separate file (todo_list.py), promoting modularity
from todo_list import TodoList

#The TodoList class is imported into the test file (test_todo_list.py), allowing access for testing

class TestTodoList(unittest.TestCase):
    def setUp(self):
        # Create a new TodoList instance before each test
        self.todo_list = TodoList()

    def test_add_task(self):
        # Test if add_task method correctly adds a task
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.tasks, [])
        #A failing test case is intentionally created in the test_add_task method by checking for the incorrect tasks list after adding a task

    def test_update_task(self):
        # Test if update_task method correctly updates an existing task
        self.todo_list.add_task("Task 1")
        self.todo_list.update_task("Task 1", "Updated Task 1")
        self.assertEqual(self.todo_list.tasks, ["Updated Task 1"])

    def test_remove_task(self):
        # Test if remove_task method correctly removes a task
        self.todo_list.add_task("Task 1")
        self.todo_list.remove_task("Task 1")
        self.assertEqual(self.todo_list.tasks, [])

if __name__ == '__main__':
    unittest.main()

#The TestTodoList class inherits from unittest.TestCase, and each test is a test-case method
```

## How to Run tests

- Create a Test suite

```py
# test_suite.py
import unittest
from test_todo_list import TestTodoList

suite = unittest.TestLoader().loadTestsFromTestCas(TestTodoList) unittest.TextTestRunner().run(suite)
```

- unit = behaviour of our program -> not each function but the feature that works togethere
- refacturing = making code better without changing function of the code
- 