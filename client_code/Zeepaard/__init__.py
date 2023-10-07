from ._anvil_designer import ZeepaardTemplate
from anvil import *
import anvil.server

class Zeepaard(ZeepaardTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_zeepaard(self):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1   
        
        X = [0,4,4,7,7,6,6,3,3,0,0,1,1,-2,-2,0,0,2,2,-1,-1,0,0,3,3,6,6,5,5,8,8,6,6,4,4,3,3,2,2]
        Y = [0,3,2,2,1,1,0,0,1,1,4,4,5,5,6,6,8,8,9,9,10,10,11,11,10,10,7,7,6,6,5,5,3,3,4,4,7,7,8]
        M = 38
        for N1 in range(8+1):
            for N2 in range(6+1):
                U = 3+6*N1
                V = 10*N2-3*N1
                P1, P2 = 10+5*(U+X[1]),150+5*(V+Y[1])
                c.move_to(P1,P2)
                for K in range(2,M+1):
                    P1, P2 = 10+5*(U+X[K]),150+5*(V+Y[K])
                    c.line_to(P1,P2)
                c.stroke()

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_zeepaard()
