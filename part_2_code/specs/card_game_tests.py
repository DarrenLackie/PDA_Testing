import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()

    def test_check_for_ace(self):
        ace_card = Card(suit='Spades', value=1)
        non_ace_card = Card(suit='Diamonds', value=2)

        self.assertTrue(self.card_game.check_for_ace(ace_card))
        self.assertFalse(self.card_game.check_for_ace(non_ace_card))

    def test_highest_card(self):
        card1 = Card(suit='Spades', value=5)
        card2 = Card(suit='Diamonds', value=8)

        self.assertEqual(self.card_game.highest_card(card1, card2), card2)

    def test_cards_total(self):
        cards = [Card(suit='Spades', value=2), Card(suit='Diamonds', value=4)]

        self.assertEqual(self.card_game.cards_total(cards), "You have a total of 6")