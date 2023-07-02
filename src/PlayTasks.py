import pywhatkit.misc as kit
import VoiceEngine
import webbrowser as web
import re 
import SpeechRecogniter

def play(strcommand):
        strcommand.replace("play", "")
        if "spotify" in strcommand:
            spotify(strcommand)
        elif "youtube" in strcommand:
            youtube(strcommand)
        else:
            VoiceEngine.say("Sorry, I can't Determine The PlatForm To Play . I support only YouTube and Spotify.")
            VoiceEngine.say("Can You Tell Me Which PlatForm Do You Like To Play The Song")
            command = str(SpeechRecogniter.getinput()).lower()
            if "youtube" in command or "spotify" in command : play(command)
            else : VoiceEngine.say("Sorry I Unable To Play It.")
            
def youtube(strcommand):
        strcommand = re.sub(r"(play|youtube|on)", "", strcommand)
        VoiceEngine.say("Starting YouTube to play " + strcommand)
        kit.playonyt(strcommand)

def spotify( strcommand):
        strcommand = re.sub(r"(play|spotify|on)", "", strcommand)
        VoiceEngine.say("Starting Spotify to play " + strcommand)
        web.open_new_tab("https://open.spotify.com/search/" + strcommand)
