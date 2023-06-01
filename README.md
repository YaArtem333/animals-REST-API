# Animals REST API

## Overview
The service for zoo that provides API for working with information about animals

Made as a project for the competition from BRAIM platform

https://challenge.braim.org/it-planet/simbirsoft.html

API documentation is in the file  ***swagger_api_documentation.yml***

## Stack

+ Python 3.10
+ Flask 2.2.3
+ Flask-SQLalchemy
+ PostgreSQL
+ Docker
  
## Preparation

You need to have: 
+ PostgreSQL account
+ Python 3.10 +

Create a postgres server database

## Install & Run

### Run with Docker

**Copy repository**
```shell
git clone
```

**Change database parameters**

1) Open file ***application.py***
2) Change parameters:
   ```python
   from flask import Flask

   app = Flask(__name__)
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost:5432/animals"
   ```
   
   Set "postgresql://{user}:{password}@{host:port}/{database}" if you use postgres
   
   Set "sqlite:///data.sqlite" if you use sqlite

   If you use another db, find information in the documentation

**Change docker-compose file**

Open ***docker-compose.yml*** file and set parameters:
```yml
    POSTGRES_USER: postgres # Your username
    POSTGRES_PASSWORD: postgres # Your password
    POSTGRES_DB: 12345 # The name of your database
```

**Create and run docker container**
```shell
docker-compose up
```
The service is available on 127.0.0.1:8000

### Run on your computer ###

**Copy repository**
```shell
git clone
```

**Install libraries**
```shell
pip install flask
```
```shell
pip install psycopg2
```
```shell
pip install requests
```
```shell
pip install flask-sqlalchemy
```

**Change database parameters**

1) Open file application.py
2) Change parameters:
   ```python
   from flask import Flask

   app = Flask(__name__)
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost:5432/animals"
   ```
   
   Set "postgresql://{user}:{password}@{host:port}/{database}" if you use postgres
   
   Set "sqlite:///data.sqlite" if you use sqlite

   If you use another db, find information in the documentation


**Run your server with database**

**Run app**

Go to the folder with ***manage.py*** file and write command
```shell
python main.py
```

The service is available