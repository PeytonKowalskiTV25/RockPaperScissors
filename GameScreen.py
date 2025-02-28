from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import rockButton, paperButton, scissorsButton, EndButton

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started",
            "won/lost": "Tie",
            "win": 0,
            "loss": 0,
            "tie": 0
        }
        self.round = 0
    
    def elementsToDisplay(self):
        self.elements = [
            rockButton(),
            paperButton(),
            scissorsButton(),
            Label((300, 200), 100, 100, self.state["status"], 14, (0,0,0)),
            Label((300, 250), 100, 100, f"Wins: {self.state["won/lost"]}", 14, (0,0,0)),
            Label((300, 300), 100, 100, f"Win: {self.state["win"]} loss: {self.state["loss"]} tie: {self.state["tie"]}", 14, (0,0,0))
        ]