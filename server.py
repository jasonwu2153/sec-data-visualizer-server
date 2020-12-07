from flask import Flask, request

from db import cnx

app = Flask(__name__)

@app.route('/sec-companies', methods=['GET'])
def get_sec_companies():
    'Returns sec-companies from the database in alphabetical order.'
    pass