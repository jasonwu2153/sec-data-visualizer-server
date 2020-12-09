get_sec_companies_sql = 'SELECT * FROM sec_companies ORDER BY name ASC;'
get_top_ten_holdings = '''SELECT holdings.lei, 
                             legal_entities.name,
                             legal_entities.title,
                             holdings.isin,
                             holdings.cusip,
                             holdings.units,
                             holdings.balance,
                             holdings.val_usd
                       FROM holdings
                       INNER JOIN legal_entities ON holdings.lei = legal_entities.lei 
                       WHERE held_by = %s
                       ORDER BY val_usd DESC
                       LIMIT 10;'''