from ._anvil_designer import TripTemplate
from anvil import *
import anvil.server

class Trip(TripTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_paarden(self):
        X , Y = [[],[],[],[],[],[], []], [[],[],[],[],[],[], []]
        X[1] = [0, 6, 15.77, 15.32, 4.87, 14.42, 3.97, 3.53, 13.07, 12.62, 12.17, 12.17, 11.95, 10, 1.6, 12.2, 
               13.7, 14.7, 13.5, 12.7, 10.7, 13.5, 14.7, 14.1, 13.7, 13, 14, 16]
        Y[1] = [0, 0, 0.3, -0.3, 0.3, -0.3, 0.3, -0.3, 0.3, -0.3, 0.3, 0.3, 0, 4.6, 5.4, 4, 2.1, 3, 4.5, 6.5, 
                7.5, 10,9.5, 8.7, 8.8, 7.7, 17.2, 19.2]
        print(len(X[1]), len(Y[1]))

        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1
        c.move_to(X[1][1],Y[1][1])
        for K in rangec.line_to([X[1][K],Y[1][K]])

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_paarden()

        