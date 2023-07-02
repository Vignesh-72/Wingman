import speech_recognition as recogniter
import VoiceEngine
import sys

listener = recogniter.Recognizer()
header   = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'}
output   = ""


def getinput():
    command = "null"
    try:
          with recogniter.Microphone() as source:
            print("Ready For Commands")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = str(command).lower()
            print(command)
            VoiceEngine.say(command)

            if command == "stop":
                #stop_event.set()
                pass
            elif command == "exit" or command == "kill" or command == "end process" :
                VoiceEngine.say("Shutding Down")
                sys.exit()

    except Exception as e:
        pass
    
    if command is not None and command != "null" :
        return str(command).lower()
    else:
        getinput()
