import unittest
from month import is_month

class TestMonth(unittest.TestCase):

    def test_it_returns_true_if_argument_is_a_month(self):
        self.assertEqual(True, is_month('jan'))
        self.assertEqual(True, is_month('nov'))
        self.assertEqual(False, is_month('Mon'))
        self.assertEqual(False, is_month('Five'))

    def test_it_does_not_return_value_for_non_strings(self):
        self.assertEqual('argument should be of type string', is_month(1))
        self.assertEqual('argument should be of type string', is_month(True))
        self.assertEqual('argument should be of type string', is_month([]))
        self.assertEqual('argument should be of type string', is_month({}))
        self.assertNotEqual('argument should be of type string', is_month('test'))

if __name__=="__main__":
    unittest.main()
