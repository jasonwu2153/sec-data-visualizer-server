from flask import Flask, jsonify, request
from flask_cors import CORS

from db import cnx
from sql import get_sec_companies_sql, \
                get_top_five_holdings_by_value, \
                get_top_five_holdings_by_number_shares, \
                get_pie_chart_holdings_data, \
                get_top_twenty_popular_holdings_by_occurrence

app = Flask(__name__)
CORS(app)

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

    # top 5 by value
    cursor.execute(get_top_five_holdings_by_value, (cik,))
    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    top_five_by_value_data = [dict(zip(attr_names, row))  
        for row in cursor.fetchall()]

    # top 5 by number of shares
    cursor.execute(get_top_five_holdings_by_number_shares, (cik,))
    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    top_five_by_number_shares_data = [dict(zip(attr_names, row))  
        for row in cursor.fetchall()]

    # pie chart data
    cursor.execute(get_pie_chart_holdings_data, (cik,))
    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    pie_chart_data = [dict(zip(attr_names, row))  
        for row in cursor.fetchall()]

    data = {
        'top_five_by_value': top_five_by_value_data,
        'top_five_by_number_shares': top_five_by_number_shares_data,
        'pie_chart_data': pie_chart_data
    }

    cursor.close()
    return jsonify(data)


@app.route('/popular-legal-entities', methods=['GET'])
def get_legal_entities():
    'Returns top 20 holdings across all sec companies.'
    cursor = cnx.cursor()

    # top 20 holdings across all sec_companies
    cursor.execute(get_top_twenty_popular_holdings_by_occurrence)
    desc = cursor.description
    attr_names = [attr[0] for attr in desc]
    data = [dict(zip(attr_names, row))
        for row in cursor.fetchall()]

    cursor.close()
    return jsonify(data)