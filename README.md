To Run this project in local:

1. Create a python virtual environment and activate it
2. Clone this repo
3. Goto api folder inside repoitory
4. install requirements (pip install -r requirements.txt)
5. start server (python manage.py runserver)

API ENDPOINT - /api/get_repos/<org_name>?n=2&m=3

If m or n is not provided it'll by default return top 5 results.

Deployed app endpoint : https://testappalmabase.herokuapp.com/api/get_repos/<org_name>?n=5&m=3