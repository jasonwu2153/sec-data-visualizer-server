get_sec_companies_sql = 'SELECT * FROM sec_companies ORDER BY name ASC;'
get_top_five_holdings_by_value = '''SELECT holdings.lei, 
                                          legal_entities.name,
                                          legal_entities.title,
                                          holdings.isin,
                                          holdings.cusip,
                                          holdings.units,
                                          holdings.balance,
                                          holdings.val_usd
                                    FROM holdings
                                    INNER JOIN legal_entities ON holdings.lei = legal_entities.lei 
                                    WHERE held_by = %s AND units = 'NS'
                                    ORDER BY val_usd DESC
                                    LIMIT 10;'''
get_top_five_holdings_by_number_shares = '''SELECT holdings.lei, 
                                                  legal_entities.name,
                                                  legal_entities.title,
                                                  holdings.isin,
                                                  holdings.cusip,
                                                  holdings.units,
                                                  holdings.balance,
                                                  holdings.val_usd
                                            FROM holdings
                                            INNER JOIN legal_entities ON holdings.lei = legal_entities.lei 
                                            WHERE held_by = %s AND units = 'NS'
                                            ORDER BY balance DESC
                                            LIMIT 5;'''
get_pie_chart_holdings_data = '''SELECT legal_entities.name,
                                        holdings.balance,
                                        holdings.val_usd
                                 FROM holdings
                                 INNER JOIN legal_entities ON holdings.lei = legal_entities.lei
                                 WHERE held_by = %s AND units = 'NS' AND holdings.balance > 0 AND holdings.val_usd > 0
                                 ORDER BY val_usd DESC
                                 LIMIT 100;'''
