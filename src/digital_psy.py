import wx
import wolframalpha
import wikipedia

class MyFrame(wx.Frame):

    def __init__(self):
        global query_cnt
        query_cnt = 0
        wx.Frame.__init__(self, None, 
            pos = wx.DefaultPosition, size = wx.Size(550, 150),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="My Digi Assistant - Psy")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label = "Hello, I am Psy. Ask me some Maths | GK")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, size = [500, 50])
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        
    def onEnter(self, event):
        global query_cnt
        query_cnt = query_cnt + 1
        print("\n* QUERY NO. " + str(query_cnt) + "\n")
        query = self.txt.GetValue()
        query = query.lower()
        print("Wait for a moment. Let me do a little bit of research...\n")
        try:
            try:
                # search in wolframalpha
                app_id = "DEMO"
                client = wolframalpha.Client(app_id)
                result = client.query(query)
                answer = next(result.results).text
                print("Here you go...\n-----------------------------------------\n")
                print(answer)
                print("\n-----------------------------------------\n")
            except:
                query = query.replace("who is", "").replace("what is", "").replace("tell me about", "")
                # search in wikipedia
                if ("detail" not in query and "describe" not in query and "all" not in query):
                    print("Here is what I found about " + query.upper() + "\n-----------------------------------------\n")
                    print(wikipedia.summary(query, sentences = 3))
                    print("\n ** For A Detailed Search, Query With The Keywords - DETAIL / DESCRIBE / ALL \n")
                else:
                    actual_query = query.replace(" detail ", " ").replace(" describe ", " ").replace(" all ", " ")
                    print("Here is what I found about " + actual_query.upper() + "\n-----------------------------------------\n")
                    print(wikipedia.summary(actual_query)) 
                print("\n-----------------------------------------\n")
        except:
            print("Oops! This is not in my Knowledge base. Try rephrasing / something else")    

if __name__ == "__main__":
    # print("Reached Main Function")
    app = wx.App()
    # print("Created wx app")
    frame = MyFrame()
    # print("Requested to show frame")
    app.MainLoop()

