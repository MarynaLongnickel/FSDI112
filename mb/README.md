# Important notes for Django Projects

1. Open terminal and create a folder to store the project.
2. Move to the respective folder (make sure that you are on the right location)
3. Create a virtual environment (WIN: python -m venv venv or MAC: python3 -m venv venv)
4. After the creation we hace to activate our virtual environment (WIN:
   venv\Scripts\activate or MAC: source venv/bin/activate)
5. Install django (WIN: pip install django or MAC: pip3 install django)
6. Create the project (django-admin startproject config .)
7. Create the structure for the project
   - Create the static, templates, img, css, js folders
   - Create the .gitignore, README.md

# Additional Notes

- All of the subcommands for django are going to be called followed by python (or python3)
  manage.py (e.g. python manage.py runserver)
- If we want to check the full list, we can run python manage.py
- To create an app we need to run "python manage.py startapp NAME_OF_THE_APP" (remember to
  change NAME_OF_THE_APP for the actual name)
