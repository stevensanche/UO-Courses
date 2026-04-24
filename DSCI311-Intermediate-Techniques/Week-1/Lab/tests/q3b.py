OK_FORMAT = True

test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> np.array_equal(elementwise_array_sum([1], [1]), np.array([2]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.array_equal(elementwise_array_sum([-1], [1]), np.array([2]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.array_equal(elementwise_array_sum([1], [-1]), np.array([0]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.array_equal(elementwise_array_sum([1, 2, 3], [1, 2, 3]), np.array([ 2, 12, 36]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.array_equal(elementwise_array_sum([1, 5, 2], [3, 6, 6]), np.array([ 28, 241, 220]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(elementwise_array_sum([], [])) is np.ndarray\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
