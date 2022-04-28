import os
import subprocess
import time
import keyboard
import pyautogui
import sys


def resource_path(relative):
    """ Image Search.
    Skip it, the function is not required by the program,
    but suddenly it will come in handy later. :)
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


img_path = resource_path('11.png')


def start_battle_net():
    """  Launching the program  """
    try:
        program = "Battle.net.exe"
        subprocess.Popen(r"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe")  # firs check run
        os.system('start /d"C:\\Program Files (x86)\\Battle.net\\" ' + program)  # second check run
        time.sleep(20)  # Waiting to start
    finally:  # Removing errors and exceptions
        return


def click_setting():
    """  We are looking for an image on the screen and click  """
    number = 0  # Exception counter.
    try:
        buttonlocation = pyautogui.locateOnScreen('11.png')  # find image to Window
        buttonlocation[0]
        buttonlocation.left
        buttonpoint = pyautogui.center(buttonlocation)
        buttonpoint[0]
        buttonpoint.x
        buttonx, buttony = buttonpoint
        pyautogui.click(buttonx, buttony)   # one click
        pyautogui.click(buttonx, buttony)   # two click

    except:
        number += 1  # Didn't find it? Add 1

        buttonlocation = pyautogui.locateOnScreen('12.png')  # find image to Window
        buttonlocation[0]
        buttonlocation.left
        buttonpoint = pyautogui.center(buttonlocation)
        buttonpoint[0]
        buttonpoint.x
        buttonx, buttony = buttonpoint
        pyautogui.click(buttonx, buttony)
        pyautogui.click(buttonx, buttony)

    finally:
        number += 1
        if number == 2:
            sys.exit()  # We finish if we haven't found it battle.net
        else:
            return


def key_login():
    pyautogui.sleep(1)
    keyboard.send("Tab")
    pyautogui.sleep(1)
    keyboard.send("down")
    pyautogui.sleep(1)
    keyboard.write("poasdf", 1)  # login, incorrect :)
    keyboard.send("shift+2")  # @
    keyboard.write("suggerin", 1)
    keyboard.write(".com", 1)
    # pyautogui.typewrite('Hello world!', interval=0.25)    #  Alternative input module
    pyautogui.sleep(1)


def key_pass():
    keyboard.send("Tab")
    pyautogui.sleep(1)
    keyboard.write("b00et1")
    keyboard.send("shift+y")  # Large letters
    keyboard.write("9", 1)
    keyboard.send("shift+x")
    keyboard.write("8", 1)
    # pyautogui.typewrite('Hello world!', interval=0.25)    #  Alternative input module
    pyautogui.sleep(1)


def click_tick():
    """  Click on the tick  """
    keyboard.send("Tab")
    pyautogui.sleep(1)
    keyboard.send("Space")
    pyautogui.sleep(1)


def click_authorization():
    keyboard.send("Tab")
    pyautogui.sleep(1)
    keyboard.send("Enter")
    pyautogui.sleep(1)


start = (start_battle_net(),
         click_setting(),
         key_login(),
         key_pass(),
         click_tick(),
         click_authorization()
         )

for i in range(len(start)):
    if i:
        pyautogui.PAUSE = 2
        pyautogui.FAILSAFE = True

sys.exit()  # Program completion control
