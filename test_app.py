import os
import unittest
import json
import yaml
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import setup_db, Movie, Actor


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.casting_assistant_token = os.environ['casting_assistant_token']
        self.casting_director_token = os.environ['casting_director_token']
        self.executive_producer_token = os.environ['executive_producer_token']

        self.app = create_app()
        self.client = self.app.test_client

        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    
    def tearDown(self):
        """Executed after reach test"""
        pass


    # Test if actors are requested successfully with token
    def test_get_actors_with_token(self):
        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data))
        self.assertTrue(data["success"])
        self.assertIn('actors', data)
        self.assertTrue(len(data["actors"]))


    # Test if requesting actors fails without token
    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"]) 
        self.assertEqual(data["message"]["description"], "Authorization Header is required.")
    

    # Test if creating a new actor works with token



    # Test if creating a new actor with wrong inputs fails




    # Test if unauthorized creating of a new actor fails (RBAC for role Casting Assistant)
    


    # Test if unauthorized creating of a new movie fails (RBAC for role Casting Director)
    

    #   



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
