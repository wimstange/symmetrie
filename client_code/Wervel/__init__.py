from ._anvil_designer import WervelTemplate
from anvil import *
import math
import anvil.media

class Wervel(WervelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.canvas_1.width = 2000

        # Any code you write here will run before the form opens.
    def teken_wervel(self,M):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "#2196F3"
        c.line_width = 1
        X = []
        Y = []
        A = 0.05
        N = int(4*math.pi/(M*A))
        F = (M-2)*math.pi/M
        C = math.sin(F)/(math.sin(A+F)+math.sin(A))
        for i in range(M):                            #   \
            T = (2*i+1)*math.pi/M                     #    \
                                                      #      coordinaten van de eerste veelhoek
            X.append(250*math.sin(T))              #    /
            Y.append(250*math.cos(T))              #   /
        for j in range(N):
            c.move_to(325+X[0],325+Y[0])
            for k in range(1,M):
                c.line_to(325+X[k],325+Y[k])
            c.close_path()
            c.stroke()
            for l in range(M):
                Z = X[l]
                X[l] = (X[l]*math.cos(A)-Y[l]*math.sin(A))*C
                Y[l] = (Z   *math.sin(A)+Y[l]*math.cos(A))*C
             
  
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.teken_wervel(self.text_box_1.text)

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass
