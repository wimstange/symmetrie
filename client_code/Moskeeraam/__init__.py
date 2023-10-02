from ._anvil_designer import MoskeeraamTemplate
from anvil import *
import anvil.server

class Moskeeraam(MoskeeraamTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def teken_moskeeraam(self):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1
        X, Y = [1,1,4], [0,3,3]
        for I in range(1,5):
            for N in range(1,3):
                X[3*I+N]=X[N]*math.cos(math.PI*I)-Y[N]*math.sin(math.PI*I)
                Y[3*I+N]=X[N]*math.sin(math.PI*I)+Y[N]*math.cos(math.PI*I)

        for I in range(0,5):
            for N in range(1,3):
                X[3*(6+i)+N]=X[3*I+N]
                Y[3*(6+i)+N]=-Y[3*I+N]
        for N2 in range(6):
            if N2 % 2 == 0:
                B = 0
            else:
                B = 1
        for N1 in range(7-B):
            for J in range(11):
                X1 = 12+4*B+8*N1
                Y1 = 8+6.93*N2
                c.move_to()
                
            
                
