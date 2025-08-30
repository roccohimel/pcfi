import os
#funtion vars
c = os.system("clear")
p = print
o = os.system
def ps():
    p()
def ra():
    p("Requesting authentication...")
#path vars
proRoot = ("~/pcfi/cfw/")
pro620 = (f"{proRoot}PRO_620/*")
pro639 = (f"{proRoot}PRO_639/*")
pro660 = (f"{proRoot}PRO_660/*")
pro661 = (f"{proRoot}PRO_661/*")
#sep
p("Choose firmware version: (on your PSP, go to: Settings --> System Settings --> System Information --> System Software)")
p("[1] 6.20")
p("[2] 6.39")
p("[3] 6.60")
p("[4] 6.61")
ps
fwv = input("> ")
c
p("Plug in PSP, then specify Memory Card path. (/example/example/disk/PSP) DO NOT PUT A SLASH AT THE END OF THE PATH NAME")
ps()
path = input("> ")
pgame = (f"{path}/PSP/GAME")
p("Attempting to install...")
o(f"find {path}")
if fwv == "1":
    ra()
    o(f"cp -r {pro620} {pgame}")
if fwv == "2":
    ra()
    o(f"cp -r {pro639} {pgame}")
if fwv == "3":
    ra()
    o(f"cp -r {pro660} {pgame}")
if fwv == "4":
    ra()
    o(f"cp -r {pro661} {pgame}")
else:
    p("Invalid firmware number! (Try again!)")
ra()
o(f"rm -rf {path}/SEPLUGINS")
ra()
o(f"rm -rf {path}/seplugins")
o(f"cp -r ~/pcfi/SEPLUGINS {path}")
c
p("INSTRUCTIONS:")
p("Go to: Game --> Memory Stick(TM)")
ps()
p("Step 1: run PRO-C Updater.")
ps()
p("Step 2: run PRO-C CIPL Flasher (run PRO-C Permanent Patch if on 6.20)")
ps()
p("Step 3: run PRO-C Fast Recovery (Enables CFW. For 6.39 to 6.61 users, run this after every power-on.)")
ps()
p("Your PSP is now modded")
ps()
ps
p("Copy offical PSP ISO files to /PSP/ISO")
p("Copy homebrew apps and unoffical games to /PSP/GAME")
p("Copy CXMB themes to /PSP/THEME")
p("Copy CFW plugins to /PSP/SEPLUGINS")

