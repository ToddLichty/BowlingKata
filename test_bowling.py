import unittest
from bowling import BowlScorer

class BowlingScorerTests(unittest.TestCase):
    
    def setUp(self):
        self.scorer = BowlScorer()

    def test_all_gutter_balls(self):
        self.rollMany(0, 20)
        self.assertEqual(0, self.scorer.get_score())

    def test_knocked_over_single_pin(self):
        self.scorer.roll(1)
        self.assertEqual(1, self.scorer.get_score())

    def test_entire_game_no_spares_or_strikes(self):
        self.rollMany(3, 20)
        self.assertEqual(60, self.scorer.get_score())


    def test_one_spare(self):
        self.scorer.roll(5)
        self.scorer.roll(5)
        self.scorer.roll(3)

        self.rollMany(0, 17)

        self.assertEqual(16, self.scorer.get_score())

    def test_one_strike(self):
        self.scorer.roll(10)
        self.scorer.roll(4)
        self.scorer.roll(3)
        
        self.rollMany(0, 17)

        self.assertEqual(24, self.scorer.get_score())

    def test_perfect_game(self):
        self.rollMany(10, 20)

        self.assertEqual(300, self.scorer.get_score())

    def rollMany(self, pins, number_of_rolls):
        for i in range(number_of_rolls):
            self.scorer.roll(pins)

