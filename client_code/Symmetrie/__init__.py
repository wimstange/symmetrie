from ._anvil_designer import SymmetrieTemplate
from anvil import *
import anvil.server
#import the forms to be displayed
from ..Bloem import Bloem
from ..Wervel import Wervel
from ..Cycloide import Cycloide
from ..Rand import Rand
from ..Moskeeraam import Moskeeraam
from ..Kwadraattegel import Kwadraattegel
from ..Stertegel import Stertegel
from ..Trip import Trip

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

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.link_1.role = ''
        self.link_2.role = 'selected'
        self.link_3.role = ''
        self.link_4.role = ''
        
        self.content_panel.clear()
        self.content_panel.add_component(Wervel())

    def link_3_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = 'selected'
        self.link_4.role = ''
        
        self.content_panel.clear()
        self.content_panel.add_component(Cycloide())

    def link_4_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = 'selected'

        self.content_panel.clear()
        self.content_panel.add_component(Rand())
        

    def link_5_click(self, **event_args):
        """This method is called when the link is clicked"""
        """This method is called when the link is clicked"""
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = 'selected'
        
        self.content_panel.clear()
        self.content_panel.add_component(Moskeeraam())

    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = 'selected'
        self.link_7.role = ''
        self.link_8.role = ''
        self.link_9.role = ''
        self.link_10.role = ''
        self.link_11.role = ''

        self.content_panel.clear()
        self.content_panel.add_component(Kwadraattegel())
        
    def link_7_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.alert("Deze optie is nog niet beschikbaar","Helaas ...")
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = ''
        self.link_7.role = 'selected'
        self.link_8.role = ''
        self.link_9.role = ''
        self.link_10.role = ''
        self.link_11.role = ''

    def link_8_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.alert("Deze optie is nog niet beschikbaar",title="Helaas ...")
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = ''
        self.link_7.role = ''
        self.link_8.role = 'selected'
        self.link_9.role = ''
        self.link_10.role = ''
        self.link_11.role = ''

    def link_9_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.alert("Deze optie is nog niet beschikbaar",title="Helaas ...")
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = ''
        self.link_7.role = ''
        self.link_8.role = ''
        self.link_9.role = 'selected'
        self.link_10.role = ''
        self.link_11.role = ''

    def link_10_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.alert("Deze optie is nog niet beschikbaar",title="Helaas ...")
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = ''
        self.link_7.role = ''
        self.link_8.role = ''
        self.link_9.role = ''
        self.link_10.role = 'selected'
        self.link_11.role = ''

    def link_11_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.alert("Deze optie is nog niet beschikbaar",title="Helaas ...")
        self.link_1.role = ''
        self.link_2.role = ''
        self.link_3.role = ''
        self.link_4.role = ''
        self.link_5.role = ''
        self.link_6.role = ''
        self.link_7.role = ''
        self.link_8.role = ''
        self.link_9.role = ''
        self.link_10.role = ''
        self.link_11.role = 'selected'
        







