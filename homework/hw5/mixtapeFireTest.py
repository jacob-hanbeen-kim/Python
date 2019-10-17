import unittest

class TestNotebook(unittest.TestCase):

    def test_mixtapeFire_1000_4(self):
        self.assertEqual(mixtapeFire(1000, 4), "Your mix tape is fire!")
    def test_mixtapeFire_1000_6(self):
        self.assertEqual(mixtapeFire(1000, 6), "Invalid input. Try again.")
    def test_mixtapeFire_600_2(self):
        self.assertEqual(mixtapeFire(600, 2), "You should quit the rap game.")
    
    def test_mixtapeFire_1500_3(self):
        self.assertEqual(mixtapeFire(1500, 3), "Your mix tape is fire!")
    def test_mixtapeFire_300_7(self):
        self.assertEqual(mixtapeFire(300, 7), "Invalid input. Try again.")
    def test_mixtapeFire_1000_2(self):
        self.assertEqual(mixtapeFire(1000, 2), "You should quit the rap game.")
    def test_mixtapeFire_400_5(self):
        self.assertEqual(mixtapeFire(400, 5), "You should quit the rap game.")


unittest.main(argv=[''], verbosity=2, exit=False)