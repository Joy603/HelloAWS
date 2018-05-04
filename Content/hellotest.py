import unittest
from hello import HelloAWS

class TestCase(unittest.TestCase):
    def test_message(self):
        helloaws = HelloAWS()
        self.assertEqual(helloaws.message, 'Hello AWS')

if __name__ == '__main__':
    unittest.main()