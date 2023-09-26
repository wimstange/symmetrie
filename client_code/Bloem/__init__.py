from ._anvil_designer import BloemTemplate
from anvil import *
import math

class Bloem(BloemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.N = self.text_box_5.text
        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        c = self.canvas_1
        for k in range(int(self.N)):
            print(k)
        
        
        
        
        
        c.begin_path()
        c.move_to(100,100)
        c.line_to(100,200)
        c.line_to(200,200)
        c.close_path()
  
        c.stroke_style = "#2196F3"
        c.line_width = 3
        c.fill_style = "#E0E0E0"
  
        c.fill()
        c.stroke()

    def text_box_5_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        self.N = self.text_box_5.text


        

