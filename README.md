# REST API built with Flask

Hi, 

This is a simple REST Api with CRUD functionality, implemented using Flask, Flask-JWT, Flask-RESTful, Flask-SQLAlchemy and Postgres. 

## Endpoints
App has 3 database tables: users, stores and items. 

![postman pic](https://github.com/soringherghisan/REST-API-FLASK_1/blob/master/postman.png?raw=true)

- first step is to make a POST request to the /register endpoint
  - the body should be a JSON object with properties 'username' and 'password'
- next, a POST request to the /auth endpoint with the same body as before 
  - if succesful, retrieve the jwt access_token from the body of the response and add it to the Authorization header with value "JWT ACCESS_TOKEN_HERE" for the next requests 
- afterwards, the GET and DELETE requests are self-explanatory
  - for the POST request for endpoint /store/\<name>, there's no body necessary
  - for the POST request for endpoint /item/\<name>, the body should be a JSON obj. with props. 'price' and 'store_id'
    - the 'store_id' prop is based on the numbers of stores already in the table, currently there are 2 example stores, with ids 1 and 2
      - the 'store_id' autoincrements so if you were to add another store to the existing two, the store you added will have and id of 3



## Links
Deployed to Heroku -> https://stores-rest-api-practice-sorin.herokuapp.com/
