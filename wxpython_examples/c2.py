#!/usr/bin/env python
import wx

class MainApp(wx.App):
        def OnInit(self):

                self.frame = wx.Frame(None, wx.ID_ANY, size=((400,400)))
                self.vbox = wx.BoxSizer(wx.VERTICAL)

                self.textItem = wx.StaticText(parent=self.frame, label="THIS IS A \
LABEL.", size=((200,50)), pos=((100,100)), style=wx.ALIGN_CENTER|
wx.SIMPLE_BORDER)
                self.textItem.SetBackgroundColour(wx.WHITE)
                self.textItem.SetForegroundColour(wx.BLACK)

                self.vbox.Add(item=self.textItem, flag=wx.ALIGN_CENTER_VERTICAL)

                self.frame.SetSizer(self.vbox)

                self.frame.Show()
                self.frame.Refresh()
                return True

if __name__ == '__main__':
        app = MainApp(False)
        import wx.lib.inspection
        wx.lib.inspection.InspectionTool().Show()
        app.MainLoop()

