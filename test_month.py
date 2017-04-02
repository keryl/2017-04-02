import unittest
import month

class TestMonth(unittest.TestCase):

    def test_it_returns_true_if_argument_is_a_month(self):
        self.assertEqual('True, is_month('Jan'))
        self.assertEqual('True', is_month('Nov'))
        self.assertEqual('False', is_month('Mon'))
        self.assertEqual('False, is_month('Five'))


if __name__=="__main__":
    unittest.main()
