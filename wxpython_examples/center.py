#!/usr/bin/env python

import wx
from wx.lib.wordwrap import wordwrap

class MYGUI(wx.App):
    def OnInit(self):
        self.frame = Frame(None, title = "My GUI")
        self.frame.CenterOnScreen()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = wx.Panel(self, -1)
        sizex, sizey = 104, 80
        buttonLabel = "Two\n".center(8) + "Lines".center(8)
        txt = "I'm as clever as you."
        wrapped_txt = wordwrap(txt, sizex, wx.ClientDC(self))

        print wrapped_txt
        button = wx.Button(parent = panel, id = wx.ID_ANY, label = buttonLabel,
                           size = (sizex, sizey))
        #self.Centre()

if __name__ == "__main__":

    app = MYGUI()
    app.MainLoop()

