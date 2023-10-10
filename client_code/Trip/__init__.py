from ._anvil_designer import TripTemplate
from anvil import *
import anvil.server
import time

class Trip(TripTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_paarden(self):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1

        M1, M2 = 27, 4
        X , Y = [[],[],[],[],[],[],[], []], [[],[],[],[],[],[],[], []]
        
        for i in range(1,6+1):
            for j in range(0,27+1):
                X[i].append(0) 
                Y[i].append(0)
        
        X[1] = [0, 16, 15.77, 15.32, 14.87, 14.42, 13.97, 13.52, 13.07, 12.62, 12.17, 12.17, 11.95, 10, 11.6, 12.2, 
               13.7, 14.7, 13.5, 12.7, 10.7, 13.5, 14.7, 14.1, 13.7, 13, 14, 16]
        Y[1] = [0, 0, 0.3, -0.3, 0.3, -0.3, 0.3, -0.3, 0.3, -0.3, 0.3, 0.3, 0, 4.6, 5.4, 4, 2.1, 3, 4.5, 6.5, 
                7.5, 10,9.5, 8.7, 8.8, 7.7, 7.2, 9.2]
        
        X[4] = [8, 7.5, 8, 10]
        Y[4] = [4.62, 5.8, 6.2, 4.6]
        for N in range(1,M1+1):
            X[2][N] = -0.5*X[1][N]+0.866*Y[1][N]+16
            Y[2][N] = -0.866*X[1][N]-0.5*Y[1][N]+27.71
            X[3][N] = -0.5*X[1][N]-0.866*Y[1][N]+16
            Y[3][N] = 0.866*X[1][N]-0.5*Y[1][N]
        for N in range(1,M2+1):
            X[5][N] = -0.5*X[1][N]+0.866*Y[1][N]+16
            Y[5][N] = -0.866*X[1][N]-0.5*Y[1][N]+27.71
            X[6][N] = -0.5*X[1][N]-0.866*Y[1][N]+16
            Y[3][N] = 0.866*X[1][N]-0.5*Y[1][N]

        for N2 in range(-1,5+1):
            if N2%2 == 0:
                B = 0
            else:
                B = 1
            for N1 in range(-1,5-B+1):
                X1 = 4+8*B+16*N1
                Y1 = 13.86*N2
                for J in range(1,3+1):
                    P, Q = 150+10*(X1+X[J][1]),150+10*(Y1+Y[J][1])
                    c.move_to(P,Q)
                    for K in range(2,M1+1):
                        P, Q = 150+10*(X1+X[J][K]),150+10*(Y1+Y[J][K])
                        c.line_to(P,Q)
                        time.sleep(.5)
                        c.stroke()
                    time.sleep(1)
                        

    

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_paarden()

        