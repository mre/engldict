import math
from threading import Thread
import time
import wx

e = lambda x: complex(math.cos(x), 0) + complex(0, math.sin(x))
r = lambda x: ((e(0*math.pi/3.0)*e(x)).real + 1)/2.0
g = lambda x: ((e(2*math.pi/3.0)*e(x)).real + 1)/2.0
b = lambda x: ((e(4*math.pi/3.0)*e(x)).real + 1)/2.0
colo = lambda rad: map(lambda x: int(128 * x(rad)), [r, g, b])

class DisplayText(wx.Dialog):

    def __init__(self, parent, text="", displayMode=0):

        # Initialize dialog
        wx.Dialog.__init__(self, parent, size=(480, 320), style=( wx.DIALOG_EX_METAL | wx.STAY_ON_TOP ) )

        # Freeze UI so user won't see stuff flashing
        self.Freeze()

        # (For Mac) Setup a panel
        self.panel = wx.Panel(self, size=(480, 320))
        self.panel.SetBackgroundColour(wx.Colour(0, 0, 128))
        self.panel.SetBackgroundColour(wx.Colour(*colo(0)))

        # Setup sizer for vertical centering
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)

        # Create text field
        self.txtField = wx.StaticText(self.panel, size=(448, -1), style=(wx.ALIGN_CENTRE_HORIZONTAL | wx.TE_MULTILINE ))
        self.txtField.SetFont(wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))      
        self.txtField.SetForegroundColour(wx.Colour(255, 255, 255))
        self.txtField.SetLabel(text)
        self.txtField.Wrap(448)
        self.sizer.Add(self.txtField, 1, 0, 15)

        # Add the static text to the sizer
        # Ensure layouts are applied
        self.panel.Layout()
        self.panel.Refresh()

        # Thaw UI
        self.Thaw()

        # Center form
        self.Center()

        self.angle = 0
        self.angle_inc = (2*math.pi)/25.0

    def change_colour(self):
        t = Thread(target=self.epilepsy_mode)
        t.start() 

    def epilepsy_mode(self):
        while True:
            time.sleep(0.02)
            self.panel.SetBackgroundColour(wx.Colour(*colo(self.angle)))
            self.panel.Refresh()
            self.angle = (self.angle + self.angle_inc) % (2*math.pi)

app = wx.App(False)

c = DisplayText(None, text="Now is the time for all good men to come to the aid of their country.")
c.Show()
#import wx.lib.inspection 
#wx.lib.inspection.InspectionTool().Show() 
c.change_colour()

app.MainLoop()
