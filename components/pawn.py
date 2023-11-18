"""Base class for characters.

Property of Austin Lidey / Copyright 2023
"""
from systems.health import Health


class Pawn:
    """Class representing single pawn."""

    def __init__(self):
        self._health = Health()

    @property
    def health(self):
        """Get Health system for this pawn."""
        return self._health
