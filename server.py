from flask import Flask, jsonify, request

from db import cnx
from sql import get_sec_companies_sql, get_top_ten_holdings

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

@app.route('/holdings-data', methods=['GET'])
def get_holdings_data():
    'Returns holding data from the database for the company with the requested cik.'
    cik = request.args.get('cik')
    cursor = cnx.cursor()
    cursor.execute(get_top_ten_holdings, (cik,))

    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    top_ten_data = [dict(zip(attr_names, row))  
        for row in cursor.fetchall()]

    cursor.close()
    return jsonify(top_ten_data)

