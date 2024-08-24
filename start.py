import os, sys
import time, datetime
import subprocess
import requests
import math

#SET THESE MANUALLY PLEASEEEEEE

flatpaks_dir = "/home/nord/rblxbots/"

aafk_click_xy = ["1888", "953"]

dice_click_zones = [["613","472"],["960","470"],["1309","747"],["622","706"],["960","709"],["1300","705"]]

#okay that's all you need to set :)



def clear():
    os.system("clear")

class colours:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

title = "\n ██▓███  ▓█████▄▄▄█████▓     ██████  ██▓ ███▄ ▄███▓    ▄▄▄▄    ▒█████  ▄▄▄█████▓\n▓██░  ██▒▓█   ▀▓  ██▒ ▓▒   ▒██    ▒ ▓██▒▓██▒▀█▀ ██▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒\n▓██░ ██▓▒▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▒██▒▓██    ▓██░   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░\n▒██▄█▓▒ ▒▒▓█  ▄░ ▓██▓ ░      ▒   ██▒░██░▒██    ▒██    ▒██░█▀  ▒██   ██░░ ▓██▓ ░       Made by\n▒██▒ ░  ░░▒████▒ ▒██▒ ░    ▒██████▒▒░██░▒██▒   ░██▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░     YoinkedYoink\n▒▓▒░ ░  ░░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ░  ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   \n░▒ ░      ░ ░  ░   ░       ░ ░▒  ░ ░ ▒ ░░  ░      ░   ▒░▒   ░   ░ ▒ ▒░     ░    \n░░          ░    ░         ░  ░  ░   ▒ ░░      ░       ░        ░ ░ ▒    ░      \n            ░  ░                 ░   ░         ░       ░          ░ ░           \n\n   |Clients|                              |Logs|          "
logstable = ["","","","","","","","",""]
runs = 0

def pretty_print(runs, startepoch, bottable, logstable):
    clear()
    template = title
    runningtime = math.ceil(time.time() - startepoch)
    runningtime = datetime.timedelta(seconds=runningtime)

    template = template + "[" + str(runs) + " runs, " + str(runningtime) +"]\n"

    for num in range(9):
        if bottable[num] != "Error":
            template = template + "\nBot " + str(num+1) + colours.HEADER + " [running]                     " + colours.END
        else:
            template = template + "\nBot " + str(num+1) + colours.FAIL + " [BORKED]                      " + colours.END
        template = template + logstable[num]
    
    print(template)

print("Pet Sim 99 Bot\nMade by YoinkedYoink\n\n\n")
input("Press enter to start bots: ")

clear()

if subprocess.check_output("wmctrl -l | grep -o -c -E '[[:space:]][1-9]{1}[[:space:]]' || true", shell=True, text=True).strip() == "0":
    print("Ready to start processes...\n")
else:
    print("Close all windows in desktops 2-10")
    exit()

botPIDS = []

for i in range(1,10):
    os.system("wmctrl -s "+str(i))

    env = os.environ.copy()
    env["HOME"] = flatpaks_dir+"/"+str(i)+"/"
    process = subprocess.Popen(["flatpak run org.vinegarhq.Sober > /dev/null"], env=env, shell=True)
    time.sleep(3)
    pid = process.pid

    process = None
    try:
        os.kill(int(pid), 0)
    except OSError:
        botPIDS.append("Error")
    else:
        if subprocess.check_output("ps "+str(pid)+" | grep -o -c -E '<defunct>' || true", shell=True, text=True).strip() == "0":
            botPIDS.append(pid)
        else:
            botPIDS.append("Error")

os.system("wmctrl -s 0")
for desknum in range(len(botPIDS)):
    if botPIDS[desknum] != "Error":
        print("Bot " + str(desknum+1) + colours.HEADER +" [ready]" + colours.END + " ("+str(botPIDS[desknum])+")")
    else:
        print("Bot " + str(desknum+1) + colours.FAIL + " [borked]" + colours.END)

input("\nPress enter when bots are in position... ")

clear()

print("\n(1) AntiAFK\n(2) Dice Farm\n")
mode = input("Choose a mode: ").strip()
discordnotify = input("Send discord notifs?(y/n): ").lower().strip()
desktopnotify = input("Send desktop notifs?(y/n): ").lower().strip()

if discordnotify in ('y','n'):
    if discordnotify == "y":
        discordwebhook = input("Discord webhook url: ").strip()
    pass
else:
    print("bad discord notify value")

if desktopnotify in ('y','n'):
    pass
else:
    print("bad desktop notify value")

clear()

if mode == "1":
    startepoch = time.time()
    while True:
        for desknum in range(len(botPIDS)):
            if botPIDS[desknum] != "Error":
                try:
                    os.kill(int(botPIDS[desknum]), 0)
                except OSError:
                    botPIDS[desknum] = "Error"
                    del logstable[0]
                    logstable.append("   !!BOT "+ str(desknum+1) +" DEAD!!     [" + datetime.datetime.now().strftime("%x %X") + "]")
                    if discordnotify == "y":
                        try:
                            req = requests.post(discordwebhook, json={"username" : "Pet Sim 99 Bot", "content" : "Bot " + str(desknum+1) + " Dead"})
                            req.raise_for_status()
                        except requests.exceptions.HTTPError:
                            del logstable[0]
                            logstable.append("!!ERR Discord Notif!! [" + datetime.datetime.now().strftime("%x %X") + "]")
                    if desktopnotify == "y":
                        os.system("notify-send -u critical -t 5000 \"Pet Sim 99 Bot\" \"A bot has died on desktop "+str(desknum+1)+"\"")
                        print("sent desktop notif")
                    continue
                else:
                    if subprocess.check_output("ps "+str(botPIDS[desknum])+" | grep -o -c -E '<defunct>' || true", shell=True, text=True).strip() != "0":
                        botPIDS[desknum] = "Error"
                        del logstable[0]
                        logstable.append("   !!BOT "+ str(desknum+1) +" DEAD!!     [" + datetime.datetime.now().strftime("%x %X") + "]")
                        if discordnotify == "y":
                            try:
                                req = requests.post(discordwebhook, json={"username" : "Pet Sim 99 Bot", "content" : "Bot " + str(desknum+1) + " Dead"})
                                req.raise_for_status()
                            except requests.exceptions.HTTPError:
                                del logstable[0]
                                logstable.append("!!ERR Discord Notif!! [" + datetime.datetime.now().strftime("%x %X") + "]")
                            #print("send discord")
                            #send discord bot notif
                        if desktopnotify == "y":
                            os.system("notify-send -u critical -t 5000 \"Pet Sim 99 Bot\" \"A bot has died on desktop "+str(desknum+1)+"\"")
                            print("sent desktop notif")
                        continue

                os.system("wmctrl -s "+str(desknum+1))

                time.sleep(1)

                os.system("xdotool mousemove " + aafk_click_xy[0] + " " + aafk_click_xy[1] + " click 1")
                time.sleep(0.2)
                os.system("xdotool mousemove " + aafk_click_xy[0] + " " + aafk_click_xy[1] + " click 1")
                time.sleep(0.2)

        os.system("wmctrl -s 0")
        runs += 1

        del logstable[0]
        logstable.append("Waiting 30 seconds... [" + datetime.datetime.now().strftime("%x %X") + "]")
        pretty_print(runs=runs, startepoch=startepoch, bottable=botPIDS, logstable=logstable)
        
        time.sleep(30)

elif mode == "2":
    startepoch = time.time()
    while True:
        for desknum in range(len(botPIDS)):
            if botPIDS[desknum] != "Error":
                try:
                    os.kill(int(botPIDS[desknum]), 0)
                except OSError:
                    botPIDS[desknum] = "Error"
                    del logstable[0]
                    logstable.append("   !!BOT "+ str(desknum+1) +" DEAD!!     [" + datetime.datetime.now().strftime("%x %X") + "]")
                    if discordnotify == "y":
                        try:
                            req = requests.post(discordwebhook, json={"username" : "Pet Sim 99 Bot", "content" : "Bot " + str(desknum+1) + " Dead"})
                            req.raise_for_status()
                        except requests.exceptions.HTTPError:
                            del logstable[0]
                            logstable.append("!!ERR Discord Notif!! [" + datetime.datetime.now().strftime("%x %X") + "]")
                    if desktopnotify == "y":
                        os.system("notify-send -u critical -t 5000 \"Pet Sim 99 Bot\" \"A bot has died on desktop "+str(desknum+1)+"\"")
                        print("sent desktop notif")
                    continue
                else:
                    if subprocess.check_output("ps "+str(botPIDS[desknum])+" | grep -o -c -E '<defunct>' || true", shell=True, text=True).strip() != "0":
                        botPIDS[desknum] = "Error"
                        del logstable[0]
                        logstable.append("   !!BOT "+ str(desknum+1) +" DEAD!!     [" + datetime.datetime.now().strftime("%x %X") + "]")
                        if discordnotify == "y":
                            try:
                                req = requests.post(discordwebhook, json={"username" : "Pet Sim 99 Bot", "content" : "Bot " + str(desknum+1) + " Dead"})
                                req.raise_for_status()
                            except requests.exceptions.HTTPError:
                                del logstable[0]
                                logstable.append("!!ERR Discord Notif!! [" + datetime.datetime.now().strftime("%x %X") + "]")
                        if desktopnotify == "y":
                            os.system("notify-send -u critical -t 5000 \"Pet Sim 99 Bot\" \"A bot has died on desktop "+str(desknum+1)+"\"")
                            print("sent desktop notif")
                        continue

                os.system("wmctrl -s "+str(desknum+1))

                time.sleep(1)

                for pos in dice_click_zones:
                    os.system("xdotool mousemove " + pos[0] + " " + pos[1] + " click 1")
                    time.sleep(0.5)
                    os.system("xdotool mousemove " + pos[0] + " " + pos[1] + " click 1")
                    time.sleep(0.5)

        os.system("wmctrl -s 0")
        runs += 1

        del logstable[0]
        logstable.append("Waiting 30 seconds... [" + datetime.datetime.now().strftime("%x %X") + "]")
        pretty_print(runs=runs, startepoch=startepoch, bottable=botPIDS, logstable=logstable)
        
        time.sleep(30)
else:
    print("Invalid mode selected")
    exit()

clear()


# for PID in botPIDS:
#     if PID != "Error":
#         try:
#             os.kill(int(PID), 9)
#         except OSError:
#             print("Bad PID " + str(PID))
#         else:
#             print("Killed " + str(PID))

print("Bye Bye!")
sys.exit(0)

