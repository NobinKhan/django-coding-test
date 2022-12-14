# Django-Coding-Test
steps
1. Pull latest from this repo

2. Install poetry in your pc (dont't install if already installed). If dont't want to use poetry then setup a classical Virtual environment and install dependency from requirements.txt provided (In src directory).

3. Run "poetry install" to install all dependency.(It will create virtual environment automatically)

4. To generate requirements.txt run "poetry export --without-hashes -f requirements.txt --output requirements.txt" this in src directory.

5. To run project run "poetry run python manage.py runserver" or "poetry shell" to activate poetry virtual environment and then run normal python commands to run the project.