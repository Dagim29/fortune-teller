import unittest
from unittest.mock import patch
from fortune_teller import generate_fortune

class TestFortuneTeller(unittest.TestCase):
    @patch('os.getenv')
    def test_generate_fortune(self, mock_getenv):
        mock_getenv.side_effect = lambda k, d=None: 'student' if k == 'GITHUB_ACTOR' else 'push'
        
        fortune = generate_fortune()
        
        # Check that actor name appears
        self.assertIn('student', fortune)
        
        # Check that it's one of the valid fortunes
        valid_fortunes = [
            "sparkle brighter than a supernova",
            "debugging skills will reach legendary status",
            "launch your career to new heights",
            "pure perfection",
            "a brilliant idea will strike",
            "make the world more colorful",
            "coding superpowers will awaken",
            "Luck is on your side"
        ]
        self.assertTrue(any(phrase in fortune for phrase in valid_fortunes))
        
        # Check minimum length
        self.assertTrue(len(fortune) > 20)

if __name__ == '__main__':
    unittest.main()
