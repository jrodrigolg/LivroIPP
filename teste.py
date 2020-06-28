from pyautogui import *
from pyperclip import *

a = ["Minhoca, minhoca",
     "Me dá uma beijoca",
     "Não dou, não dou",
     "Então eu vou roubar",
     "Minhoco, minhoco",
     "Você é mesmo louco",
     "Beijou do lado errado",
     "A boca é do outro lado",
     ]

while True:
    if True:
        click(1100, 705)
        for i in a:
            copy(i)
            hotkey("ctrl", "v")
            time.sleep(.7)
            hotkey("enter")
            time.sleep(.7)
        break
