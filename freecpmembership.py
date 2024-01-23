from discum import Client
import time
import random
import os

# Cache Format: cID:uID:ET

# Mostly written for templating because I always forget how to use discum

def rng_colour():
    return f"\033[38;5;{random.randint(16, 255)}m"

banner = f"""
{rng_colour()}
     _ _                       _                  _          _   _     _     
  __| (_)___  ___ ___  _ __ __| |  ___ _   _  ___| | _____  | |_| |__ | |__  
 / _` | / __|/ __/ _ \| '__/ _` | / __| | | |/ __| |/ / __| | __| '_ \| '_ \\ 
| (_| | \__ \ (_| (_) | | | (_| | \\__ \\ |_| | (__|   <\\__ \\ | |_| |_) | | | |
 \__,_|_|___/\\___\\___/|_|  \\__,_| |___/\\__,_|\\___|_|\\_\\___/  \\__|_.__/|_| |_|
                                                                             
\033[0m
"""

print(banner)
preload = "sp4m.cache"
needsInit = True
if os.path.exists(preload):
    needsInit = False
    with open(preload, "r") as file:
        filename = file.read().strip()
    print(f"sp4m.cache -> {filename}")
    if not os.path.exists(filename):
        print(f"Broken Cache File, pointing to {filename}")
        time.sleep(2)
        needsInit = True
    else:
        choice = input(f"Enter Y to use {filename}, anything else for manual input:\n")
        if choice.upper() == "Y":
            with open(filename, "r") as file:
                cache = file.read().strip()
            cID, uID, ET = cache.split(':')
        else:
            needsInit = True

if needsInit:
    print(banner)
    cID = input("Channel ID:\n")
    uID = input("User ID:\n")
    ET = input("Extra Text:\n")
    saveChoice = input("Enter Y to save\n")
    if saveChoice.upper() == "Y":
        saveName = input("Save as: \n")
        with open(f"{saveName}.sp4m", "w") as file:
            file.write(f"{cID}:{uID}:{ET}")
            print("Saved! Be sure to add filename to sp4m.cache")
            time.sleep(1)

if os.path.exists("DT.txt"):
    with open("DT.txt", "r") as file:
        DT = file.read().strip()
else:
     print(banner)
     DT = input("Discord Token:\n")
     saveChoice = input("Enter Y to save to DT.txt\n")
     if saveChoice.upper() == "Y":
        with open("DT.txt", "w") as file:
            file.write(DT)

bot = Client(token=DT)

if ET != "":
    msgText = f"<@{uID}> {ET}"
else:
    msgText = f"<@{uID}>"

while True:
    message = bot.sendMessage(cID, msgText)
    mID = message.json()['id']
    time.sleep(0.5)
    bot.deleteMessage(cID, mID)
    # Customize delays here
    delay = random.randint(1,3)
    time.sleep(delay)
