import unittest
import month

class TestMonth(unittest.TestCase):

    def test_it_returns_true_if_argument_is_a_month(self):
        self.assertEqual('True, is_month('Jan'))
        self.assertEqual('True', is_month('Nov'))
        self.assertEqual('False', is_month('Mon'))
        self.assertEqual('False, is_month('Five'))

    def test_it_does_not_return_value_for_non_strings(self):
        self.assertEqual('argument should be of type string', is_month(1))
        self.assertEqual('argument should be of type string', is_month(True))
        self.assertEqual('argument should be of type string', is_month([]))
        self.assertEqual('argument should be of type string', is_month({}))




if __name__=="__main__":
    unittest.main()
