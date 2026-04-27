import pyautogui

pyautogui.time.sleep(3)

while "Dino Bot Running":
    x, y = pyautogui.position()
    rgb = pyautogui.pixel(x, y)

    brightness = ( rgb[0] +rgb[1] + rgb[2])/3

    if brightness < 128: # Obstacle detection
        pyautogui.press("space")
        print("Jump")
    else:
        print("Run")

