import pyautogui
import random
import string
import time

def generate_random_username():
    name_length = random.randint(10, 20)
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return random_name

def back_to_register(new_url):
    # print("=====B1: mo trinh duyet")
    time.sleep(2)
    pyautogui.click(-1850, 652)
    pyautogui.hotkey('command', 'l')
    pyautogui.press('backspace')
    pyautogui.write(new_url)
    pyautogui.press('enter')
    time.sleep(2)

def register(username, password):
    # print("=====B2: dang ky")
    # print("Nhap email")
    pyautogui.press('tab')
    pyautogui.write(username + '@gmail.com')
    # print("Nhap username")
    pyautogui.press('tab')
    pyautogui.write(username)
    # print("Nhap password")
    pyautogui.press('tab')
    pyautogui.write(password)
    # print("Nhap confirm password")
    pyautogui.press('tab')
    pyautogui.write(password)
    # skip Referral code
    pyautogui.press('tab')
    # print("Tic i have read")
    pyautogui.press('tab')
    pyautogui.press('space')
    # cloudflare
    pyautogui.click(-1132, 1392)
    # print("Click register")
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)

def login(username, password):
    # print("=====B3: dang nhap")
    # print("click back to login")
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    # print("Nhap username")
    pyautogui.press('tab')
    pyautogui.write(username)
    # print("Nhap password")
    pyautogui.press('tab')
    pyautogui.write(password)
    # cloudflare
    pyautogui.click(-1131, 1252)
    # print("Click register")
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)

def claim():
    # print("=====B4: claim")
    # print("close popup")
    # pyautogui.press('tab')
    # pyautogui.press('space')
    # time.sleep(0.5)
    # print("click extension")
    # pyautogui.click(-147, 64)
    pyautogui.click(-223, 64) # incognito
    time.sleep(0.5)
    # print("activate")
    # pyautogui.click(-307, 409)
    pyautogui.click(-378, 409) # incognito

# MAIN FUNCTION
password = '1234d@EF'
new_url = "https://app.nodepay.ai/register?ref=7sIsRp5LWWvWext"
loop = 1
for i in range(loop):
    begin = time.time() 
    username = generate_random_username()
    back_to_register(new_url)
    register(username, password)
    login(username, password)
    claim()
    print(i+1, username, time.time() - begin)
# while True:
#     print(pyautogui.position())
