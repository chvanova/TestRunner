from sys import argv
from TestRunner import TestRunner

"""
Please implement TestRunner class (check requirements in TestRunner.py). 
It should get module name as input and execute all methods from this module that name starts from 'test_'

Please use TestClass from test_class.py as an example of this test class.

So for this test class execution should look like this:

/Users/avolkov/work/virtual_env_37/bin/python3.7 run.py suites.test_class.TestClass
pass: 2 |error: 1 |fail: 1 |skipped: 1 

Process finished with exit code 0
"""

if __name__ == '__main__':
    file_name = argv[0]
    tr = TestRunner(file_name)
    tr.process_tests()
    print(tr.get_result())
