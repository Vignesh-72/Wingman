import pywhatkit.misc as kit
import PlayTasks as player
import GPTModel
import VoiceEngine
import SpeechRecogniter

def filltercommand(command):

      print(command)
      if "hey computer" in command:
          command = command.replace("hey computer", "")
          if "play" in command:
             player.play(command)
             return
          if "open" in command:
              GPTModel.google(command.replace("open", ""))
              return
          if "use query search  " in command:
              GPTModel.querysearch(command)
              return
          if "wikipedia" in command:
              GPTModel.wiki(command)
              return
          if "google search" in command :
              GPTModel.querysearch(command)
              return
          if "take screenshot" in command or "take a screenshot" in command:
              kit.take_screenshot()   
              return
          if "take web screenshot" in command or "take a web screenshot" in command:
              kit.web_screenshot(((str(command).lower()).replace("take","").replace("web","").replace("a","")))
          GPTModel.gpt2(command)
          if "what can you do" in command or "help" in command:
              VoiceEngine.say("I Can Be Your Trusable Personal Assistant I Can Help You With")
              VoiceEngine.say("I Can Open Any Website By Your Voice Command Just Say Open And The Website You Want To Open It")
              VoiceEngine.say("I Can Answer  Any Music By Your Voice Command Just Say Play And The Name Of The Song To Play It . You Can Provide Additional Command Such As Youtube Or Spotify So I Will Play The Song On That Platform You Specified")
              VoiceEngine.say("I Can Answer Your Question By Using GPT Modle And I Can Use Google Search And WikiPeadia To Find Answers To Your Questions")
              VoiceEngine.say("To Do A Google Search You Can Say Google Search About And What You What , And Same Goes For Wikipedia Tell Wikipedia And What You Want To Know")
              VoiceEngine.say("I Can Send Whatapp Message And Take Screenshot and read notification")
              VoiceEngine.say("At A Nutshell Im A simple and light weight AI Personal Assistant ") 
              return
          if "guide me" in command:
              VoiceEngine.say("Sure I will guide you so you can use my full potential, let start")
              VoiceEngine.say("First You Need A HuggingFace User Access Token do you have it")
              command = str(SpeechRecogniter.getinput()).lower()
              if "i have" in command or "i got " in command or "yes" in command:   
                VoiceEngine.say("After You Got The User Access Token Open My Folder Which Will Be Located At C Drive And A Open The File Named dot env and paste the access token to next huggingface api key , and your done ")
                return
              else:
                  VoiceEngine.say("Do You Like Me to open the tutorial page on how to get huggingface user access token ")
                  command = str(SpeechRecogniter.getinput()).lower()
                  if "yes" in command or "sure" in command or "open" in command:
                      GPTModel.google("https://huggingface.co/docs/hub/security-tokens")
                      return
                  else:
                      VoiceEngine.say("Ok If You Will To Use My Full Power You Need The HuggingFace User Access Token , Feel Free To About Asking Help")
                      return
          if "user access token":
              VoiceEngine.say("After You Got The User Access Token Open My Folder Which Will Be Located At C Drive And A Open The File Named dot env and paste the access token to next huggingface api key , and your done ")
              return
          if "who created you" in command or "creator of you" in command:
              VoiceEngine.say("I Was Created By Vignesh As A Fun Project")
              return
          if "about you" in command:
              VoiceEngine.say("I am an AI-powered language model developed by OpenAI, known as Wingman. My purpose is to assist and provide information And Be Your personal assistant, created to provide dedicated support and assistance. It Took One Day To Build Me.")
       
      VoiceEngine.say("Is there anything else you want me to do?")


