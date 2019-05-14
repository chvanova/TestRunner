import sys
import importlib

"""
Please add 'skip' decorator here. If test method annotated with this decorator then test is not executed.
Semantic is like this:
"""


def skip(func):
    skip.count = 0

    def wrapper(func):
        skip.count += 1
        return wrapper

    return wrapper

"""
Please add TestRunner class here. Class must have mandatory methods:
    
    process_tests - should execute all test methods from test class that name starts with 'test_' with logic like this:
    
        1. If test method execution has no asserts or exceptions this test should be marked as 'pass'.
        2. If test method execution has finished with assertion then this test should be marked as 'fail'.
        3. If test method execution has finished with exception then this test should be marked as 'error'.
        4. If test method decorated with @skip decorator test should be marked as skipped.
              
    get_result - should return statistic for pass, error, fail, skipped tests. 
    
    So for TestClass class from test_class.py the result should look like this:
        >> pass: 2 |error: 1 |fail: 1 |skipped: 1 

Class semantic is like this:
"""
sys.path.append('/home/kchvanova/PycharmProjects/test_task/TestRunner/suites')
mod = importlib.import_module('test_class')


class TestRunner:

    def __init__(self, method_name='runTest'):
        self.method_name = method_name
        self.passed = 0
        self.failed = 0
        self.errors = 0
        self.skipped = 0

    def find_tests(self):
        test_suite = None
        test_names = []
        for attr in dir(mod):
            if attr.startswith('Test'):
                test_suite = getattr(mod, attr)
                for i in dir(test_suite):
                    if i.startswith('test_'):
                        test_names.append(getattr(test_suite, i))
        return test_names, test_suite

    def process_tests(self):
        test_names, test_suite = self.find_tests()
        for test in test_names:
            try:
                test(test_suite())
                if 'test' in test.__name__:
                    self.passed += 1
            except AssertionError:
                self.failed += 1
            except FileNotFoundError:
                self.errors += 1

    def get_result(self):
        return 'pass: {} |error: {} |fail: {} |skipped: {}'.format(self.passed, self.errors, self.failed, skip.count)
