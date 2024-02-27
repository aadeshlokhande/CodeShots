import pyautogui as pg 
from time import sleep

msg = ["Are you a student and you don't know how to code?","Join ICE Computers, Nagpur!","Learn C, C++, Python, Java and Web Development.","Enroll: wa.me/9673067036"]

sleep(3)
contactsFile = open("ss1.txt","r")

for index in range(20):
    contact = contactsFile.readline()
    pg.click(93,206,interval=2)
    pg.typewrite(contact,0.1)
    sleep(2)
    pg.press("enter")
    sleep(5)
    for i in msg:
        pg.typewrite(i,0.08)
        pg.hotkey("shift","enter")
    pg.press("enter")
    sleep(10)
    file = open("sentDone.txt","a")
    file.write(f"{contact} ")
    file.close()