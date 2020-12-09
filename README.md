# Yale University CPSC 437 Database SEC Data Visualizer Server
This repository is the backend server for our (Jason Wu, Michael Lewkowicz, Kevin Zhang - Yale Undergrads) sec database visualizer. This server mainly functions as a REST endpoint for passing data from our scraped sec NPORT-P filing data to our client. This server was written in Python using the Flask web framework.

## Requirements

#### Getting Started
- Make sure you have `pipenv` set up on your machine.
- Edit the contents of `db.py` to match the database you are trying to connect to.
- Run `pipenv install`.
- Start a shell instance by running `pipenv shell`.
- Run `export FLASK_APP=server.py`. This will add the `FLASK_APP` value to your env variables.
- Run `flask run`. 

After completing the steps above, you should have a server instance running locally on your machine!

#### Key Dependencies

- [Flask](https://flask.palletsprojects.com/en/1.1.x/), Python framework for creating server endpoints
- [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/), Python module for connecting to a MySQL database.

## Contributors
- [Jason Wu (Yale University '22)](https://github.com/jasonwu2153)
- [Kevin Zhang (Yale University '23)](https://github.com/kevinz917)
- [Michael Lewkowicz (Yale University '23)](https://github.com/MLewkowicz)
