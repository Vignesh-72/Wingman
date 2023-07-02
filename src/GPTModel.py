import requests
import pywhatkit.misc as kit
import re
import VoiceEngine
import SpeechRecogniter
from bs4 import BeautifulSoup
from dotenv import dotenv_values

env_vars = dotenv_values('E:\\dev\\Assistant\\.env')
huggingfacehub_api_token = env_vars['HUGGINGFACEHUB_API_TOKEN']

#https://api-inference.huggingface.co/models/facebook/blenderbot-3B

GPT2 = "https://api-inference.huggingface.co/models/facebook/blenderbot-1B-distill"
headers = {
    "Authorization": f"Bearer {huggingfacehub_api_token}"
}
USER_AGENT = "User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"


def google(strcommand):
        VoiceEngine.say("Searching In Google")
        strcommand = re.sub(r"search|google","",strcommand)
        VoiceEngine.say("Searching "+strcommand+" On Google")
        kit.search(strcommand)

def querysearch(strcommand):
        try:
            URL = "https://www.google.co.in/search?q="+strcommand
            page = requests.get(URL,headers=headers)
            soup = BeautifulSoup(page.content,"html.parser")
            result = soup.find(class_='Z0LcW t2b5Cf')
            if result is not None:
               result = result.get_text()
               VoiceEngine.say(result)
            result = soup.find(class_="vk_gy vk_sh card-section sL6Rbf")
            if result is not None: 
              result = result.get_text()
              VoiceEngine.say(result)
        except:
              google(strcommand)         
           
def wiki(strcommand):
       VoiceEngine.say("Searching In WikiPeadia")
       try:
        strcommand = re.sub(r"use wikipedia","",strcommand)
        strcommand = re.sub(r"wikipedia","",strcommand)

        results = wiki.search(strcommand)
        for result in results:
           VoiceEngine.say(wiki.page(result).summary)
       except:
         VoiceEngine.say("Sorry I Can't Find It On WikiPeadia But Google Might Contain Some Info About It")
         VoiceEngine.say("would you like to do a google search")
         command = str(SpeechRecogniter.getinput()).lower()
         if "ok " in command or "sure" in command or "do" in command : google(strcommand)
         else : return

def gpt2(payload):
        
        print("gpt2")
        is_Key_set = is_APIKey_Set()
        if (is_Key_set == False):
             VoiceEngine.say("I Require A HuggingFace User Access Tokens To Use My Full Power Do Like To Know More About It")
             command = str(SpeechRecogniter.getinput()).lower()
             if "ok " in command or "sure" in command : notsetEnvDetails()
             else : return     

        response1 = requests.post(GPT2, headers=headers, json=payload)
        json_response = response1.json()
        generated_text = json_response['generated_text']
        VoiceEngine.say(generated_text)


def is_APIKey_Set(): 
     if huggingfacehub_api_token is None:
          return False

def notsetEnvDetails():
     huggingface="https://huggingface.co/docs/hub/security-tokens"
     VoiceEngine.say("I Require A HuggingFace User Access Tokens To Use MY GPT Model")
     VoiceEngine.say("You Can Create A User Access Tokens From The HuggingFace WebSite For Free")
     VoiceEngine.say("Do You Like To Open The Tutorial Page About How To Get HuggingFace User Access Tokens")
     command = str(SpeechRecogniter.getinput()).lower()
     if "ok " in command or "sure" in command or "do" in command or "open" in command: google(huggingface)
     else : return   
     
     


          
