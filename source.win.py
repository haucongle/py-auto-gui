import pyautogui
import random
import string
import time

def gen_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 20)))

def register(username, wait_time):
    time.sleep(wait_time)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.press('backspace')
    pyautogui.write('https://app.nodepay.ai/register?ref=7sIsRp5LWWvWext')
    pyautogui.press('enter')
    time.sleep(wait_time)
    pyautogui.press('tab')
    pyautogui.write(username + '@bmail.com')
    pyautogui.press('tab')
    pyautogui.write(username)
    pyautogui.press('tab')
    pyautogui.write('1234d@EF')
    pyautogui.press('tab')
    pyautogui.write('1234d@EF')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(3483,1942)
    pyautogui.press(['tab','tab','tab','tab'])
    time.sleep(wait_time/2)
    pyautogui.press('enter')

def login(username, wait_time):
    time.sleep(wait_time)
    pyautogui.hotkey('ctrl', 'l')
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
    pyautogui.click(3485,1667)
    pyautogui.press(['tab','tab','tab','tab'])
    time.sleep(wait_time/2)
    pyautogui.press('enter')

def activate():
    time.sleep(wait_time)
    pyautogui.click(4743,128)
    time.sleep(0.5)
    pyautogui.click(4441,821)

loop = 200
for i in range(loop):
    begin = time.time()
    wait_time = 3+i/200
    username = gen_username()
    register(username, wait_time)
    login(username, wait_time)
    activate()
    print(i, username, time.time() - begin)
# while True:
#     print(pyautogui.position())
# users = [
#     '3fas5knx0ftwpgn',
#     'qciyj2yf2d1w',
#     'wos7cam5f9',
# ]
# for username in users:
#     wait_time = 3
#     login(username, wait_time)
#     activate()
