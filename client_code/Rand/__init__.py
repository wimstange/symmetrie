from ._anvil_designer import RandTemplate
from anvil import *
import anvil.server
import math

class Rand(RandTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        self.M = 11
        self.C = 12               # horizontale verplaatsing van het moetief
        self.C0 = self.C
        self.H, self.V, self.P, self.Q = 120, 90, 1, 1
        self.N = int((self.H-16)/self.C)
        self.X = [0, 0, 0, 8, 8, 4, 4, 6, 6, 2, 2, 6]
        self.Y = [0, -8, 8, 8, 2, 2, 4, 4, 6, 6, 0, 0]
        
    def teken_randversieringen(self):

        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1
 
        if self.type.selected_value == "T":
            self.C0 = self.C
            for I in range(1,2*self.N):
                self.teken_stuk(I)
            print("Keuze T")
        if self.type.selected_value == "TH":
            print("Keuze TH")
            self.C0 = self.C
            for I in range(1,2*self.N):
                self.teken_stuk(I)
                self.Q = -self.Q
                self.teken_stuk(I)
            
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

 
        
        # c.move_to(100+10*X[1],100+10*Y[1])
        # for K in range(2,10+1):
        #    c.line_to(100+10*X[K],100+10*Y[K])
        #    c.stroke()

    def teken_stuk(self,I):
        c = self.canvas_1
        S , T = self.C0*I+10+self.P*self.X[1], self.Q*self.Y[1]
        c.move_to(10+10*S,10+10*T)
        for K in range(2,self.M+1):
            S, T = self.C0*I+10+self.P*self.X[K], self.Q*self.Y[K]
            c.line_to(10+10*S, 10+10*T)
            c.stroke()
        return
    
    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_randversieringen()

    def type_change(self, **event_args):
        """This method is called when an item is selected"""
        print("type verandert")
        print(self.type.selected_value)
        self.teken_randversieringen()


            
