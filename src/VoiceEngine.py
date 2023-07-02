import pyttsx3 as speech
engine   = speech.init()
voice    = engine.getProperty("voices")

def say(command):
    engine.say(command)
    engine.runAndWait()