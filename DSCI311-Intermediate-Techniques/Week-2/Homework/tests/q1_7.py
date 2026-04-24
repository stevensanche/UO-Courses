OK_FORMAT = True

test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(counts_aggregated_by_name_and_year.columns)\n3', 'hidden': False, 'locked': False},
                                   {'code': '>>> counts_aggregated_by_name_and_year.query("Year == 2013")["Count"].sum()\n3081614', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
