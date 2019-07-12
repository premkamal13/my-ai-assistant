import wx
import wolframalpha
import wikipedia

import config_reader
from os import system
from time import sleep

# from espeak import espeak
# import pyttsx3
# espeak.synth("Welcome")
# engine = pyttsx3.init()

app_configs = config_reader.getConfigs()
assistant_name = app_configs.assistant_name;
app_id = app_configs.wolfram_app_id;
user_name = app_configs.user_name;

system("say Hi there " + user_name + "!")
sleep(0.2)
system("say I am " + assistant_name)
sleep(0.1)
system("say I will be assisting you today. I can help you with difficult maths problems and GK questions")
sleep(0.5)
system("say Please enter your query in the box!")
# engine.runAndWait()

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
        lbl = wx.StaticText(panel, label = "Hello, I am " + assistant_name +". Ask me some Maths | GK")
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
        query = query.lower().replace("who is", "").replace("what is", "").replace("tell me about", "")
        system("say Interesting question " + user_name + ". Let me do some research on " + query)
        try:
            try:
                # search in wolframalpha
                client = wolframalpha.Client(app_id)
                result = client.query(query)
                answer = next(result.results).text
                print("Here you go...\n-----------------------------------------\n")
                print(answer)
                answer = str(answer).replace("-", " minus ")
                system("say " + answer)
                print("\n-----------------------------------------\n")
            except:
                # search in wikipedia
                if ("detail" not in query and "describe" not in query and "all" not in query):
                    print("I found some results on " + query.upper() + "\n-----------------------------------------\n")
                    answer = wikipedia.summary(query, sentences = 3)
                    print(answer)
                    
                    system("say I have written down what I could find about " + query + " for you. Please check the console.")
                    print("\n ** For A Detailed Search, Query With The Keywords - DETAIL / DESCRIBE / ALL \n")
                else:
                    actual_query = query.replace(" detail ", " ").replace(" describe ", " ").replace(" all ", " ")
                    print("Here is what I found about " + actual_query.upper() + "\n-----------------------------------------\n")
                    answer = wikipedia.summary(actual_query)
                    print(answer)
                    system("say I wrote down the detailed results for you. Please check the console.") 
                print("\n-----------------------------------------\n")
        except:
            answer = "Ummm sorry! I don't know this one. Can i answer another question?"
            print(answer)
            system("say " + answer)    
        sleep(0.8)
        system("say You can enter another query when you are ready!")

if __name__ == "__main__":
    # print("Reached Main Function")
    app = wx.App()
    # print("Created wx app")
    frame = MyFrame()
    # print("Requested to show frame")
    app.MainLoop()

