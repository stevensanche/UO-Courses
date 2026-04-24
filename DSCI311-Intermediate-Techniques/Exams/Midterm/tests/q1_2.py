OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> (type(mismatches) == pd.Series) | (type(mismatches) == np.ndarray)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> (len(mismatches)) > 0 & (len(mismatches) < 30)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
