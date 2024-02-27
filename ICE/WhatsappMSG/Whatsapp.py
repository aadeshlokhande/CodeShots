import pyautogui as pg 
from time import sleep 
import webbrowser
file = open("allCon.txt","r")

contacts = []
for i in range(12):
    data = file.readline().replace("\n","")
    contacts.append(data)

contacts = list(set(contacts))

contacts.sort()

# for i in contacts:
#     a = i.split(",")
#     print(a)

# exit()
for cont in contacts:
    contact = cont.split(",")
    name = contact[0]
    lname = contact[1]
    mobile = contact[2]
    webbrowser.open_new_tab(f"wa.me/91{mobile}")

    sleep(10)
    pg.click(890, 1058)
    sleep(1)


    pg.typewrite(f"Hello *{name.capitalize()} {lname.capitalize()}* ,",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite("Now that you've conquered *C programming*, it's time to take the next step with *C++* . Discover the power of *Object-Oriented Programming*, the convenience of the Standard Template Library, and enhanced features. *C++* opens doors to exciting *career opportunities* in *software development*.",0.05)
    pg.hotkey("shift","enter")
    pg.hotkey("shift","enter")
    pg.typewrite("_*Let's explore this journey together!*_",0.07)
    pg.hotkey("shift","enter")
    pg.hotkey("shift","enter")
    pg.typewrite("Best Regards",0.07)
    pg.hotkey("shift","enter")
    pg.typewrite("*ICE Computers*",0.07)


    pg.press("enter")
    

    # close tab
    pg.hotkey("alt","tab")
    sleep(1)
    pg.hotkey("ctrl","w")

    sleep(1)


file.close()