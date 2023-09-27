from ._anvil_designer import WervelTemplate
from anvil import *
import math

class Wervel(WervelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_wervel(self,M):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "#2196F3"
        c.line_width = 1
        X = []
        A = 0.5
        N = math.int(4*math.pi/(M*A))
        F = (M-2)*math.pi/M
        C = math.sin(F)/(math.sin(A+F)+math.sin(A))
        for i in range(M):
            T = (2*I+1)*math.pi/M
            X.append(math.sin(T))
            Y.append(math.cos(T))
        for j in range(N):
            c.move_to(X[0],Y[0])
            
            
        
        for k in range(N):
            T=2*k*math.pi/N
            Q=C*math.cos(M*T)
            R=A+B*math.cos(M*T+Q)
            X=250+100*R*math.cos(T)
            Y=250+100*R*math.sin(T)
            if k==0:
                c.move_to(X,Y)
            else:
                c.line_to(X,Y)
                
            c.stroke()