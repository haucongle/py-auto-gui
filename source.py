import pyautogui
import random
import string
import time

def gen_username():
    name_length = random.randint(10, 20)
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return random_name

def register(username, wait_time):
    time.sleep(wait_time)
    pyautogui.click(-1850,652)
    pyautogui.hotkey('command', 'l')
    pyautogui.press('backspace')
    pyautogui.write('https://app.nodepay.ai/register?ref=7sIsRp5LWWvWext')
    pyautogui.press('enter')
    time.sleep(wait_time)
    pyautogui.press('tab')
    pyautogui.write(username + '@gmail.com')
    pyautogui.press('tab')
    pyautogui.write(username)
    pyautogui.press('tab')
    pyautogui.write('1234d@EF')
    pyautogui.press('tab')
    pyautogui.write('1234d@EF')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(-1132, 1392)
    pyautogui.press(['tab','tab','tab','tab'])
    time.sleep(wait_time/2)
    pyautogui.press('enter')

def login(username, wait_time):
    time.sleep(wait_time)
    pyautogui.hotkey('command', 'l')
    pyautogui.press('backspace')
    pyautogui.write('https://app.nodepay.ai/login')
    pyautogui.press('enter')
    time.sleep(wait_time)
    pyautogui.press('tab')
    pyautogui.write(username)
    pyautogui.press('tab')
    pyautogui.write('1234d@EF')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(-1131, 1252)
    pyautogui.press(['tab','tab','tab','tab'])
    time.sleep(wait_time/2)
    pyautogui.press('enter')

def activate():
    time.sleep(wait_time)
    pyautogui.click(-147, 64)
    time.sleep(0.5)
    pyautogui.click(-307, 409)

loop = 2
for i in range(loop):
    begin = time.time()
    wait_time = 3+i/20
    username = gen_username()
    register(username, wait_time)
    login(username, wait_time)
    activate()
    print(i, username, time.time() - begin)