from ._anvil_designer import StertegelTemplate
from anvil import *
import anvil.server
import math

class Stertegel(StertegelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_stertegel(self):
        
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.fill_style = "rgba(256,0,0,1)"
   
        P1 = math.pi/3
        P2 = math.pi/6
        R, S = 1.6906, 4.6189
        
        for N2 in range(6):
            if N2%2 == 0:
                B = 0
            else:
                B = 1
            for N1 in range(7-B):
                U = 12+4*B+8*N1
                V = 8+6.93*N2
                X = -15+15*(U+R)
                Y = 15+15*V
                
                c.move_to(X,Y)
                for K in range(6):
                    X, Y = -15+15*(U+R*math.cos(K*P1)), 15+15*(V+R*math.sin(K*P1))
                    c.line_to(X,Y)
                    X, Y = -15+15*(U+S*math.cos(K*P1+P2)), 15+15*(V+S*math.sin(K*P1+P2))
                    c.line_to(X,Y)
                    c.stroke()
                c.close_path()
                c.fill()
                
    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_stertegel()

                              
                              