from PyUI.Screen import Screen
from PyUI.PageElements import Label
from BuiltScreen import StartButton

class EndScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0))
        self.state = {
            "status": "Game Over"
        }
    
    def quit(self):
        self.window.quit()

    def elementsToDisplay(self):
        self.elements = [
            Label((300, 200), 100, 100, "Game Over", 14, (255,255,255)),
            Label((300, 250), 100, 100, f"Total wins: {self.state["wins"]}", 14, (255,255,255)),
            StartButton((300, 300), 100, 100, "Restart")
        ]