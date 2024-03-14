import pyautogui
import time
import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab
import test_screen


def screen_shot(time_sleep): 
    time.sleep(time_sleep)
    test_screen.run_application()
    # find_latest_png_in_directory("./screen_shot")

# screen_shot(1)

def get_location_object(image_path, threshold=0.7):
    # Lấy cửa sổ hiện tại
    current_window = gw.getActiveWindow()
    # Chụp ảnh của cửa sổ hiện tại
    screenshot = pyautogui.screenshot()
    # Chuyển đổi ảnh sang mảng NumPy và chuyển đổi sang ảnh xám
    screenshot_np = np.array(screenshot)
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    # Đọc hình ảnh mẫu
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Tìm kiếm template trong ảnh chụp màn hình
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    # Tìm vị trí của template trong ảnh chụp màn hình
    locations = np.where(result >= threshold)
    if len(locations[0]) > 0:
        # Đánh dấu vị trí của template trên ảnh chụp màn hình
        w, h = template.shape[::-1]
        for pt in zip(*locations[::-1]):
            cv2.rectangle(screenshot_np, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
       
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # # Tính toạ độ của khung chứa template
        # # h, w = template.shape
        top_left = max_loc
        # # bottom_right = (top_left[0] + w, top_left[1] + h)
        # print(top_left)
        # x,y = top_left
        # mouse_movement(x,y)
        return top_left
    else:
        return 0
    
    
    
    


