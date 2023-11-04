import pyautogui as spam
import time
limit=input("enter the number of messages you want to send")
msg=input("message you want to send")
i=0
time.sleep(5)
while i < int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
    i+=1
    