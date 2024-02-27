import pyautogui as pg 
from time import sleep 
import webbrowser
file = open("ICE Computers.csv","r")

contacts = []
for i in range(18):
    data = file.readline().replace("\n","").split(":-")
    contacts.append(data)

# print(contacts)


for contact in contacts:
    mobile = contact[3]
    name = contact[0]
    lname = contact[1]
    course = contact[5]
    fee =  contact[-1]
    webbrowser.open_new_tab(f"wa.me/91{mobile}")

    sleep(10)
    pg.click(890, 1058)
    sleep(1)

    pg.typewrite(f"Hello *{name}*,",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite(f"I hope this message finds you well.",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite(f"this is to inform you that you have a pending fee of *{fee}* for the course of *{course}*. we request you submit the fees as soon as possible.",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite(f"Thank You. 😊",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite(f"*ICE COMPUTERS*",0.07)
    pg.press("enter")
    sleep(1)


file.close()