import unittest
from addition import add


# Ma classe TestAddition hérite de classe TestCase
# Cette classe contient plusieurs méthodes pour permettre de tester notre programme
class TestAddition(unittest.TestCase):

    # Chaque méthode contient un test de la fonction
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        self.assertEqual(add(1.2, 5.3), 6.5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -3), -3)

if __name__ == '__main__':
    unittest.main()