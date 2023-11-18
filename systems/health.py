"""Health system for Project Impossible.

Property of Austin Lidey / Copyright 2023
"""


class Health:
    """Class for health stats."""

    def __init__(self):
        self._max_health: float = 2500.0
        self._current_health: float = 1000.0
        self._is_alive: bool = True

    def add_health(self, added_health: float) -> None:
        """Add health to your pawn.

        Args:
            added_health (float): Amount of health we want to add.
        """
        if added_health > 0.0:
            # What is the total health after application?
            total_health = self.current_health + added_health

            if total_health >= self.max_health:
                self.current_health = self.max_health
            else:
                self.current_health = total_health

    def remove_health(self, removed_health: float) -> None:
        """Add health to your pawn.

        Args:
            removed_health (float): Amount of health we want to add.
        """
        if removed_health >= 0.0:
            self._current_health -= removed_health

        # If we're at or below 0, the pawn is dead.
        if self.current_health <= 0.0:
            self.is_alive = False

    @property
    def is_alive(self) -> bool:
        """Get the life status of the pawn.

        Returns:
            bool: True if pawn is alive, False otherwise.
        """
        return self._is_alive

    @property
    def current_health(self):
        """Get the current health of the pawn."""
        return self._current_health

    @is_alive.setter
    def is_alive(self, status: bool) -> None:
        """Set the life status of the pawn.

        Args:
            status (bool): Current life status.
        """
        if isinstance(status, bool):
            self._is_alive = status

    @current_health.setter
    def current_health(self, new_value: float):
        """Set the current health of the pawn.

        Args:
            new_value (float): Value to set current_health at.
        """
        if new_value:
            self._current_health = new_value

    @property
    def max_health(self) -> float:
        """Get the max health for the pawn.

        Returns:
            float: The max health for the pawn.
        """
        return self._max_health

    @max_health.setter
    def max_health(self, new_value):
        """Set the max health for the pawn.

        Args:
            new_value (_type_): The max health value.
        """
        if new_value:
            self._max_health = new_value
