import subprocess

def say(text):
   subprocess.call(['say', text])

say("Hello Bing! How have you been?")

