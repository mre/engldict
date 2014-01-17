import wx

class MyFrame(wx.Frame):
  def __init__(self, parent, id):
    wx.Frame.__init__(self, parent, id, "Hide test", size=(160,160))

    # create widgets
    self.pnl = myPanel(self)
    self.Layout()

class myPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        #bitmap = wx.EmptyBitmap(15,15)
        #self.button = wx.BitmapButton(self, -1, bitmap=bitmap, size=(15,15), style=wx.NO_BORDER)
        #self.Bind(wx.EVT_BUTTON, self.onClick, self.button)

    def onClick(self, event):
        print "haaa"
        self.Hide()


app = wx.PySimpleApp()
p = myPanel(None, -1)
p.Show()
app.MainLoop()
