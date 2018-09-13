import unittest
import unittestpackage.assert_demo

class TestCaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run only once before every test")
        print("#*" * 30)

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("running method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after every test")
        print("#*" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
