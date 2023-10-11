from ._anvil_designer import RandTemplate
from anvil import *
import anvil.server
import math

class Rand(RandTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
    def teken_randversieringen(self):
        
        H, V, P, Q, N = 120, 90, 1, 1, math.int((H-16)/C)
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1

        C = 12               # horizontale verplaatsing van het moetief
        
        X = [0, 0, 0, 8, 8, 4, 4, 6, 6, 2, 2, 6]
        Y = [0, -8, 8, 8, 2, 2, 4, 4, 6, 6, 0, 0]

        if self.type.selected_value == "T":
            C0 = C
            for I in range(1,2*N):
                self.teken_stuk()
            print("Keuze T")
        if self.type.selected_value == "TH":
            print("Keuze TH")
        if self.type.selected_value== "TV":
            print("Keuze TV")
        if self.type.selected_value == "TC":
            print("Keuze TC")
        if self.type.selected_value == "THV":
            print("Keuze THV")
        if self.type.selected_value == "G":
            print("Keuze G")
        if self.type.selected_value == "GV":
            print("Keuze GV")

 
        
        c.move_to(100+10*X[1],100+10*Y[1])
        for K in range(2,10+1):
            c.line_to(100+10*X[K],100+10*Y[K])
            c.stroke()

    def teken_stuk(self):
        c.move_to(C0*I+10+P*I[1],Q*Y[1])
        for K in range(2,M+1):
            c.line_to(C0*I+10+P*X[K],Q*Y[K])
    
    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_randversieringen()

    def type_change(self, **event_args):
        """This method is called when an item is selected"""
        print("type verandert")
        print(self.type.selected_value)
        self.teken_randversieringen()


            
