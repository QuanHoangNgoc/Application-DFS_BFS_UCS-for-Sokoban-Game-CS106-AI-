import json

class Scores:
    def __init__(self, game):
        self.game = game

    def load(self):
        try:
            with open("scores", "r") as data:
                scores = json.load(data)
                self.game.index_level = scores["level"]
            self.game.load_level()
            self.game.start()
        except FileNotFoundError:
            print("No saved data")

    def save(self):
        # Saving score in file only when current level > saved level
        try:
            with open("scores", "r") as data:
                scores = json.load(data)
                saved_level = scores["level"]
        except FileNotFoundError:
            saved_level = 0

        if saved_level < self.game.index_level:
            data = {
                "level": self.game.index_level
            }
            with open("scores", "w") as scores:
                json.dump(data, scores, ensure_ascii=False, indent=4)
