from ._anvil_designer import KwadraattegelTemplate
from anvil import *
import anvil.server
import math

class Kwadraattegel(KwadraattegelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    
    def teken_kwadraattegel(self):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1

        
        self.P1 = math.pi/2
        self.X = []
        self.Y = []
        for n in range(25+1):
            self.X.append(0)
            self.Y.append(0)
        self.X[1], self.X[2], self.X[3] = 0, 1, 3
        self.Y[1], self.Y[2], self.Y[3] = 0, 1, -1
        
        for I in range(1,3+1):
            for N in range(1,3+1):
                self.X[3*I+N] = self.X[N]*math.cos(self.P1*I)-self.Y[N]*math.sin(self.P1*I)
                self.Y[3*I+N] = self.X[N]*math.sin(self.P1*I)+self.Y[N]*math.cos(self.P1*I)
        for I in range(0,3+1):
            for N in range(1,3+1):
                self.X[3*(4+I)+N] = 4-self.Y[3*I+N]
                self.Y[3*(4+I)+N] = 4-self.X[3*I+N]
        for N2 in range(0,5+1):
            for N1 in range(0,7+1):
                for J in range(0,7+1):
                    X1 = 10+8*N1
                    Y1 = 10+8*N2
                    P = 10+10*(X1+self.X[3*J+1])
                    Q = 10+10*self.Y[3*J+1]
                    c.move_to(P,Q)
                    print(P,Q)
                    for K in range(2,3+1):
                        P = 10+10*(X1+self.X[3*J+K])
                        Q = 10+10*(Y1+self.Y[3*J+K])
                        print(P,Q)
                        c.line_to(P,Q)
                    c.stroke()
                    
                
    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_kwadraattegel()

