import pyautogui
import time
from pyautogui import ImageNotFoundException

pyautogui.FAILSAFE = True

#Time delay to ensure the script only runs after the teams tab is open.
time.sleep(60)

cancel_icon_image = r"C:\\Users\pc\Pictures\Screenshots\Screenshot 2025-07-30 110808.png"
teams_icon_image = r"C:\Users\pc\Pictures\Screenshots\Screenshot 2025-07-30 105348.png"

def find_button_and_click(image:str,):
    """ This function takes an image path as an argument,
    locates the position on the screen and clicks on it."""
    icon_location = pyautogui.locateCenterOnScreen(image,confidence = 0.9,grayscale=True)
    pyautogui.moveTo(icon_location,duration = 3,tween=pyautogui.easeInQuad)
    pyautogui.click()
#These try-except blocks handle exceptions that come up when the image is not found and instead display an alert
try :
    # confirms that the teams icon is present on screen
    teams_icon_location = pyautogui.locateCenterOnScreen(teams_icon_image,confidence = 0.9)
    try:
        # This try-block checks if the cancel icon is present and if not it clicks on the teams icon to display it on the screen and then cancel it
        find_button_and_click(cancel_icon_image)
    except ImageNotFoundException:
        pyautogui.moveTo(teams_icon_location, duration=3, tween=pyautogui.easeInQuad)
        pyautogui.click()
        find_button_and_click(cancel_icon_image)

except ImageNotFoundException:
    pyautogui.alert(text='Your wishes couldn\'t be fulfilled my liege because the Teams app isn\'t open', title='Status Report', button='OK')

