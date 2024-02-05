from abc import ABC ,  abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("Drawing a Text box")

class DropDownlist(UIControl):
    def draw(self):
        print("Drawing a  drop down list")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownlist()
textbox = TextBox()
draw([ddl, textbox])

