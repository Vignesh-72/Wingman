import SpeechRecogniter
import TaskRecogniter
import VoiceEngine

class Assist:
    def __init__(self):
        self.start()

    def start(self):
        VoiceEngine.say("Your Wing Man Is Ready To Help")
        while True:
            command = SpeechRecogniter.getinput()
            if command is None or command == "null": 
                continue
            TaskRecogniter.filltercommand(str(command).lower())

assist = Assist()

