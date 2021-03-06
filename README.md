# CapstoneApp - CastingAgency

## Capstone Project of Udacity Nanodegree Full Stack Web Developer

This project is about a Casting Agency modeling a company that is responsible for creating and managing actors and movies. There are different roles within the company who are having different permissions for interacting with the company's application. 

The application is hosted on the following URL (deployed on Heroku): https://cems-casting-agency.herokuapp.com

When running the app locally: http://localhost:5000 or  http://127.0.0.1:5000

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

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
The application requires authentication and authorization to perform various actions. The endpoints require different permissions that are passed with `Bearer` Token. 

There are three different roles: 

- Casting Assistant
    - Can view actors and movies (`get:actors`, `get:movies`)
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database (`post:actors`, `delete:actors`)
    - Modify actors or movies (`patch:actors`, `patch:movies`)
- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database (`post:movies`, `delete:movies`)



### Endpoints

- GET '/actors'
- POST '/actors'
- PATCH '/actors'
- DELETE '/actors'

- GET '/movies'
- POST '/movies'
- PATCH '/movies'
- DELETE '/movies'


#### GET '/actors'
- Fetches a list of actors with the id, name, age and gender of each actor
- Request Arguments: None
- Returns: An object with a list of actors sorted by the id, and success information
```
{
    'actors': [
        { 
            'id' : '1',
            'name' : 'John Doe',
            'age' : 25,
            'gender' : 'm'
        },
        { 
            'id' : '2',
            'name' : 'Jane Doe',
            'age' : 25,
            'gender' : 'w'
        }
    ],
    'success': true
}
```

#### POST '/actors'
- Sends a post request in order to add a new actor
- Request Body:
```
{
    'name":'John Doe',
    'age':25,
    'gender':'m'
}
```
- Returns: Returns an object of the added actor with the created id, name, age and gender, and the success information
```
{
    'actors': [
        { 
            'id' : '1',
            'name' : 'John Doe',
            'age' : 25,
            'gender' : 'm'
        },
    ],
    'success': true
}
```

#### PATCH '/actors/${integer}'
- Sends a patch request in order to update an existing actor
- Request Arguments: id - integer
- Request Body:
```
{
    "name":'John Doe',
    "age":25,
    "gender":'m'
}
```
- Returns: Returns an object of the updated actor, and the success information
```
{
    'actors': [
        { 
            'id' : '1',
            'name' : 'John Doe',
            'age' : 25,
            'gender' : 'm'
        },
    ],
    'success': true
}
```

#### DELETE '/actors/${integer}'
- Sends a delete request in order to remove an existing actor
- Request Arguments: id - integer
- Returns: Returns an object with id of the deleted actor, and the success information
```
{
    'delete': 1,
    'success': true
}
```


#### GET '/movies'
- Fetches a list of movies with the id, title and release_date of each movie
- Request Arguments: None
- Returns: An object with a list of movies sorted by the id, and success information
```
{
    'movies': [
        { 
            'id' : '1',
            'title' : 'Titanic',
            'release_date' : 'Thu, 08 Jan 1998 00:00:00 GMT'
        },
        { 
            'id' : '2',
            'title' : 'Pulp Fiction'',
            'release_date' : 'Thu, 03 Nov 1994 00:00:00 GMT'
        }
    ],
    'success': true
}
```

#### POST '/movies'
- Sends a post request in order to add a new movie
- Request Body:
```
{ 
    'title' : 'Titanic',
    'release_date' : '01.08.1998'
}
```
- Returns: Returns an object of the added movie with the created id, title and release_date, and the success information
```
{
    'movies': [
        { 
            'id' : '1',
            'title' : 'Titanic',
            'release_date' : 'Thu, 08 Jan 1998 00:00:00 GMT'
        },
    ],
    'success': true
}
```

#### PATCH '/movies/${integer}'
- Sends a patch request in order to update an existing movie
- Request Arguments: id - integer
- Request Body:
```
{ 
    'title' : 'Titanic',
    'release_date' : '01.08.1998'
}
```
- Returns: Returns an object of the updated movie, and the success information
```
{
    'movies': [
        { 
            'id' : '1',
            'title' : 'Titanic',
            'release_date' : 'Thu, 08 Jan 1998 00:00:00 GMT'
        },
    ],
    'success': true
}
```

#### DELETE '/movies/${integer}'
- Sends a delete request in order to remove an existing movie
- Request Arguments: id - integer
- Returns: Returns an object with id of the deleted movie, and the success information
```
{
    'delete': 1,
    'success': true
}
```


### Error handling

The API will return the following error responses based on the request failures:

    400: Bad Request
    401: Unauthorized
    404: Not Found
    422: Unprocessable Entity
    500: Internal Server Error


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