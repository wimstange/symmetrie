from ._anvil_designer import BloemTemplate
from anvil import *
import math

class Bloem(BloemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
 
        self.teken_bloem(self.text_box_1.text,
                         self.text_box_2.text,
                         1,
                         self.text_box_4.text,
                         self.text_box_5.text)

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        pass
        
        
    def teken_bloem(self,a,b,d,m,n):
        cv = self.canvas_1
        cv.stroke_style = "#2196F3"
        cv.line_width = 3
        cv.fill_style = "#E0E0E0"      
        cv.begin_path()
        cv.move_to(100,100)
        for k in range(n):
            t = 2 * k * math.pi / n
            q = d * math.cos(m * t)
            r = a + b * math.cos(m * t  + q)
            x = r * math.cos(t)
            y = r * math.sin(t)
            cv.line_to(x,y)
            cv.close_path()
            cv.stroke()
  

  
        # cv.fill()
        # cv.stroke()


        

