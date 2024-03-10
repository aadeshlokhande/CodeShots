import pyperclip
from time import sleep
import pyautogui as pg

number = ["7058548510","8600073906","7028373062","7709553810","9022746514","8767993086","8080237326","7709065192","7498765517","8657304112","7709869270","9356858076","9322375481","9172512104","9823868354","9022734703"]

for num in number:
    pg.click(1507,468,interval=1)
    pg.typewrite(num,0.08)
    sleep(1)
    pg.press("enter")
    sleep(3)
    pg.rightClick(1760,971,interval=1)
    pg.click(1690,811)
    try:
        a = pyperclip.paste()
        a = a.split("Name: ")[1].split("Carrier: ")[0].replace("\n","")
        nikName = a.split("Name: ")[-1]
        file = open("premrajcallingContacts.txt","a")
        strd = f"{num},{a.replace("\n","")},{nikName}"
        file.write(strd)
        print(strd)
        file.close()
    except:
        print("error")