import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from datetime import date
from models import setup_db, Actor, Movie, act_movies

casting_assistant_jwt = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDVjOGM2NTEwOGMzNWFlMGQzYzE0ZTMiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMTU2ODgsImV4cCI6MTY4OTAyMjg4OCwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.clnil1EP3QnYf3n2GDbK4rbWy_82cYt86pnapGR4W1ENuPLITD7yrSp4TpREEgi87k0uCNf15z4i3vEqNqhTumAYi4wITCJ4pw30nurdcyx56UXcXw5aLVZjfEDxWIUzCPEQnCcekjAs_2l86wUTgIIxhkMDyVr68D1P2A16giIlHjNTwoy-6cGgsstA4UL5SVGzNUd5E8dU7dF6Vr2Q5xqMwic92MG7xXOfVu8gwIIWlF5srrD0MK4PVXDFmxCsn7-qRMi47DBw30J4Z1hJAdQOtSXM86IycCWIfpmULE4Zn051xa4TWhHZ_aB5HpEvKkAFx4Jv9N3_I-r0J4vcLg'
casting_director_jwt = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDdiMzdiMWZjNjBjNTVlYTg2NDQ5OGMiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMTU3MzEsImV4cCI6MTY4OTAyMjkzMSwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.gBmISJsS_8M4EP7n-ysFmtB4yN0seJw3aGqjCiOl1DPOdJCTzy1aNiRQ8fmer-Ehejm_AQlTLMMMHU0fTB70HhUsqvJVRhU16YqmZ-cvfphHJcN1NRyk0CGaQxPFW9jrPo11U1t8e5GlB5KlN8SOLg1Gs2JQMSmFYWV4eiNJgOcYI9SsSL9WbGP-JpNLu_SP9xmhXzeB76KnSXELM5G8URFYm9qz7B7tLEgJQl2I3m-0oH-1PEL-4zYrtAa4JVNHdZKhKM8PvXVLTQFQfIARKfm8AvAACrfAQsx-6qeV4iHu4i-wKk9UrOpSRWIl3LczXn8dQsrYQxYeT3XjlOkxPw'
executive_producer_jwt = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDdiMzZlYmVkMTUzOWJlNGQxOWUxOWYiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMTU3NjAsImV4cCI6MTY4OTAyMjk2MCwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.E99yCWRlxdCxx-dDIxB9BuVmqEfqpWMONjzd4qnNPZRfErEMNxqkMbS98hI-labyoAOnBhOcFkPPo1l0OXlD8QcC0zCLCMTN_2Ymr0pcnkLgbRYDoMQKE3_Hn-ICl4MSsTOu5pf0EZQSc938QSuSjwMDW6f4MafkxBGXdnGkyBzBOO0uwHQk_p_T2--p0agaugivVegDlayUPazKDLL0O1iC_60vOfOoYX6Xvr_8HxGQOWTCtJMMWacSWhwU4AbvDZQHgNsa4YF-EMR007VFTYFh3LRvBKeCiDfteGjTyqHqPRsD8ayFXtfFgWAqqDqIGVhpnIGtj2tCWgZTSeb0RQ'

class CastingAgencyTestCase(unittest.TestCase):
  """This class represents the ___ test case"""

  def setUp(self):
    """Executed before each test. Define test variables and initialize app."""
    self.app = create_app()
    self.client = self.app.test_client
    self.database_path = 'postgres://buftwapmmeyhys:ef0ba4b52ffb3fd29a301bc617cb689f089d8673e0e721dd08f7761096e6b96e@ec2-52-2-167-43.compute-1.amazonaws.com:5432/d9961816q55imd'
    setup_db(self.app, self.database_path)

    self.new_actor = {
      'name': "Lola",
      'gender': 'Female',
      'age': 46
    }

    # binds the app to the current context
    with self.app.app_context():
        self.db = SQLAlchemy()
        self.db.init_app(self.app)
        # create all tables
        self.db.create_all()

  def tearDown(self):
    """Executed after reach test"""
    pass
  

  """GET METHODS"""


  def test_get_actors(self):
    res = self.client().get('/actors', headers = {'Authorization' : casting_assistant_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])


  def test_get_actors_with_error_401(self):
    res = self.client().get('/actors',  headers = {'Authorization' : casting_director_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Authorization header is expected.")


  def test_get_actors_with_error_404(self):
    res = self.client().get('/actors/4', headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Resource Not Found")


  def test_get_movies(self):
    res = self.client().get('/movies', headers = {'Authorization' : casting_assistant_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])


  def test_get_movies_with_error_401(self):
    res = self.client().get('/movies')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Authorization header is expected.")


  """DELETE METHODS"""


  def test_delete_actor(self):
    res = self.client().delete('/actors/1', headers = {'Authorization' : casting_director_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])


  def test_delete_actor(self):
    res = self.client().delete('/actors/2', headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])


  def test_delete_actor_with_error_422(self):
    res = self.client().delete('/actors/152', headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Unprocessable Content")


  def test_delete_actor_with_error_404(self):
    res = self.client().delete('/actors/1000', headers = {'Authorization' : casting_director_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Resource Not Found")


  """POST METHODS"""


  def test_create_actor(self):
    actor = {
        'name' : 'Amily',
        'gender': 'Female',
        'age' : "25"
    } 

    res = self.client().post('/actors', json = actor, headers = {'Authorization' : casting_director_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    

  def test_create_actor_with_error_401(self):
    actor = {
        'name' : 'Anna',
        'gender': 'Female',
        'age' : "33"
    } 

    res = self.client().post('/actors', json = actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Authorization header is expected.")


  def test_create_movie(self):
    movie = {
        'title' : '1+1',
        'release_date' : date.today()
    } 

    res = self.client().post('/movies', json = movie, headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])


  def test_create_movie_with_error_422(self):
    no_name_movie = {
        'release_date' : date.today()
    } 

    res = self.client().post('/movies', json = no_name_movie, headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Unprocessable Content")
  

  def test_actor_creation_not_allowed_405_error(self):
    res = self.client().post('/actors/555', json=self.new_actor, headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Method Not Allowed")


  """PATCH METHODS"""


  def test_update_actor(self):
    new_json_actor_new_age = {
        'age' : 11
    } 
    res = self.client().patch('/actors/1', json = new_json_actor_new_age, headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertEqual(data['id'], 1)


  def test_update_actor_with_error_400(self):
    res = self.client().patch('/actors/152', headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 400)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Invalid Request")


  def test_update_movie_with_error_404(self):
    res = self.client().patch('/movies/1000', headers = {'Authorization' : executive_producer_jwt})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])
    self.assertEqual(data['message'], "Resource Not Found")


# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()