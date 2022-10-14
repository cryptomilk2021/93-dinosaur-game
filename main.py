import pyautogui
from PIL import Image

button7location = pyautogui.locateOnScreen('start_button.png')
location = button7location
pyautogui.click(x=location[0] + 20, y=location[1] + 20, clicks=1, button='left')

dino_location = pyautogui.locateOnScreen('dino.png')



while True:
    location = pyautogui.locateOnScreen('cact.png', region=(dino_location[0] + 95, dino_location[1] - 10, 40, 40))
    if location is not None:
        pyautogui.press('space')


