import os
import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from database.models import setup_db, db_drop_and_create_all, Actor, Movie
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
    @uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    #db_drop_and_create_all()
    
    """
    CORS Headers
    after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/greeting', methods=['GET'])
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting



    # ROUTES

    """
    Check if app is running
    """
    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy")



    '''
    ACTOR ROUTES
    '''

    '''
        GET /actors endpoint: view all actors 
        authorized for all Casting Agency roles 
    '''
    @app.route('/actors', methods=['GET'])
    #@requires_auth('get:actors')
    def get_actors():
        
        actors = Actor.query.order_by(Actor.id).all()

        # if no actors were found:
        if not actors:
            abort(404)

        try:
            actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actors
            })

        except BaseException:
            abort(422)


    '''
        POST /actors endpoint: add a new actor 
        authorized for roles "Casting Director" and "Executive Producer"
    '''
    @app.route('/actors', methods=['POST'])
    #@requires_auth('post:actors')
    def create_actor():

        try:
            data = request.get_json()

            actor = Actor(
                name=data.get('name'),
                age=data.get('age'),
                gender=data.get('gender')
            )
            actor.insert()

            return jsonify({
                'success': True,
                'actors': actor.format()
            }), 200

        except BaseException:
            abort(422)


    '''
        PATCH /actors endpoint: modify an actor 
        authorized for roles "Casting Director" and "Executive Producer"
    '''
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    #@requires_auth('patch:actors')
    def update_actor(actor_id):

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        # if no actor was found:
        if not actor:
            abort(404)

        try:
            data = request.get_json()

            if 'name' in data:
                actor.name = data.get('name')

            if 'age' in data:
                actor.age = data.get('age')

            if 'gender' in data:
                actor.gender = data.get('gender')

            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            }), 200

        except BaseException:
            abort(422)


    '''
        DELETE /actors endpoint: remove an actor 
        authorized for roles "Casting Director" and "Executive Producer"
    '''
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    #@requires_auth('delete:actors')
    def delete_actor(actor_id):

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        
        # if no actor was found:
        if not actor:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                'success': True,
                'delete': actor_id
            }), 200

        except BaseException:
            abort(422)



    '''
    MOVIE ROUTES
    '''

    '''
        GET /movies endpoint: view all movies 
        authorized for all Casting Agency roles 
    '''
    @app.route('/movies', methods=['GET'])
    #@requires_auth('get:movies')
    def get_movies():
        
        movies = Movie.query.order_by(Movie.id).all()

        # if no moves were found:
        if not movies:
            abort(404)

        try:
            movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': movies
            })

        except BaseException:
            abort(422)


    '''
        POST /movies endpoint: add a new movie 
        only authorized for role "Executive Producer"
    '''
    @app.route('/movies', methods=['POST'])
    #@requires_auth('post:movies')
    def create_movie():

        try:
            data = request.get_json()

            movie = Movie(
                title=data.get('title'),
                release_date=data.get('release_date')
            )
            movie.insert()

            return jsonify({
                'success': True,
                'movies': movie.format()
            }), 200

        except BaseException:
            abort(422)


    '''
        PATCH /movies endpoint: modify a movie
        authorized for roles "Casting Director" and "Executive Producer"
    '''
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    #@requires_auth('patch:movies')
    def update_movie(movie_id):

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        # if no movie was found:
        if not movie:
            abort(404)

        try:
            data = request.get_json()

            if 'title' in data:
                movie.title = data.get('title')

            if 'release_date' in data:
                movie.release_date = data.get('release_date')

            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200

        except BaseException:
            abort(422)



    '''
        DELETE /movies endpoint: remove a movie
        only authorized for role "Executive Producer"
    '''
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    #@requires_auth('delete:movies')
    def delete_movie(movie_id):

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        
        # if no movie was found:
        if not movie:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200

        except BaseException:
            abort(422)






    '''
    error handlers for AuthError and aborts
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        return jsonify({
            "success": False,
            "error": ex.status_code,
            "message": ex.error
        }), ex.status_code


    return app

app = create_app()

if __name__ == '__main__':
    app.run()