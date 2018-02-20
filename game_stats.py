from pathlib import Path

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        self.game_paused = False

        # High score should never be reset.
        file = Path('data.dat')
        if file.exists():
            with open('data.dat', 'rb') as binary_file:
                data = binary_file.read()
                self.high_score = int.from_bytes(data, byteorder='big')
        else:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
