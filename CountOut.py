import pyautogui
import time


class Count:
    def __init__ (self):
        self.number=0
        pyautogui.FAILSAFE = False
        self.AskForNumber()

    def AskForNumber(self):
        self.number = int(input('What number do you want me to start with?'))
        time.sleep(5)
        self.CountLoop()

    def CountLoop(self):
        while True:
            try:
                x, y = pyautogui.position()
                if x is 0:
                    if y is 0:
                        force=input('~~Paused~~\nPlease press enter to continue...\nThe next printed number is {}'.format(self.number))
                        time.sleep(5)
                        continue
                pyautogui.typewrite('{}'.format(self.number))
                pyautogui.press('enter')  
                self.number +=1
                time.sleep(1)
            except KeyboardInterrupt:
                input('~~Paused~~\nPlease press enter to continue...\nThe next printed number is {}'.format(self.number))
                continue
            
Count()
