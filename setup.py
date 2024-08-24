import os
print("first time run script")
input("press enter to continue... ")

basedir = input("flatpak install dir: ").strip()

if os.path.isdir(basedir):
    print("dir exists")
elif os.path.isdir(basedir) == False:
    print("creating dir " + basedir)
    os.system("mkdir "+basedir)

if len(os.listdir(basedir)) == 0:
    print("Dir is empty, continuing...")
else:
    print("Dir is not empty!!!\nExiting!!!")
    exit()

print("Creating bot subfolders...")
os.system("mkdir "+basedir+"/{1..9}")

print(str(len(os.listdir(basedir))) + " folders created!")

print("Downloading sober flatpak")
os.system("env HOME="+basedir+"/1 flatpak install -y --noninteractive --user https://sober.vinegarhq.org/sober.flatpakref > /dev/null")

if os.path.isdir(basedir + "/1/.local/"):
    print("download completed")
else:
    print("error during download\nExiting")
    exit()

print("Install roblox apk now...")
os.system("env HOME="+basedir+"/1 flatpak run org.vinegarhq.Sober > /dev/null")
input("Press enter when install is complete: ")


print("Copying optimal fflags...")

os.system("cat ./ClientSettings > "+basedir+"/1/.var/app/org.vinegarhq.Sober/data/sober/exe/ClientSettings/ClientAppSettings.json")
print("Set fflags")

print("Copying all files to other subdirs...")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/2")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/3")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/4")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/5")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/6")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/7")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/8")
os.system("cp -r "+basedir+"/1/./ "+basedir+"/9")
print("Copied all")

print("Setup except for logins should be complete!")