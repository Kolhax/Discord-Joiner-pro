import requests
from discord_webhook import DiscordWebhook
import os
import webbrowser
import sys
from time import sleep

os.system('color a')
os.system('title Mass Joiner Bot - KeparDEV ')
os.system('cls && mode 800')
words = ("""
        /$$$$$           /$$
       |__  $$          |__/
          | $$  /$$$$$$  /$$ /$$$$$$$   /$$$$$$   /$$$$$$
          | $$ /$$__  $$| $$| $$__  $$ /$$__  $$ /$$__  $$
     /$$  | $$| $$  \ $$| $$| $$  \ $$| $$$$$$$$| $$  \__/
    | $$  | $$| $$  | $$| $$| $$  | $$| $$_____/| $$
    |  $$$$$$/|  $$$$$$/| $$| $$  | $$|  $$$$$$$| $$
     \______/  \______/ |__/|__/  |__/ \_______/|__/



     /$$$$$$$
    | $$__  $$
    | $$  \ $$ /$$$$$$   /$$$$$$
    | $$$$$$$//$$__  $$ /$$__  $$
    | $$____/| $$  \__/| $$  \ $$
    | $$     | $$      | $$  | $$
    | $$     | $$      |  $$$$$$/
    |__/     |__/       \______/


               Made By Kepar#0001 :)
               I was bored

               Tokens Extracted From 'tokens.txt'

    """)

for char in words:
    sleep(0.00000001)
    sys.stdout.write(char)
    sys.stdout.flush()

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")

os.system('pause >nul')