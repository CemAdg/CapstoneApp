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
        GET /actors endpoint to view all actors 
        authorized for all Casting Agency roles 
    '''
    @app.route('/actors', methods=['GET'])
    #@requires_auth('get:actors')
    def get_actors():
        
        try:
            actors = Actor.query.all()
            if not actors:
                abort(404)
            actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actors
            })

        except BaseException:
            abort(422)


    '''
        POST /actors endpoint add a new actor 
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
    error handler for AuthError and aborts
    '''

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