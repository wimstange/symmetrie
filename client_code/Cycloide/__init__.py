from ._anvil_designer import CycloideTemplate
from anvil import *
import anvil.server
import math
import anvil.media

class Cycloide(CycloideTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_cycloide(self):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "#2196F3"
        c.line_width = 1
        M = 7
        N = 180
        for k in range(1,N):
            T = 2*k*math.pi/N
            X1, Y1 = 250*math.cos(T), 250*math.sin(T)
            X2, Y2 = 250*math.cos(M*T), 250*math.sin(M*T)
            c.move_to(X1+250,Y1+250)
            c.line_to(X2+250,Y2+250)
            c.stroke()

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_cycloide()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        img = self.canvas_1.get_image()
        anvil.media.download(img)
