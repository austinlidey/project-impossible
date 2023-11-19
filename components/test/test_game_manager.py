"""Unit test the Game Manager class.

Property of Austin Lidey / Copyright 2023
"""
import unittest

from components.game_manager import GameManager


class TestGameManager(unittest.TestCase):
    """Class to facilitate testing of the GameManager class."""

    def setUp(self) -> None:
        self.gm = GameManager()
        return super().setUp()

    def test_singleton(self) -> None:
        """Verify the singleton pattern is working."""
        new_gm = GameManager()
        new_gm.testattr = 123
        # Use ID to verify they are the same object.
        self.assertEqual(id(self.gm), id(new_gm))
        # Create attribute on new copy, verify it's present on the original.
        self.assertEqual(self.gm.testattr, new_gm.testattr)


if __name__ == "__main__":
    unittest.main()
