OK_FORMAT = True

test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(error_vs_alpha.columns)\n4', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(error_vs_alpha["CV Error"][error_vs_alpha["alpha"] == 0.000010][0], 10.59, 1)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
