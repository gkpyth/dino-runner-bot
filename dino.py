import pyautogui
import mss
import numpy as np

# ==================== INITIAL BRIEF PAUSE ====================
pyautogui.time.sleep(3)
# ==================== INITIAL BRIEF PAUSE ====================

# ==================== SCREEN REGION CONSTANT ====================
constant = 30   # Padding constant around the cursor position
# ==================== SCREEN REGION CONSTANT ====================

# ==================== HELPER FUNCTIONS ====================
def get_bg(img):
    '''
    Determines the background color of the screen

    Returns "light" or "dark"
    '''
    if (img[:,:,:3].mean(axis=2) > 128).any(): # Obstacle detection based on brightness
        return "light"
    else:
        return "dark"
# ==================== HELPER FUNCTIONS ====================

# ==================== MAIN GAME LOOP ====================
with mss.MSS() as sct:
    while "Bot Running":
        x, y = pyautogui.position()

        screen_region = {"top": y - constant, "left": x - constant, "width": 2 * constant, "height": 2 * constant}

        img = np.array(sct.grab(screen_region))

        if get_bg(img) == "light":

            if (img[:,:,:3].mean(axis=2) < 128).any():
                pyautogui.hotkey("space")

        elif get_bg(img) == "dark":
            if (img[:,:,:3].mean(axis=2) > 128).any():
                pyautogui.hotkey("space")
# ==================== MAIN GAME LOOP ====================

