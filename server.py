from flask import Flask, jsonify, request

from db import cnx
from sql import get_sec_companies_sql

app = Flask(__name__)

@app.route('/sec-companies', methods=['GET'])
def get_sec_companies():
    'Returns sec-companies from the database in alphabetical order.'
    cursor = cnx.cursor()
    cursor.execute(get_sec_companies_sql)

    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    data = [dict(zip(attr_names, row))  
        for row in cursor.fetchall()]

    cursor.close()
    return jsonify(data)
