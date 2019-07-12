import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 
            pos = wx.DefaultPosition, size = wx.Size(450, 100),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="My Digi Assistant - Psy")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label = "Hello, I am Psy. How may I assist you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, size = [400, 30])
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        
    def onEnter(self, event):
        inp = self.txt.GetValue()
        inp = inp.lower()
        print("It worked !")

if __name__ == "__main__":
    print("Reached Main Function")
    app = wx.App()
    print("Created wx app")
    frame = MyFrame()
    print("Requested to show frame")
    app.MainLoop()

