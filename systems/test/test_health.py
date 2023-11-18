"""Unit test the health class.

Property of Austin Lidey / Copyright 2023
"""
import unittest

from systems.health import Health


class TestHealth(unittest.TestCase):
    """Class to facilitate testing of the Health class."""

    def setUp(self) -> None:
        self.testing_health = Health()
        # HP removed, HP expected remaining, Is alive
        self.remove_health_test_cases = [
            (-1000.0, 1000.0, True),
            (-123.456, 1000.0, True),
            (-0.1, 1000.0, True),
            (-0, 1000.0, True),
            (0, 1000.0, True),
            (1.0, 999.0, True),
            (100.0, 900.0, True),
            (1000.0, 0.0, False),
            (10000.0, -9000.0, False),
        ]

        return super().setUp()

    def test_health_init(self):
        """Verify we instantiate Health with the correct values."""
        self.assertEqual(self.testing_health.current_health, 1000.0)
        self.assertEqual(self.testing_health.max_health, 2500.0)
        self.assertEqual(self.testing_health.is_alive, True)

    def test_health_properties(self):
        """Verify that we can get/set the properties of Health."""
        self.testing_health.max_health = 5000.0
        self.assertEqual(self.testing_health.max_health, 5000.0)
        self.testing_health.current_health = -1.0
        self.assertEqual(self.testing_health.current_health, -1.0)
        self.testing_health.is_alive = False
        self.assertEqual(self.testing_health.is_alive, False)

    def test_add_health(self):
        """Verify the add health method."""
        test_cases = [
            (-1000.0, 1000.0),
            (-123.456, 1000.0),
            (-0.1, 1000.0),
            (-0, 1000.0),
            (0.0, 1000.0),
            (1.0, 1001.0),
            (100.0, 1100.0),
            (1000.0, 2000.0),
            (10000.0, 2500.0),
        ]
        for amount, expected_result in test_cases:
            self.testing_health.add_health(amount)
            self.assertEqual(self.testing_health.current_health, expected_result)
            # Reset the testing_health object.
            self.testing_health = Health()

    def test_remove_health(self):
        """Verify the remove health method."""

        for amount, expected_health, expected_is_alive in self.remove_health_test_cases:
            self.testing_health.remove_health(amount)
            self.assertEqual(self.testing_health.current_health, expected_health)
            self.assertEqual(self.testing_health.is_alive, expected_is_alive)
            # Reset the testing_health object.
            self.testing_health = Health()


if __name__ == "__main__":
    unittest.main()
