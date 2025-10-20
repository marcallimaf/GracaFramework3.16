class Faith:
    def __init__(self, username):
        self.username = username
        self.saved = False

    def accept(self, savior="Jesus"):
        print(f"{self.username} has accepted {savior}.")
        self.saved = True

    def is_saved(self):
        return self.saved
