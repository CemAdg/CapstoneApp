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

    """
    Testing APIs for actors
    """

    # Test creating a new actor with correct permissions
    def test_01_create_actor_as_director(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actors', data)

    def test_02_create_actor_as_producer(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actors', data)

    # Test creating a new actor with missing permissions fails

    def test_03_403_create_actors_with_wrong_permission(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test creating a new actor with wrong inputs fails
    def test_04_422_create_actors_with_wrong_inputs(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "title": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test requesting actors successfully with token

    def test_05_get_actors_with_token(self):
        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actors', data)

    # Test failing requesting actors without token

    def test_06_401_get_actors_without_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(
            data["message"]["description"],
            "Authorization Header is required.")

    # Test unauthorized updating of an actor

    def test_07_403_update_actors_with_wrong_permission(self):
        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test updating an actor that does not exist
    def test_08_404_update_not_existing_actor(self):
        res = self.client().patch('/actors/99', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test authorized updating of an actor

    def test_09_update_actors_with_correct_inputs(self):
        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "name": "John Doe",
            "age": 25,
            "gender": "m"
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actors', data)

    # Test updating an actor with wrong inputs
    def test_10_422_update_actor_with_wrong_inputs(self):
        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "name": "John Doe",
            "age": "twentyfive",
            "gender": "m"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test unauthorized deleting of an actor

    def test_11_403_delete_actors_with_missing_permissions(self):
        res = self.client().delete('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test deleting of an actor that does not exist
    def test_12_404_delete_not_existing_actor(self):
        res = self.client().delete('/actors/99', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test authorized deleting of an actor
    def test_13_delete_actors_with_correct_inputs(self):
        res = self.client().delete('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('delete', data)
        self.assertEqual(data['delete'], 1)

    # Test authorized deleting of an actor
    def test_14_delete_actors_with_correct_inputs(self):
        res = self.client().delete('/actors/2', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('delete', data)

    """
    Testing APIs for movies
    """

    # Test creating a new movie with correct permissions
    def test_15_create_movie_as_producer(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('movies', data)

    def test_16_create_movie_as_producer(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic 2",
            "release_date": "08.01.1998"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('movies', data)

    # Test creating a new movie with missing permissions fails
    def test_17_403_create_movies_with_wrong_permission(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test creating a new movie with wrong inputs fails
    def test_18_422_create_movies_with_wrong_inputs(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test requesting movies successfully with token
    def test_19_get_movies_with_token(self):
        res = self.client().get('/movies', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('movies', data)

    # Test failing requesting movies without token
    def test_20_401_get_movies_without_token(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(
            data["message"]["description"],
            "Authorization Header is required.")

    # Test unauthorized updating of a movie
    def test_21_403_update_movies_with_wrong_permission(self):
        res = self.client().patch('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test updating a movie that does not exist
    def test_22_404_update_not_existing_movies(self):
        res = self.client().patch('/movies/99', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test updating a movie with wrong inputs
    def test_23_422_update_movies_with_wrong_inputs(self):
        res = self.client().patch('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic",
            "release_date": ""
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test authorized updating of a movie as director
    def test_24_update_movies_with_correct_inputs(self):
        res = self.client().patch('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.casting_director_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('movies', data)

    # Test authorized updating of a movie as producer
    def test_25_update_movies_with_correct_inputs(self):
        res = self.client().patch('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        }, json={
            "title": "Titanic",
            "release_date": "08.01.1998"
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('movies', data)

    # Test unauthorized deleting of a movie
    def test_26_403_delete_movies_with_missing_permissions(self):
        res = self.client().delete('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.casting_assistant_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test deleting of a movie that does not exist
    def test_27_404_delete_not_existing_movies(self):
        res = self.client().delete('/movies/99', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    # Test authorized deleting of an movie
    def test_28_delete_movies_with_correct_inputs(self):
        res = self.client().delete('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('delete', data)

    # Test authorized deleting of an movie
    def test_29_delete_movies_with_correct_inputs(self):
        res = self.client().delete('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.executive_producer_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('delete', data)
        self.assertEqual(data['delete'], 2)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
