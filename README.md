# CapstoneApp - CastingAgency

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies in this directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## API Reference

This chapter gives a detailed documentation about the API endpoints and their expected behavior.

### Endpoints

- GET '/actors'
- GET '/questions?page=${integer}'
- GET '/categories/${integer}/questions?page=${integer}'
- POST '/questions'
- POST '/quizzes'
- DELETE '/questions/${integer}'


#### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs, and success information
```
{
    'categories': { 
        '1' : "Science",
        '2' : "Art",
        '3' : "Geography",
        '4' : "History",
        '5' : "Entertainment",
        '6' : "Sports" 
    },
    'success': true
}
```

## Running the server

From within this directory first ensure you are working using your created virtual environment. 
Uncomment the line `db_drop_and_create_all()` on the initial run to initialize the database and to setup the tables in the database.
Before that, please ensure that you create your PostgreSQL database and that you adjust all the environment variables (e.g. `DATABASE_URL`) on your OS. The required environment variables are listed in the setup.sh script.

To run the server, execute:

Linux:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Windows PowerShell:
```bash
$env:FLASK_APP="app.py"
$env:FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 


## Testing
To run the tests, run

Linux:
```bash
dropdb capstoneapp_test
createdb capstoneapp_test
psql capstoneapp_test < database_dump
python test_app.py
```