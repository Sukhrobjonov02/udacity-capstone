## Udacity Full-Stack Web Developer Nanodegree Capstone
1. Motivation
2. Setup
3. Endpoints
4. Authentification
5. Deployment

## Motivations
This is the final project of the Udacity Full-Stack Web Developer Nanodegree. 
The capstone project includes the exploration of various topics, including:

-- Database modeling using PostgreSQL and SQLAlchemy, as documented in the "model.py" file.
-- API development and the implementation of CRUD (Create, Read, Update, Delete) operations on the database using Flask, which can be found in the "app.py" file.
-- Unit testing to ensure the correctness and functionality of the application, with test cases defined in the "test_app.py" file.
-- Integration of authorization and role-based authentication control using Auth0, as specified in the "auth.py" file.
-- Deployment of the project on the Heroku platform.

The application functions as a virtual casting agency, catering to the roles of casting assistant and executive producer.
Its primary objective revolves around efficiently managing the casting agency's operations, specifically in relation to actors and movies.

## Setup
### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the requirements.txt file.

### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:
```
export FLASK_APP=api.py;
```
To run in the development mode, run:
```
export FLASK_ENV=development;
```
To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


To login or set up an account, go to the following url:
```
https://dev-g30o00804fpc8bgb.us.auth0.com/authorize?audience=movies&response_type=token&client_id=5X8I7KbUlzzzLl7RFWOwWzDPdGhDRhL3&redirect_uri=https://127.0.0.1:8080/login-results
```


The application will consist of 3 distinct roles:

1. Casting Assistant: This role will have permissions limited to performing GET requests for both actors and movies.
2. Casting Director: This role will have wider permission that Casting Assistant, allowing for the execution of all actions allowed for Castring Assistant and adding/removing actors or modifying both actors and movies.
3. Executive Producer: This role will have comprehensive permissions, allowing for the execution of all available actions and operations within the application.

To perform unit testing in the "test_app.py" file, there are three tokens: one for the casting assistant role, second one for the casting director role and another for the executive producer role. These tokens should be generated and obtained from Auth0, where you will need to create the relevant roles and users.

After creating the roles and users in Auth0, assign the appropriate roles to the corresponding user accounts to ensure proper authentication and authorization during testing.

To use the tokens for authentication, extract the access token from the redirected URL provided by Auth0 after successful authentication. Then, include the access token in the authorization header when sending requests to the application.

By following these steps, you can perform unit testing with the appropriate authentication and authorization in place to simulate the behavior of the casting assistant and executive producer roles.

### Endpoints
#### GET /actors
- General:
    - Returns all actors.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors`

```
{
  "result": [{
      "id": 1,
      "name": "Anna"
      "age": 20,
      "gender": "Female"
    }],
  "success": true
}
```

#### GET /movies
- General:
    - Returns all movies.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/movies`

```
{
  "result": [{
      "id": 1,
      "title": "1+1"
      "release_date": "2023-04-13",
      "genres": ["Comedy"]
    }],
  "success": true
}
```


#### DELETE /actors/{actor_id}
- General:
    - Deletes an existing actor (if it exists) by given `ID`.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors/15 -X DELETE`

```
{
  'deleted': 1,
  'success' : true
}
```


#### DELETE /movies/{actor_id}
- General:
    - Deletes an existing movie (if it exists) by given `ID`.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/movies/15 -X DELETE`

```
{
  'deleted': 1,
  'success' : true
}
```

#### POST /actors
- General:
    - Adds a new actor using the submitted name, age and gender properties (all of them are required).
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors -X POST -H "Content-Type: application/json" -d '{"name":"Abdulaziz", "gender":"Male", "age":"21"}'`

```
{
    "posted": [{
            "age": 21,
            "gender": "Male",
            "id": 3,
            "name": "Abdulaziz"
        }],
    "success": true
}
```

#### POST /movies
- General:
    - Adds a new movie using the submitted title, release_date and genres properties (title and genres are required, release_date has default today's date).
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/movies -X POST -H "Content-Type: application/json" -d '{"title":"Spider-Man", "release_date":"2019-05-16", "genres":["Action"]'`

```
{
    "posted": [{
            "title": "Spider-Man",
            "release_date": "2019-05-16",
            "id": 2,
            "genres": ["Action]
        }],
    "success": true
}
```

#### PATCH /actors/{actor_id}
- General:
    - Updates an existing actor using the submitted age property.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors/15 -X PATCH -H "Content-Type: application/json" -d '{"age": "15"}'`

```
{
  "success": true,
  "updated": 15
}
```

#### PATCH /movies/{movies_id}
- General:
    - Updates an existing movie using the submitted title, release_date and genres properties. Can update all of them, or only one that was provided.
- Sample: `curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/movies/10 -X PATCH -H "Content-Type: application/json" -d '{"title": "Flash", "release_date": "2015-07-22", "genres": ["Action", "Drama"]}'`

```
{
  "success": true,
  "updated": 10
}
```

## Authentification
When making API calls, ensure that you include the necessary authentication information in the headers. Specifically, add an "Authorization" header with the Bearer token as the value. Remember to prepend the token with the word "Bearer" followed by a space.

Additionally, please keep in mind the following details:

Roles and permission tables should be properly configured in Auth0, the authentication and authorization service.
Access to various functionalities will be limited based on the assigned roles. Make sure to define at least two different roles, each with different permissions, to enforce role-based access control (RBAC).
The JSON Web Token (JWT) will contain the necessary permission claims to support RBAC. These claims will specify the allowed actions based on the user's assigned roles.
By adhering to these guidelines, you can ensure secure and controlled access to your API endpoints based on the user's assigned roles and permissions.

For example: (Bearer token for Casting Director)
```
{
    "Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDdiMzZlYmVkMTUzOWJlNGQxOWUxOWYiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMDg0NDQsImV4cCI6MTY4OTAxNTY0NCwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.VAvPkcso6Ye5iSH0PeoDnbylbLvaziPKf5PkB55OGFoN7_WlmebccTQ56vljoa24RmxM7PVbWtRQypfovzAgGvZYCmMZYTzh5seaaG1sjENincxXsjtFGQgKrt7aEhYUc5ZPS_In1Y02-or-NNalr-VJjhucbaFT4TnRyNNUeCWZpCZQgzpnfDCFxTypznHdf2uCoQyvEnFtg53r9vAexSgzKXOrMP0VkIGhdR6l6JBlelrpgGoGOQesufSNvED21lGVF5mb1Aw98nl6W5EY-kuNJ7NgAmZPtZUhdXw84HSGe-KQUPQJ_zPSiny_qTC3cYh-qj-pbBsEBb_av9BzZg"
}
```
To debug and examine the permissions of a token, you can visit JWT.io's debugger tool at https://jwt.io/#debugger-io. This tool allows you to analyze the token and verify if it contains the relevant permissions required to perform specific requests.

Here's an example of how to add an actor to a Heroku database with the Bearer token attached for authentication:
```
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"Anna", "gender":"Female", "age":"35"}' "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDdiMzdiMWZjNjBjNTVlYTg2NDQ5OGMiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMDc2OTgsImV4cCI6MTY4OTAxNDg5OCwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.awaX3D3hLqvGwOSM4nN7QwwieMWANcr6yeBpcE8U_mSGErnr0Q6SmxTw2K4_vFdyo_tV-ba2PJAko7eZ9ZrZJC-lFmHkjP2taeXi_jyKYOjzx4ggznpZiheoyHVRxH-7YThVLBXX2RN0jGzZ3cbwy1W6x68TwFIUY_N_EewSn-V50e895oqndQTtRezBH3BsvilhrUsGEZLWclrpf8juPsNTfsBqfuehevFYQtGm9TNKYQRDpqihYonxABYCCbeb38OHm5dA-UERoA0SMvgBtlTvjFI4sJzVP7-KJWCyrLQpy9MMohc5BdnJHi6aoW3qHMg84f8956qoECFScX5f1g" https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors 
```
Here's an example of how to update an actor with ID 2 in a Heroku database, using a Bearer token for authentication:
```
$ curl https://udacity-capstone-c1ff4110f0e0.herokuapp.com/actors/2 -X PATCH -H "Content-Type: application/json" -d '{"age":"15"}' "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1RX2IyVFREVm11bFVZM0lSaE9GTCJ9.eyJpc3MiOiJodHRwczovL2Rldi1nMzBvMDA4MDRmcGM4YmdiLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDdiMzZlYmVkMTUzOWJlNGQxOWUxOWYiLCJhdWQiOiJtb3ZpZXMiLCJpYXQiOjE2ODkwMDg0NDQsImV4cCI6MTY4OTAxNTY0NCwiYXpwIjoiNVg4STdLYlVsenp6TGw3UkZXT3dXekRQZEdoRFJoTDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.VAvPkcso6Ye5iSH0PeoDnbylbLvaziPKf5PkB55OGFoN7_WlmebccTQ56vljoa24RmxM7PVbWtRQypfovzAgGvZYCmMZYTzh5seaaG1sjENincxXsjtFGQgKrt7aEhYUc5ZPS_In1Y02-or-NNalr-VJjhucbaFT4TnRyNNUeCWZpCZQgzpnfDCFxTypznHdf2uCoQyvEnFtg53r9vAexSgzKXOrMP0VkIGhdR6l6JBlelrpgGoGOQesufSNvED21lGVF5mb1Aw98nl6W5EY-kuNJ7NgAmZPtZUhdXw84HSGe-KQUPQJ_zPSiny_qTC3cYh-qj-pbBsEBb_av9BzZg"
```

### Deployment 
The API is live and hosted on the [Heroku](https://www.heroku.com). To access the API, you need to use the provided URL, and authentication is required for interaction.

## Author
Abdulaziz Sukhrobjonov - [LinkedIn](https://www.linkedin.com/in/abdulaziz-sukhrobjonov/) | [GitHub](https://github.com/Sukhrobjonov02)

## License

`The Treasure Library` is a public domain work, dedicated using
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do
whatever you want with it.