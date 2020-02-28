Jsnapy
========

This small repository is intended for testing of a bug in Junpier/jsnapy.

Create a virtualenv and install the requirements.

To run it, set the `JSNAPY_HOME` environment variable to the current directory, so Jsnapy can find the `logging.yml` file.

```shell script
JSNAPY_HOME=./ python main.py
```

Testing
========

The output of this script should show a failed test, because the element "protocol-name" in the POST snapshot is different from the PRE snapshot.
But the test result shows that jsnapy is only reading the PRE snapshot and the tests succeed.

```python
{'show route 0.0.0.0': [{'count': {'fail': 0, 'pass': 2},
                         'failed': [],
                         'node_name': './protocol-name',
                         'passed': [{'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': '*'},
                                     'message': 'Same protocol name',
                                     'post': {'./protocol-name': ['BGP']}, # THIS IS WRONG
                                     'post_node_value': ['BGP'],
                                     'pre': {'./protocol-name': ['BGP']},
                                     'pre_node_value': ['BGP']},
                                    {'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': ''},
                                     'message': 'Same protocol name',
                                     'post': {'./protocol-name': ['BGP']},
                                     'post_node_value': ['BGP'],
                                     'pre': {'./protocol-name': ['BGP']},
                                     'pre_node_value': ['BGP']}],
                         'result': True,
                         'test_name': 'show_default_route',
                         'testoperation': 'no-diff',
                         'xpath': '//route-table[normalize-space(table-name) '
                                  '!= "inet.0" and normalize-space(table-name) '
                                  '!= "VRF02.inet.0"]/rt/rt-entry'},
                        {'count': {'fail': 0, 'pass': 2},
                         'failed': [],
                         'node_name': './as-path',
                         'passed': [{'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': '*'},
                                     'message': 'Same as-path',
                                     'post': {'./as-path': ['60606']},
                                     'post_node_value': ['60606'],
                                     'pre': {'./as-path': ['60606']},
                                     'pre_node_value': ['60606']},
                                    {'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': ''},
                                     'message': 'Same as-path',
                                     'post': {'./as-path': ['60606']},
                                     'post_node_value': ['60606'],
                                     'pre': {'./as-path': ['60606']},
                                     'pre_node_value': ['60606']}],
                         'result': True,
                         'test_name': 'show_default_route',
                         'testoperation': 'no-diff',
                         'xpath': '//route-table[normalize-space(table-name) '
                                  '!= "inet.0" and normalize-space(table-name) '
                                  '!= "VRF02.inet.0"]/rt/rt-entry'},
                        {'count': {'fail': 0, 'pass': 2},
                         'failed': [],
                         'node_name': './nh/to',
                         'passed': [{'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': '*'},
                                     'message': 'Same next hop IP',
                                     'post': {'./nh/to': ['10.1.199.66']},
                                     'post_node_value': ['10.1.199.66'],
                                     'pre': {'./nh/to': ['10.1.199.66']},
                                     'pre_node_value': ['10.1.199.66']},
                                    {'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': ''},
                                     'message': 'Same next hop IP',
                                     'post': {'./nh/to': ['10.1.253.0']},
                                     'post_node_value': ['10.1.253.0'],
                                     'pre': {'./nh/to': ['10.1.253.0']},
                                     'pre_node_value': ['10.1.253.0']}],
                         'result': True,
                         'test_name': 'show_default_route',
                         'testoperation': 'no-diff',
                         'xpath': '//route-table[normalize-space(table-name) '
                                  '!= "inet.0" and normalize-space(table-name) '
                                  '!= "VRF02.inet.0"]/rt/rt-entry'},
                        {'count': {'fail': 0, 'pass': 2},
                         'failed': [],
                         'node_name': './nh/via',
                         'passed': [{'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': '*'},
                                     'message': 'Same next hop interface',
                                     'post': {'./nh/via': ['irb.283']},
                                     'post_node_value': ['irb.283'],
                                     'pre': {'./nh/via': ['irb.283']},
                                     'pre_node_value': ['irb.283']},
                                    {'id': {'../../table-name': 'VRF14.inet.0',
                                            './active-tag': ''},
                                     'message': 'Same next hop interface',
                                     'post': {'./nh/via': ['ae0.0']},
                                     'post_node_value': ['ae0.0'],
                                     'pre': {'./nh/via': ['ae0.0']},
                                     'pre_node_value': ['ae0.0']}],
                         'result': True,
                         'test_name': 'show_default_route',
                         'testoperation': 'no-diff',
                         'xpath': '//route-table[normalize-space(table-name) '
                                  '!= "inet.0" and normalize-space(table-name) '
                                  '!= "VRF02.inet.0"]/rt/rt-entry'}]}
```
