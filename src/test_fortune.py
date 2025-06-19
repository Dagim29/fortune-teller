import unittest
from unittest.mock import patch
from fortune_teller import generate_fortune

class TestFortuneTeller(unittest.TestCase):
    @patch('os.getenv')
    def test_generate_fortune(self, mock_getenv):
        mock_getenv.side_effect = lambda k, d=None: 'student' if k == 'GITHUB_ACTOR' else 'push'
        
        fortune = generate_fortune()
        self.assertIn('student', fortune)
        self.assertIn('push', fortune)
        self.assertTrue(len(fortune) > 20)

if __name__ == '__main__':
    unittest.main()