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

#Polymorphism:

# Abstract Base Class (ABC): The UIControl class serves as an ABC, defining a common interface for UI controls with the draw() method.
# Subtypes with Different Implementations: TextBox and DropDownlist inherit from UIControl and provide their own specific implementations 
  # of draw(), showcasing polymorphic behavior.
# Generic Function: The draw(controls) function treats all UIControl instances uniformly, 
  # regardless of their exact type. It calls control.draw() for each control, relying on polymorphism 
  # to execute the appropriate drawing logic for each subtype.

