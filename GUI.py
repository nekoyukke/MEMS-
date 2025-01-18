import pyautogui
import random
import time
import subprocess
import webbrowser
from PIL import Image, ImageOps
import ctypes
from tkinter import messagebox
import threading
import winsound

#エラーで死なないようにするため
pyautogui.FAILSAFE=False
#max*0.001s間実行される
max = 2000
#現在のステップ数
step = 0
#mouseの動く感度
mouse_move_size = 1

#windows標準のアプリの絶対パス
#追加おｋ
links =[r'C:\Windows\notepad.exe',r'C:\Windows\explorer.exe'
        ]
#windows標準音再生
sound2 = ['SystemHand','SystemAsterisk']

def invert_screen():
    # 画面全体のキャプチャを取る
    screenshot = pyautogui.screenshot()

    # 画像を反転させる
    inverted_image = ImageOps.invert(screenshot.convert("RGB"))

    # 反転した画像を画面に表示
    inverted_image.show()

def error():
    messagebox.showerror("virus", "MEMS++ has this computer")

def sound():
    winsound.PlaySound( sound2[random.randint(0,1)], winsound.SND_ALIAS )


#拡大鏡を設置
pyautogui.hotkey('win', ';')
time.sleep(0.5)
#全部を最小にする
pyautogui.hotkey('win', 'd')


while (step<max):
    mouse_position = pyautogui.position()
    try:
        if (step*mouse_move_size < 50):
            pyautogui.moveTo(mouse_position.x+random.randint(-mouse_move_size*step,mouse_move_size*step),mouse_position.y+random.randint(-mouse_move_size*step,mouse_move_size*step))
        else:
            pyautogui.moveTo(mouse_position.x+random.randint(-50,50),mouse_position.y+random.randint(-50,50))
    except:
        pyautogui.moveTo(200,200)

    if (random.randint(0,9)==0):
        invert_screen()
    if (random.randint(0,9)==0):
        threading.Thread(target=error).start()
    
    #cmd起動
    if (random.randint(0,9)==0):
        pyautogui.hotkey('win')
        pyautogui.press('c')
        pyautogui.press('m')
        pyautogui.press('d')
        pyautogui.press('enter')

    #クリック
    if (random.randint(0,9)==0):
        pyautogui.click()

    #ウイルスの削除方法をggる
    if (random.randint(0,9)==0):
        webbrowser.open("https://www.google.com/search?q=how+to+remove+a+virus")

    #メモ帳
    if (random.randint(0,9)==0):
        try:
            subprocess.Popen(links[random.randint(0,len(links)-1)])
        except:
            print("error")
    
    if (random.randint(0,2) == 1):
        pyautogui.hotkey('ctrl', 'alt', 'i')
    if (random.randint(0,10) == 1):
        threading.Thread(target=sound).start()
    time.sleep(0.001)
    step+=1

print("stop")