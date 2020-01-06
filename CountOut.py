import pyautogui
import time


class Count:
    def __init__ (self):
        self.number=0
        pyautogui.FAILSAFE = False
        self.AskForNumber()

    def AskForNumber(self):
        self.number = int(input('What number do you want me to start with?\n'))
        time.sleep(5)
        self.CountLoop()

    def CountLoop(self):
        while True:
            try:
                self.CheckFailSafe()
                pyautogui.typewrite('{}'.format(self.number))
                pyautogui.press('enter')  
                self.number +=1
                time.sleep(4)
            except KeyboardInterrupt:
                input('~~Paused~~\nPlease press enter to continue...\nThe next printed number is {}'.format(self.number))
                continue

    def CheckFailSafe(self):
            x, y = pyautogui.position()
            if x is 0:
                if y is 0:
                    print('~~Paused~~\nWould you like to continue?\nThe next printed number is {}'.format(self.number))
                    Ask=input('1 to continue  ~  2 to quit\n')
                    if Ask is '1':
                        time.sleep(5)
                        self.CountLoop()
                    elif Ask is '2':
                        print('Would you like to change the number or exit the program?')
                        Change=input('1 to change number.  ~  2 to exit.\n')
                        if Change is '1':
                            self.AskForNumber()
                        elif Change is '2':
                            quit()
                        else:
                            quit()
                    else:
                        quit()
Count()
