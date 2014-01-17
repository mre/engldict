import random
import wx
import wx.lib.buttons as buttons

########################################################################
class TTTPanel(wx.Panel):
    """
Tic-Tac-Toe Panel object
"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """
Initialize the panel
"""
        wx.Panel.__init__(self, parent)
        self.toggled = False
        self.playerWon = False
        
        self.layoutWidgets()
        
    #----------------------------------------------------------------------
    def checkWin(self, computer=False):
        """
Check if the player won
"""
        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and \
               button2.GetLabel() == button3.GetLabel() and \
               button1.GetLabel() != "":
                print "Player wins!"
                self.playerWon = True
                button1.SetBackgroundColour("Yellow")
                button2.SetBackgroundColour("Yellow")
                button3.SetBackgroundColour("Yellow")
                self.Layout()
                
                if not computer:
                    msg = "You Won! Would you like to play again?"
                    dlg = wx.MessageDialog(None, msg, "Winner!",
                                           wx.YES_NO | wx.ICON_WARNING)
                    result = dlg.ShowModal()
                    if result == wx.ID_YES:
                        wx.CallAfter(self.restart)
                    dlg.Destroy()
                    break
                else:
                    return True
        
    #----------------------------------------------------------------------
    def layoutWidgets(self):
        """
Create and layout the widgets
"""
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)
        
        size = (100,100)
        self.button1 = buttons.GenToggleButton(self, size=size, name="btn1")
        self.button2 = buttons.GenToggleButton(self, size=size, name="btn2")
        self.button3 = buttons.GenToggleButton(self, size=size, name="btn3")
        self.button4 = buttons.GenToggleButton(self, size=size, name="btn4")
        self.button5 = buttons.GenToggleButton(self, size=size, name="btn5")
        self.button6 = buttons.GenToggleButton(self, size=size, name="btn6")
        self.button7 = buttons.GenToggleButton(self, size=size, name="btn7")
        self.button8 = buttons.GenToggleButton(self, size=size, name="btn8")
        self.button9 = wx.BitmapButton(self, wx.ID_ANY, self.contbmp, pos=(150,300), style=wx.NO_BORDER)
        self.normalBtnColour = self.button1.GetBackgroundColour()
        

        self.widgets = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6,
                        self.button7, self.button8, self.button9]
        
        # change all the main game buttons' font and bind them to an event
        for button in self.widgets:
            button.SetFont(font)
            button.Bind(wx.EVT_BUTTON, self.onToggle)
                    
        # add the widgets to the sizers
        self.fgSizer.AddMany(self.widgets)
        mainSizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        
        self.endTurnBtn = wx.Button(self, label="End Turn")
        self.endTurnBtn.Bind(wx.EVT_BUTTON, self.onEndTurn)
        self.endTurnBtn.Disable()
        btnSizer.Add(self.endTurnBtn, 0, wx.ALL|wx.CENTER, 5)
        
        startOverBtn = wx.Button(self, label="Restart")
        startOverBtn.Bind(wx.EVT_BUTTON, self.onRestart)
        btnSizer.Add(startOverBtn, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        
        self.methodsToWin = [(self.button1, self.button2, self.button3),
                             (self.button4, self.button5, self.button6),
                             (self.button7, self.button8, self.button9),
                             # vertical ways to win
                             (self.button1, self.button4, self.button7),
                             (self.button2, self.button5, self.button8),
                             (self.button3, self.button6, self.button9),
                             # diagonal ways to win
                             (self.button1, self.button5, self.button9),
                             (self.button3, self.button5, self.button7)]
        
        self.SetSizer(mainSizer)
        
    #----------------------------------------------------------------------
    def enableUnusedButtons(self):
        """
Re-enable unused buttons
"""
        for button in self.widgets:
            if button.GetLabel() == "":
                button.Enable()
        self.Refresh()
        self.Layout()
        
    #----------------------------------------------------------------------
    def onEndTurn(self, event):
        """
Let the computer play
"""
        # rest toggled flag state
        self.toggled = False
        
        # disable all played buttons
        for btn in self.widgets:
            if btn.GetLabel():
                btn.Disable()
        
        computerPlays = []
        noPlays = []
        
        for button1, button2, button3 in self.methodsToWin:
            if button1.GetLabel() == button2.GetLabel() and button3.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    #if button1.GetLabel() == "O":
                    noPlays.append(button3)
                
            elif button1.GetLabel() == button3.GetLabel() and button2.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    noPlays.append(button2)
                
            elif button2.GetLabel() == button3.GetLabel() and button1.GetLabel() == "":
                if button1.GetLabel() == "" and button2.GetLabel() == "" and button1.GetLabel() == "":
                    pass
                else:
                    noPlays.append(button1)
                    
            noPlays = list(set(noPlays))
            
            if button1.GetLabel() == "" and button1 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button1)
                    
            if button2.GetLabel() == "" and button2 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button2)
                    
            if button3.GetLabel() == "" and button3 not in noPlays:
                if not self.checkWin(computer=True):
                    computerPlays.append(button3)
                    
        
        computerPlays = list(set(computerPlays))
        print noPlays
        choices = len(computerPlays)
        while 1 and computerPlays:
            btn = random.choice(computerPlays)
            
            if btn not in noPlays:
                print btn.GetName()
                btn.SetLabel("O")
                btn.Disable()
                break
            else:
                print "Removed => " + btn.GetName()
                computerPlays.remove(btn)
            if choices < 1:
                self.giveUp()
                break
            choices -= 1
        else:
            # Computer cannot play without winning
            self.giveUp()
        
        self.endTurnBtn.Disable()
        self.enableUnusedButtons()
        
    #----------------------------------------------------------------------
    def giveUp(self):
        """
The computer cannot find a way to play that lets the user win,
so it gives up.
"""
        msg = "I give up, Dave. You're too good at this game!"
        dlg = wx.MessageDialog(None, msg, "Game Over!",
                               wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            self.restart()
        else:
            wx.CallAfter(self.GetParent().Close)
        dlg.Destroy()
        
    #----------------------------------------------------------------------
    def onRestart(self, event):
        """
Calls the restart method
"""
        self.restart()
                
    #----------------------------------------------------------------------
    def onToggle(self, event):
        """
On button toggle, change the label of the button pressed
and disable the other buttons unless the user changes their mind
"""
        button = event.GetEventObject()
        button.SetLabel("X")
        button_id = button.GetId()
        
        self.checkWin()
        if not self.toggled:
            self.toggled = True
            self.endTurnBtn.Enable()
            for btn in self.widgets:
                if button_id != btn.GetId():
                    btn.Disable()
        else:
            self.toggled = False
            self.endTurnBtn.Disable()
            button.SetLabel("")
            self.enableUnusedButtons()
            
        # check if it's a "cats game" - no one's won
        if not self.playerWon:
            labels = [True if btn.GetLabel() else False for btn in self.widgets]
            if False not in labels:
                msg = "Cats Game - No one won! Would you like to play again?"
                dlg = wx.MessageDialog(None, msg, "Game Over!",
                                       wx.YES_NO | wx.ICON_WARNING)
                result = dlg.ShowModal()
                if result == wx.ID_YES:
                    self.restart()
                dlg.Destroy()
                
    #----------------------------------------------------------------------
    def restart(self):
        """
Restart the game and reset everything
"""
        for button in self.widgets:
            button.SetLabel("")
            button.SetValue(False)
            button.SetBackgroundColour(self.normalBtnColour)
        self.toggled = False
        self.playerWon = False
        self.endTurnBtn.Disable()
        self.enableUnusedButtons()
            
########################################################################
class TTTFrame(wx.Frame):
    """
Tic-Tac-Toe Frame object
"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        title = "Tic-Tac-Toe"
        size = (500, 500)
        wx.Frame.__init__(self, parent=None, title=title, size=size)
        panel = TTTPanel(self)
        
        self.Show()
        
if __name__ == "__main__":
    app = wx.App(False)
    frame = TTTFrame()
    app.MainLoop()
    
