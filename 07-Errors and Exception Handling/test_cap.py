import unittest
import cap

class TestCap(unittest.TestCase):
    """Testing for cap.py class"""

    def test_one(self):
        text = "python"
        res = cap.cap_text(text)
        self.assertEqual(res, 'Python')

    def test_two(self):
        text = "hello my name is"
        res = cap.cap_text(text)
        self.assertEqual(res, 'Hello My Name Is')

if __name__ == '__main__':
    unittest.main()
