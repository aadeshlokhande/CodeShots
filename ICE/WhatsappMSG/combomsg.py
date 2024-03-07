import webbrowser 
# import pyperclip
from time import sleep
import pyautogui as pg


numbers = ["9322169657","7057530377","7756881805","9527538676","8390226485","8767558054","9356957418","7499965136","9356626160","9021895510","9284888671","8767060053","7498711373","8766801667","7620407357","9307489625","9588419280","9172080007","9146630915","7498934547","9423260377","7385680792","9156411322","9356063563","9423811893","9766376251","7249620996","9699722601","9403601193","9145777923","9860321398","9529850206","9309310894","9921964644","9175986112","7020198669","9359555184","9049644908","9022543316","9356318870","8149240125","7843038911","7499767412","8999207318","7821808947","9356957418","9922277553","9359052129","8380945579","6302833154","9356829315","8010847991","9552778437","9404088117","9021933936","7030001042","7058548510","8600073906","7028373062","7709553810","9022746514","8767993086","8080237326","7709065192","7498765517","8657304112","7709869270","9356858076","9322375481","9172512104","9823868354","9022734703"]

msg = """Exciting News from *ICE Computers*! Enroll in our programming courses *(C language, C Plus Plus, Python)* starting *15th March*! The fee is ₹3,500 per course, but we have a special offer : Enroll in all courses for just *₹4,999*! The classes will be held from 6 to 7 PM and will last for 3 months. No prerequisites are required, and seats are limited! To enroll, WhatsApp us at *7058232826* or visit us at *Opposite AXIS ATM, Vaibhav Nagar, Wanadongri, Nagpur*. Don't miss this opportunity to learn programming from industry experts at *ICE Computers*!"""
msg = msg.replace(" ","%20")

sleep(2)
for number in numbers:
    link = f"https://wa.me/91{number}/?text={msg}"
    # pyperclip.copy(link)
    webbrowser.open(link)
    sleep(3)
    webbrowser.open(link)
    sleep(3)
    pg.press("enter",interval=1)
    pg.hotkey("alt","tab")
    sleep(1)
    pg.hotkey("ctrl","w",interval=0.5)
    pg.hotkey("ctrl","w")
    sleep(1)