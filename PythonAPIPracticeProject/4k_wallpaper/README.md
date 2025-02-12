# Steps to run project:

- Download this project folder

- Create a virtual environment at project root (Optional)

- Install packages: `pip install -r requirements.txt`

- Mock the database: `python3 manage.py recreatedb.py` (Optional)

- Run server: `python3 manage.py runserver`

- Go to URL: `localhost:8000`

- Enter the following login details if the database has mock data:
    - Email: sohamjobanputra7@gmail.com
    - Password: soham@123

- To create custom login: `python3 manage.py createsuperuser`
