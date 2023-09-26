from ._anvil_designer import SymmetrieTemplate
from anvil import *
#import the forms to be displayed
from ..Bloem import Bloem

class Symmetrie(SymmetrieTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.link_1.role = 'selected'
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        
        self.content_panel.clear()
        self.content_panel.add_component(Bloem())

