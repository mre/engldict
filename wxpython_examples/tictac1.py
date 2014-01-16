"""
Author: Daniel Gopar
Contact: gopardaniel<at>yahooo<dot>com

Project: Tic Tac Toe GUI made in WxPython.
"""
import wx
import wx.lib.buttons as buttons
import random

class GamePanel(wx.Panel):
    """ Panel where game will be """
    #---------------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #self.SetBackgroundColour('WHITE')
        self.isPlayerX = True
        self.playerX_score = 0
        self.playerO_score = 0
        self.isComputer = True
        
        # Call methods
        self.createSizer()
        self.createFont()
        self.createText()
        self.createButtons()
        self.bindEvents()
        self.addSizerContent()
        
        # Set the panels main Sizer
        self.SetSizer(self.main_sizer)
    
    #---------------------------------------------------------------------------
    def createSizer(self):
        """ Create Main sizer """
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
    #---------------------------------------------------------------------------
    def createText(self):
        """ Create Text that keeps score """
        self.playerX_score_text = wx.StaticText(self, -1,
                                "Player X Score:\n%s" % self.playerX_score)
        self.playerO_score_text = wx.StaticText(self, -1,
                                "Player O Score:\n%s" % self.playerO_score)
        self.playerO_score_text.SetFont(self.score_font)
        self.playerX_score_text.SetFont(self.score_font)
        
        self.score_sizer = wx.BoxSizer()
        self.score_sizer.Add(self.playerX_score_text, 0, wx.RIGHT, 10)
        self.score_sizer.Add(self.playerO_score_text, 0, wx.LEFT, 10)
        
    #---------------------------------------------------------------------------
    def createFont(self):
        """ Create fonts to be used """
        self.btn_font = wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)
        self.score_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)
    #---------------------------------------------------------------------------
    def createButtons(self):
        """ Create buttons to be used in game """
        # Crate grid sizer for buttons
        self.btn_sizer = wx.GridSizer(rows=3, cols=3, vgap=5, hgap=5)
        
        # Create buttons for game
        self.btn1 = buttons.GenToggleButton(self,size=(100,100))
        self.btn2 = buttons.GenToggleButton(self,size=(100,100))
        self.btn3 = buttons.GenToggleButton(self,size=(100,100))
        self.btn4 = buttons.GenToggleButton(self,size=(100,100))
        self.btn5 = buttons.GenToggleButton(self,size=(100,100))
        self.btn6 = buttons.GenToggleButton(self,size=(100,100))
        self.btn7 = buttons.GenToggleButton(self,size=(100,100))
        self.btn8 = buttons.GenToggleButton(self,size=(100,100))
        self.btn9 = buttons.GenToggleButton(self,size=(100,100))
        
        # Get normal button color
        self.normal_btn_color = self.btn1.GetBackgroundColour()
        
        # Add buttons to a list
        self.btn_list = [self.btn1, self.btn2, self.btn3,
                         self.btn4, self.btn5, self.btn6,
                         self.btn7, self.btn8, self.btn9]
                        
                         # Horizontal Wins
        self.btn_wins = [(self.btn1, self.btn2, self.btn3),
                         (self.btn4, self.btn5, self.btn6),
                         (self.btn7, self.btn8, self.btn9),
                         # Vertical Wins
                         (self.btn1, self.btn4, self.btn7),
                         (self.btn2, self.btn5, self.btn8),
                         (self.btn3, self.btn6, self.btn9),
                         # Diagnol wins
                         (self.btn1, self.btn5, self.btn9),
                         (self.btn3, self.btn5, self.btn7)]
        
        # Add buttons to btn_sizer and set font for each button
        for btn in self.btn_list:
            btn.SetFont(self.btn_font)
            self.btn_sizer.Add(btn)
            self.Bind(wx.EVT_BUTTON, self.onToggle, btn)
    
        self.restart_btn = wx.Button(self, -1, "Restart Game")
    
    #---------------------------------------------------------------------------
    def bindEvents(self):
         """ Bind Events """
         self.Bind(wx.EVT_BUTTON, self.onRestart, self.restart_btn)
        
    #---------------------------------------------------------------------------
    def addSizerContent(self):
        """ Add things to main sizer """
        self.main_sizer.Add(self.btn_sizer, 0, wx.ALIGN_CENTER|wx.TOP, 10)
        self.main_sizer.Add((-1, 15))
        self.main_sizer.Add(self.restart_btn, 0, wx.ALIGN_CENTER)
        self.main_sizer.Add((-1, 10))
        self.main_sizer.Add(self.score_sizer, 0, wx.ALIGN_CENTER)
        
    #---------------------------------------------------------------------------
    def onRestart(self, event=None):
        """ Restart the game """
        for btn in self.btn_list:
            btn.SetLabel("")
            btn.SetValue(False)
            btn.Enable()

        self.isPlayerX = True
    #---------------------------------------------------------------------------
    def onToggle(self, event):
        """ When a button is pressed mark it with X or O """
        btn = event.GetEventObject()
        if self.isPlayerX:
            btn.SetLabel("X")
        else:
            btn.SetLabel("O")
        btn.Disable()
        # If player won then end method
        if self.checkWin():
            return
        
        # if computer is playing then do this
        if self.isComputer:
            self.computerMove()
            self.checkWin()
        # if its a player vs player then this
        else:
            self.isPlayerX = not self.isPlayerX
        
    #--------------------------------------------------------------------------
    def checkWin(self):
        """ Check if anyone has won """
        # Loop through the list of possible wins
        for btn1, btn2, btn3 in self.btn_wins:
            if btn1.GetLabel() == btn2.GetLabel() == btn3.GetLabel() and \
                btn3.GetLabel() in ("X","O"):
                # Change color to show where winner won
                self.changeButtonColor(btn1,btn2,btn3,"BLUE")
                # Display the winner in a message
                if btn1.GetLabel() == "X":
                    winner = "X"
                    wx.MessageBox("Player X Wins!", "WINNER")
                else:
                    winner = "O"
                    wx.MessageBox("Player O Wins!", "WINNER")
                # Change colors back to normal
                self.changeButtonColor(btn1,btn2,btn3)
                # Update the score of the winners
                self.updateScore(winner)
                # Winner found
                return True
        # No win
        return False
                    
    #---------------------------------------------------------------------------
    def updateScore(self, winner):
        """ Add to the winners score """
        # Player X is playing against someone else and NOT the computer
        if winner == "X":
            self.playerX_score += 1
            self.playerX_score_text.SetLabel("Player X Score:\n%s" \
                                             % self.playerX_score)
        else:
            self.playerO_score += 1
            self.playerO_score_text.SetLabel("Player O Score:\n%s" \
                                             % self.playerO_score)
        self.onRestart()
    
    #---------------------------------------------------------------------------
    def changeButtonColor(self,btn1, btn2, btn3, color=None):
        """ Change button color to tell user where the winning spots are """
        if color == None:
            color = self.normal_btn_color
        
        btn1.SetBackgroundColour(color)
        btn2.SetBackgroundColour(color)
        btn3.SetBackgroundColour(color)
        self.Refresh()
        
    #---------------------------------------------------------------------------
    def computerMove(self):
        """ Computer chooses best option for move """
        # Loop through the list of possible wins
        for btn_tupple in self.btn_wins:
            xcount = 0
            ocount = 0
            for btn in btn_tupple:
                if btn.GetLabel() == "X":
                    xcount += 1
                elif btn.GetLabel() == "O":
                    ocount += 1
                else: button = btn
            # If possible score for opponent or computer then take it
            if xcount == 2 or ocount == 2:
                try:
                    button.SetLabel("O")
                    button.Disable()
                    button.SetValue(True)
                except:
                    # Some positions are not possible so resort to this
                    self.randMove()
                return
    
        # Select random spot for first couple of moves
        self.randMove()
        
    #---------------------------------------------------------------------------
    def randMove(self):
        """ Play a random move """
        # Get a random move, repeat until you get a button that is not used
        while True:
            rand = random.randint(0,len(self.btn_list)-1)
            if self.btn_list[rand].IsEnabled():
                self.btn_list[rand].SetLabel("O")
                self.btn_list[rand].Disable()
                self.btn_list[rand].SetValue(True)
                break
        
class Frame(wx.Frame):
    """ Frame that will hold game """
    #---------------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Tic Tac Toe", size=(400,500))
        self.pnl = GamePanel(self)
        
        
if __name__ == "__main__":
    app = wx.App(False)
    f = Frame()
    f.Show()
    app.MainLoop()
