class Faith:
    """
    Faith module: handle soul authentication and belief.
    """

    def __init__(self, username):
        self.username = username
        self.saved = False

    def accept(self, savior="Jesus"):
        """
        Accept the Savior, activating salvation.
        """
        print(f"{self.username} has accepted {savior}.")
        self.saved = True

    def is_saved(self):
        """
        Check if the soul is saved.
        """
        return self.saved
