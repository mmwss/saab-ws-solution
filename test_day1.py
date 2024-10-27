import unittest

def run_all_tests():
    loader = unittest.TestLoader()

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(loader.discover('day1/tests'))

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    run_all_tests()
