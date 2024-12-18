import pyautogui
import random
import string
import time

def generate_random_username():
    name_length = random.randint(10, 20)
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return random_name

def back_to_register(new_url):
    pyautogui.click(-1850, 652)
    pyautogui.hotkey('command', 'l')
    pyautogui.press('backspace')
    pyautogui.write(new_url)
    pyautogui.press('enter')

def register(username, password):
    pyautogui.press('tab')
    pyautogui.write(username + '@gmail.com')
    pyautogui.press('tab')
    pyautogui.write(username)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(-1132, 1392)
    for i in range(4):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')

def login(username, password):
    pyautogui.press('tab')
    pyautogui.write(username)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.click(-1131, 1252)
    for i in range(4):
        pyautogui.press('tab')
    pyautogui.press('enter')

def claim():
    # pyautogui.click(-147, 64)
    pyautogui.click(-223, 64) # incognito
    time.sleep(0.5)
    # pyautogui.click(-307, 409)
    pyautogui.click(-378, 409) # incognito

password = '1234d@EF'
new_url = "https://app.nodepay.ai/register?ref=7sIsRp5LWWvWext"
loop = 100
for i in range(loop):
    wait_time = 4+i/10
    username = generate_random_username()
    time.sleep(2)
    back_to_register(new_url)
    time.sleep(wait_time)
    register(username, password)
    time.sleep(wait_time)
    login(username, password)
    time.sleep(wait_time)
    claim()
