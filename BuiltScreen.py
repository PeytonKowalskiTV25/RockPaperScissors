import sys
import pygame
from PyUI.Screen import Screen #will need a screen object to extend
from PyUI.PageElements import * #will need the base element classes to extend
from random import randint

##create the custom screen class
class ExampleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        ##give the screen a state for updating values and labels----
        self.state = {
            "status": "onGoing",
            "won/lost": "Tie",
            "win": 0,
            "loss": 0,
            "tie": 0
        }
        ##----------------------------------------------------------

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (255,255,255))
        ]
        

##Add custom page elements
class StartButton(Button):
    def __init__(self):
        super().__init__((400, 100), 100, 100, "Start")
    
    def onClick(self, screen):
        screen.state["status"] = "Game Started"

class QuitButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 100, 100, "Quit")

    def onClick(self, screen):
        pygame.quit()
        sys.exit()

class rockButton(Image):
    def __init__(self):
        super().__init__((200, 100), 100, 100, "./imgus/bear.jpg")
    
    def onClick(self, screen):
        screen.state["status"] = "Bear"
        cpuChoice = randint(0,2)
        if cpuChoice == 0:
            screen.state["won/lost"] = "Tie!"
            screen.state["tie"] += 1
            screen.round += 1
        elif cpuChoice == 1:
            screen.state["won/lost"] = "You Win!"
            screen.state["win"] += 1
            screen.round += 1
        else:
            screen.state["won/lost"] = "You Lose!"
            screen.state["loss"] += 1
            screen.round += 1

class paperButton(Image):
    def __init__(self):
        super().__init__((300, 100), 100, 100, "./imgus/hunter.jpg")
    
    def onClick(self, screen):
        screen.state["status"] = "Hunter"
        cpuChoice = randint(0,2)
        if cpuChoice == 0:
            screen.state["won/lost"] = "You Lose!"
            screen.state["loss"] += 1
            screen.round += 1
        elif cpuChoice == 1:
            screen.state["won/lost"] = "Tie!"
            screen.state["tie"] += 1
            screen.round += 1
        else:
            screen.state["won/lost"] = "You Win!"
            screen.state["win"] += 1
            screen.round += 1
        
class scissorsButton(Image):
    def __init__(self):
        super().__init__((400, 100), 100, 100, "./imgus/ninja.jpg")
    
    def onClick(self, screen):
        screen.state["status"] = "Ninja"
        cpuChoice = randint(0,2)
        if cpuChoice == 0:
            screen.state["won/lost"] = "You Win!"
            screen.state["win"] += 1
            screen.round += 1
        elif cpuChoice == 1:
            screen.state["won/lost"] = "You Lose!"
            screen.state["loss"] += 1
            screen.round += 1
        else:
            screen.state["won/lost"] = "Tie!"
            screen.state["tie"] += 1
            screen.round += 1
