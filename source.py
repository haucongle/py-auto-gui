import pyautogui
import random
import string
import time

def generate_random_username():
    name_length = random.randint(5, 15)
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    return random_name

def back_to_register(new_url):
    print("=====B1: mo trinh duyet")
    time.sleep(3)
    # pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('command', 'l')
    pyautogui.press('backspace')
    pyautogui.write(new_url, interval=0.05)
    pyautogui.press('enter')
    time.sleep(2)

def register(username, password):
    print("=====B2: dang ky")
    print("Nhap email")
    pyautogui.press('tab')
    pyautogui.write(username + '@gmail.com', interval=0.05)
    time.sleep(0.5)
    print("Nhap username")
    pyautogui.press('tab')
    pyautogui.write(username, interval=0.05)
    time.sleep(0.5)
    print("Nhap password")
    pyautogui.press('tab')
    pyautogui.write(password, interval=0.05)
    time.sleep(0.5)
    print("Nhap confirm password")
    pyautogui.press('tab')
    pyautogui.write(password, interval=0.05)
    time.sleep(0.5)
    # skip Referral code
    pyautogui.press('tab')
    print("Tic i have read")
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(0.5)
    print("Click register")
    for i in range(6):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(2)

def login(username, password):
    print("=====B3: dang nhap")
    print("click back to login")
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    print("Nhap username")
    pyautogui.press('tab')
    pyautogui.write(username, interval=0.05)
    time.sleep(0.5)
    print("Nhap password")
    pyautogui.press('tab')
    pyautogui.write(password, interval=0.05)
    time.sleep(0.5)
    print("Click access my account")
    for i in range(5):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(2)

def claim():
    print("=====B4: claim")
    print("close popup")
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(0.5)
    print("claim")
    pyautogui.click(738, 966)
    time.sleep(0.5)
    print("click extension")
    pyautogui.click(1316, 255)
    time.sleep(0.5)
    print("activate")
    pyautogui.click(1150, 601)


# MAIN FUNCTION
username = generate_random_username()
password = '1234d@EF'
# new_url = "https://app.nodepay.ai/register?ref=JJZqh2EuYeF3qjr"
# loop = 1
new_url = input("Nhap link: ") 
loop = int(input("Nhap so lan lap: "))
for i in range(loop):
    back_to_register(new_url)
    register(username, password)
    login(username, password)
    claim()
