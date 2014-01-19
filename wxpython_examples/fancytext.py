# wxPython's wx.lib.fancytext can show super and subscripted text
# using XML code
import wx
import wx.lib.fancytext as fancytext

class FancyText(wx.Panel):
  """display fancytext on a panel"""
  def __init__(self, parent):
    wx.Panel.__init__(self, parent, wx.ID_ANY)
    self.Bind(wx.EVT_PAINT, self.OnPaint)

  def OnPaint(self, evt):
    """generate the fancytext on a paint dc canvas"""
    dc = wx.PaintDC(self)
    fancytext.RenderToDC(xml_str, dc, 0, 20)

# the XML code string
xml_str = """\
<font family="swiss" color="blue" size="20">
H<sub>2</sub>O
x<sup>3</sup> + y<sup>2</sup> - 15 = 0
</font>
"""
app = wx.App(0)
frame = wx.Frame(None, wx.ID_ANY, title='wxPython fancy text',
  pos=(100, 50), size=(500, 250))
FancyText(frame)
frame.Show(True)
app.MainLoop()
