import wx
from wx.lib.buttons import GenBitmapTextButton
from wx.lib.fancytext import RenderToBitmap as fancy_render

class Gui(wx.App):
  """ A simple wxpython app """
  def OnInit(self):
    self.frame = Frame(None, title = "Vocabulary Trainer")
    self.frame.CenterOnScreen()
    self.frame.Show()
    return True

class Frame(wx.Frame):
  """ Main frame for the application """
  def __init__(self, *args, **kwargs):
    wx.Frame.__init__(self, *args, **kwargs)
    self.panel = MainPanel(self)


class MainPanel(wx.Panel):
  """ Main panel for the application """
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)

    # Setup
    self.createSizer()
    self.createFonts()
    self.createButtons()
    #self.bindEvents()
    self.addSizerContent()

    # Set the panels main Sizer
    self.SetSizer(self.main_sizer)

  def createSizer(self):
    """ Create Main sizer """
    self.main_sizer = wx.BoxSizer(wx.VERTICAL)

  def createFonts(self):
    """ Create fonts to be used """
    self.btn_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                   wx.FONTWEIGHT_NORMAL)

  def render(self, txt, word=None):
    if word:
      highlight = "<font style='italic' weight='bold' color='red' family='swiss'>" + word + "</font>"
      txt = txt.replace(word, highlight)
    return fancy_render(txt)

  def question_button(self, txt, word, size=(200,200)):
    btn = GenBitmapTextButton(self, bitmap=self.render(txt, word), label="\n", size=size)
    btn.SetBackgroundColour('#c2e6f8')
    return btn

  def answer_button(self, txt, size=(200,200)):
    btn = GenBitmapTextButton(self, bitmap=self.render(txt), label="\n", size=size)
    btn.SetBackgroundColour('#fcff9c')
    return btn

  def createButtons(self):
    """ Create buttons to be used in game """
    # Create grid sizer for buttons
    self.btn_sizer = wx.GridSizer(rows=3, cols=3, vgap=0, hgap=0)
    
    # Create buttons
    size = (200,200)
    # Use bitmap buttons in case we want to add a nice icon later on
    word = "nice"
    txt ="Use bitmap buttons in case\n we want to add a\n nice icon later on"
    q = self.question_button(txt, word)
    self.btn_sizer.Add(q)
    a = self.answer_button(txt)
    self.btn_sizer.Add(a)
    #self.Bind(wx.EVT_BUTTON, self.onToggle, email)

    #self.btn1 = buttons.GenToggleButton(self,size=size, style=wx.NO_BORDER|wx.ALIGN_CENTRE)
    #self.btn9 = wx.Button(self, id=wx.ID_ANY, label="test", size=size, style=wx.NO_BORDER)
    #self.btn9 = wx.BitmapButton(self, wx.ID_ANY, self.contbmp, pos=(150,300), style=wx.NO_BORDER)
    #self.btn1.SetBackgroundColour("Blue")

    # Add buttons to a list
    """
    self.btn_list = [self.btn1, self.btn2, self.btn3,
                     self.btn4, self.btn5, self.btn6,
                     self.btn7, self.btn8, self.btn9]

    Add buttons to btn_sizer and set font for each button
    for btn in self.btn_list:
        btn.SetFont(self.btn_font)
        btn.setBackgroundColor("#9aeafe")
        self.btn_sizer.Add(btn)
        self.Bind(wx.EVT_BUTTON, self.onToggle, btn)
    """

  def addSizerContent(self):
      """ Add things to main sizer """
      self.main_sizer.Add(self.btn_sizer, 0, wx.ALIGN_CENTER|wx.TOP, 10)
      self.main_sizer.Add((-1, 15))
      #self.main_sizer.Add(self.restart_btn, 0, wx.ALIGN_CENTER)
      #self.main_sizer.Add((-1, 10))
      #self.main_sizer.Add(self.score_sizer, 0, wx.ALIGN_CENTER)

if __name__ == "__main__":
  app = Gui()
  app.MainLoop()
