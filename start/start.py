import random
import string 
import requests
import os
import time
import json
from colorama import Fore,init
import datetime
from configparser import ConfigParser
import sys
init(autoreset=True)
__version__ = "Author: Support"
__github__= "https://github.com/dk6m"
dir_path = os.path.dirname(os.path.realpath(__file__))
configur = ConfigParser()
configur.read(os.path.join(dir_path, f"config.ini"))
tokens_list = os.path.join(dir_path, f"tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
def s_sys_h():
       if configur.getboolean("sys","MULTI_TOKEN") == True:
          return {
        "Content-Type": "Application/json",
        "Orgin": "https://discord.com/",
        "Authorization":avail_tokens(tokens_list)[integ_0]
        }
       elif configur.getboolean("sys","MULTI_TOKEN") == False:
          return{
        "Content-Type": "Application/json",
        "Orgin": "https://discord.com/",
        "Authorization":configur.get("sys","TOKEN")
        }
       else:
          return {
        "Content-Type": "Application/json",
        "Orgin": "https://discord.com/",
        "Authorization":configur.get("sys","TOKEN")
        }
def sys_c_t():
       if configur.get("sys","TOKEN") != "":
          pass
       elif configur.get("sys","TOKEN") == "" and configur.getboolean("sys","MULTI_TOKEN") == False:
            print(f"{Lb}[!]{Fore.RED} No token found. You must paste your token inside the 'config.ini' file, in front of the value 'TOKEN'.")
            exit()
       elif configur.getboolean("sys","MULTI_TOKEN") == True and not avail_tokens(tokens_list)[0]:
           print(f"{Lb}[!]{Fore.RED} No tokens found. You must paste your tokens inside the 'tokens.txt' file.")
           exit()
       elif configur.getboolean("sys","MULTI_TOKEN") is not True and configur.getboolean("sys","MULTI_TOKEN") is not False and configur.get("sys","TOKEN") == "":
           print(f"{Lb}[!]{Fore.RED} Invalid config detected. Please re-check the config file, `config.ini` and your settings.")
           exit()
available_usernames = []
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTYELLOW_EX
Delay = configur.getfloat("config","default_delay")
def setconf():
       global string_0
       global digits_0
       global punctuation_0
       global webhook_0
       global sat_string
       global sat_digits
       global sat_multi_token
       global sat_punct
       global sat_webhook
       sat_webhook = configur.get("sys","WEBHOOK_URL")
       sat_string = configur.getboolean("config","string")
       sat_digits = configur.getboolean("config","digits")
       sat_punct = configur.getboolean("config","punctuation")
       sat_multi_token = configur.getboolean("sys","MULTI_TOKEN")
       if sat_webhook =="":
          webhook_0 = False
       elif sat_webhook !="":
          webhook_0 = True
       if sat_string == True:
          string_0 = string.ascii_lowercase
       elif sat_string == False:
          string_0 = ""
       else:
          string_0 = string.ascii_lowercase
          sat_string = True
       if sat_digits == True:
          digits_0 = string.digits
       elif sat_digits == False:
          digits_0 = ""
       else:
          digits_0 = string.digits
          sat_digits = True
       if sat_punct == True:
          punctuation_0 = sample_0
       elif sat_punct == False:
          punctuation_0 = ""
       else:
          punctuation_0 = sample_0
          sat_punct = True
       if sat_punct == False and sat_digits == False and sat_string == False:
          punctuation_0 = sample_0
          digits_0 = string.digits
          string_0 = string.ascii_lowercase
def main():
        sys_c_t()
        os.system(f"title {__version__} - Connected as {requests.get(sys_url,headers=s_sys_h()).json()['username']}")
        s_sys_h()
        setconf()    
        print(f"""{Fore.LIGHTYELLOW_EX}
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
      {__version__} 
      {__github__}                     {Fore.LIGHTCYAN_EX}Connected as {requests.get(sys_url,headers=s_sys_h()).json()['username']}{Ly}#{Fore.LIGHTCYAN_EX}{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}{Ly}

      Make a choice:                             
     {Fore.LIGHTCYAN_EX}1-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate names and check{Fore.LIGHTBLACK_EX}]{Ly}             
     {Fore.LIGHTCYAN_EX}2-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Check a specific list{Fore.LIGHTBLACK_EX}]{Ly}
     {Fore.LIGHTCYAN_EX}3-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate 4 letters with vowel replacement and check{Fore.LIGHTBLACK_EX}]{Ly}
     {Fore.LIGHTCYAN_EX}4-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate 5 letters with vowel replacement and check{Fore.LIGHTBLACK_EX}]{Ly}

      Discord Username checker.
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
    """)
        proc0()
def setdelay():
       global Delay
       print(f"{Lb}[!]{Ly} Default delay is: {Delay}s (config.ini){Lb}")
       d_input = input(f"{Lb}[{Ly}Edit Delay (Press Enter to skip){Lb}]:> ")
       if d_input=="" or d_input.isspace():
          return
       else:   
        try:
          int(d_input)
          Delay = int(d_input)
        except ValueError:
          print(f"{Lb}[!]{Fore.RED}Error: You must enter a valid integer. No strings.")
          setdelay()
def proc0():
        m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Support{Fore.LIGHTBLACK_EX}]:> {Fore.LIGHTYELLOW_EX}").lower()
        if m_input=="exit":
            sys.exit(0)
        if m_input=="":
            proc0()
        elif m_input=="2":
            setdelay()
            opt2load()
        elif m_input=="1":
           setdelay()
           opt1load()
        elif m_input=="3":
           setdelay()
           opt3load()
        elif m_input=="4":
           setdelay()
           opt4load()
        else:
            proc0()
def validate_names(opt,usernames):
       global available_usernames
       global integ_0
       if opt == 2:
        for username in usernames:
           body = {
               "username": username
           }
           time.sleep(Delay)
           endpoint = requests.post(URL, headers=s_sys_h(), json=body)
           json_endpoint = endpoint.json()
           if endpoint.status_code == 429 and sat_multi_token == True:
               tokens = avail_tokens(tokens_list)
               if integ_0 + 1 >= len(tokens):
                   print(f"{Lb}[!]{Fore.RED} All tokens rate limited. Waiting 120 seconds...")
                   time.sleep(120)
                   integ_0 = 0
               else:
                   integ_0 = (integ_0 + 1) % len(tokens)
               print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url,headers=s_sys_h()).json()['username']}#{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}")
           elif endpoint.status_code == 429 and sat_multi_token == False:
             sleep_time = endpoint.json()["retry_after"]
             print(f"{Lb}[!]{Fore.RED} Rate limit hit. Waiting {sleep_time} seconds (Discord rate limit)")
             time.sleep(sleep_time)
           if json_endpoint.get("taken") is not None:
               if json_endpoint["taken"] is False:
                print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{username}' available.")
                ch_send_webhook(username)
                save(username)
                available_usernames.append(username)
               elif json_endpoint["taken"] is True:
                  print(f"{Lb}[-]{Fore.RED} '{username}' taken.")
           else:
               print(f"{Lb}[?]{Fore.RED} Error validating '{username}': {endpoint.json()['message']} |Support: Make sure you have a valid token.")
       elif opt == 1 or opt == 3 or opt == 4:
           body = {
               "username": usernames
           }
           endpoint = requests.post(URL, headers=s_sys_h(), json=body)
           json_endpoint = endpoint.json()
           if endpoint.status_code == 429 and sat_multi_token == True:
               tokens = avail_tokens(tokens_list)
               if integ_0 + 1 >= len(tokens):
                   print(f"{Lb}[!]{Fore.RED} All tokens rate limited. Waiting 120 seconds...")
                   time.sleep(120)
                   integ_0 = 0
               else:
                   integ_0 = (integ_0 + 1) % len(tokens)
               print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url,headers=s_sys_h()).json()['username']}#{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}")
           elif endpoint.status_code == 429 and sat_multi_token == False:
             sleep_time = endpoint.json()["retry_after"]
             print(f"{Lb}[!]{Fore.RED} Rate limit hit. Waiting {sleep_time} seconds (Discord rate limit)")
             time.sleep(sleep_time)
           if json_endpoint.get("taken") is not None:
               if json_endpoint["taken"] is False:
                print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{usernames}' available.")
                ch_send_webhook(usernames)
                save(usernames)
                available_usernames.append(usernames)
               elif json_endpoint["taken"] is True:
                  print(f"{Lb}[-]{Fore.RED} '{usernames}' taken.")
           else:
               print(f"{Lb}[?]{Fore.RED} Error validating '{usernames}': {endpoint.json()['message']} |Support: Make sure you have a valid token.")
def avail_tokens(path):
       with open(path, 'r') as at:
            tokens = at.read().splitlines()
       return tokens
def exit():
       input(f"{Fore.YELLOW}Press Enter to exit.")
       sys.exit(0)
def checkavail(): 
       if len(available_usernames) < 1:
          print(f"{Lb}[!]{Fore.RED} Error: No available usernames found.")
          exit()
       else:
          return
def opt2load():
        global av_list
        global dir_path
        list_path = os.path.join(dir_path, f"usernames.txt")
        print(f"{Lb}[!]{Ly}Checking 'usernames.txt' for a valid list...")
        try:
         with open(list_path) as file:
          usernames = [line.strip() for line in file]
          validate_names(2,usernames)
         checkavail()
         print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
         exit()
        except FileNotFoundError:
           print(f"{Lb}[!]{Fore.RED} Error: Couldn't find the list (usernames.txt). Please make sure to create a valid list file in the same directory: \n({dir_path}\\)")
           exit()
def opt1load():
       opt1_input:int = input(f"{Lb}[{Ly}How many letters in a username{Lb}]:> ")
       try:
        int(opt1_input)
        if int(opt1_input) >32 or int(opt1_input) <2:
           print(f"{Lb}[!]{Fore.RED} Error: The username must contain at least 2 letters, and not more than 32 letters.")
           opt1load()
        opt2_input:int = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
        opt1func(int(opt2_input),int(opt1_input))
       except ValueError:
          print(f"{Lb}[!]{Fore.RED} Error: You must enter a valid integer. No strings.")
          opt1load()
def opt1func(v1,v2):
       for i in range(v1):
        name = get_names(int(v2))
        validate_names(1,name)
        time.sleep(Delay)
       checkavail()
       print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
       exit()
def get_names(length: int) ->str:
       return ''.join(random.sample(string_0 + digits_0 + punctuation_0, length))
def opt3load():
        path = os.path.join(dir_path, "4lwords.txt")
        try:
            with open(path, "r") as f:
                words = [line.strip().lower() for line in f if len(line.strip()) == 4 and any(c in 'aeiou' for c in line.lower())]
        except FileNotFoundError:
            print(f"{Lb}[!]{Fore.RED} Error: 4lwords.txt not found in the directory.")
            exit()
        count = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
        try:
            count = int(count)
            for _ in range(count):
                word = random.choice(words)
                vowels = [i for i, c in enumerate(word) if c in 'aeiou']
                if not vowels:
                    continue
                idx = random.choice(vowels)
                word = word[:idx] + random.choice(string.digits) + word[idx+1:]
                validate_names(3, word)
                time.sleep(Delay)
            checkavail()
            print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
            exit()
        except ValueError:
            print(f"{Lb}[!]{Fore.RED} Error: You must enter a valid integer.")
            opt3load()
def opt4load():
        path = os.path.join(dir_path, "5lwords.txt")
        try:
            with open(path, "r") as f:
                words = [line.strip().lower() for line in f if len(line.strip()) == 5 and any(c in 'aeiou' for c in line.lower())]
        except FileNotFoundError:
            print(f"{Lb}[!]{Fore.RED} Error: 5lwords.txt not found in the directory.")
            exit()
        count = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
        try:
            count = int(count)
            for _ in range(count):
                word = random.choice(words)
                vowels = [i for i, c in enumerate(word) if c in 'aeiou']
                if not vowels:
                    continue
                idx = random.choice(vowels)
                word = word[:idx] + random.choice(string.digits) + word[idx+1:]
                validate_names(4, word)
                time.sleep(Delay)
            checkavail()
            print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
            exit()
        except ValueError:
            print(f"{Lb}[!]{Fore.RED} Error: You must enter a valid integer.")
            opt4load()
def save(content:string):
       with open(av_list, "a") as file:
            file.write(f"\n{content}")
def ch_send_webhook(val0:str):
       if webhook_0 == True:
        webhook = Discord(url=sat_webhook)
        try:
         webhook.post(
           username="GetSniped",
           avatar_url="https://images-ext-1.discordapp.net/external/myIlmuBbhV4o7e5mFoqAFRhZ3Gv2yhdVjUnAYgapsMo/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1348389033801158738/b416ff71837dcaf94ea225e2769cbc16.png",
           embeds=[
        {
          "title": f"`{val0}` is available.",
          "timestamp": str(datetime.datetime.utcnow()),
          "footer": {
            "text": "GetSniped"
          },
          "author": {
            "name": "Username Sniped",
            "url": "https://github.com/dk6m",
            "icon_url": "https://images-ext-1.discordapp.net/external/myIlmuBbhV4o7e5mFoqAFRhZ3Gv2yhdVjUnAYgapsMo/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1348389033801158738/b416ff71837dcaf94ea225e2769cbc16.png"
          },
          "thumbnail": {
            "url": "https://images-ext-1.discordapp.net/external/myIlmuBbhV4o7e5mFoqAFRhZ3Gv2yhdVjUnAYgapsMo/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1348389033801158738/b416ff71837dcaf94ea225e2769cbc16.png"
          },
          "fields": [],
          "color": 16777215
        }
      ],
        )
        except Exception as s:
           print(f"{Lb}[!]{Fore.RED} Error: Something went wrong while sending the webhook request. Exception: {s} | Support: Make sure you have a valid webhook URL")
       else:
          return
class Discord:
        def __init__(self, *, url):
            self.url = url
        def post(
            self,
            *,
            content=None,
            username=None,
            avatar_url=None,
            tts=False,
            file=None,
            embeds=None,
            allowed_mentions=None
        ):
            if content is None and file is None and embeds is None:
                raise ValueError("required one of content, file, embeds")
            data = {}
            if content is not None:
                data["content"] = content
            if username is not None:
                data["username"] = username
            if avatar_url is not None:
                data["avatar_url"] = avatar_url
            data["tts"] = tts
            if embeds is not None:
                data["embeds"] = embeds
            if allowed_mentions is not None:
                data["allowed_mentions"] = allowed_mentions
            if file is not None:
                return requests.post(
                    self.url, {"payload_json": json.dumps(data)}, files=file
                )
            else:
                return requests.post(
                    self.url, json.dumps(data), headers={"Content-Type": "application/json"}
                )
if __name__ == "__main__":
        main()
