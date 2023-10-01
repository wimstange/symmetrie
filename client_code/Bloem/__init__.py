from ._anvil_designer import BloemTemplate
from anvil import *
import anvil.server
import math
import anvil.media

class Bloem(BloemTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
 
        self.teken_bloem(self.text_box_1.text,
                        self.text_box_2.text,
                        self.text_box_3.text,
                        self.text_box_4.text,
                        self.text_box_5.text)

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""

        img = self.canvas_1.get_image()
        anvil.media.download(img)

        # gebruik makend van server module, een upgrade nodig?
        # img = self.canvas_1.get_image()
        # filename = 'bloem.jpg'  # Hier kunt u de gewenste bestandsnaam instellen
        # anvil.server.call('save_image_with_name', img, filename)

        # gebruik maken van een zelf gedefinieerde client functie, (nog?) niet geimpementeerd in anvil.works        
        # img = self.canvas_1.get_image()
        # filename = 'bloem.jpg'  # Hier kunt u de gewenste bestandsnaam instellen
        # self.opslaan(img, filename)

    def canvas_1_reset(self, **event_args):
        """This method is called when the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form."""
        self.teken_bloem(self.text_box_1.text,
                        self.text_box_2.text,
                        self.text_box_3.text,
                        self.text_box_4.text,
                        self.text_box_5.text)
        
        
    def teken_bloem(self,A,B,C,M,N):
        c = self.canvas_1
        c.clear_rect(0,0,self.canvas_1.get_width(),self.canvas_1.get_height()) 
        c.begin_path()
        c.stroke_style = "rgba(0,0,0,1)"    # ""#2196F3"
        c.line_width = 1
        
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

    def opslaan(self,image,bestandsnaam):
        with open(bestandsnaam, 'wb') as file:
            file.write(image.get_bytes())