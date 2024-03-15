import time
import pyautogui
import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab,Image,ImageTk
import tkinter as tk
import win32gui
import win32con

def hide_taskbar():
    # Lấy handle của taskbar
    hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    
    # Ẩn taskbar bằng cách thiết lập thuộc tính SW_HIDE
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

def show_tasbar():
    hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
# def hide_other_windows():
#     # Lặp qua tất cả các cửa sổ trên desktop và ẩn chúng
#     for window in gw.getAllWindows():
#         if window.isActive and window.isMinimized == False:
#             window.minimize()
#         else:
#             window.minimize()

def hide_other_windows():
    # Tạo một danh sách để lưu trữ trạng thái của các cửa sổ
    windows_state = []

    # Lặp qua tất cả các cửa sổ trên desktop và ẩn chúng
    for window in gw.getAllWindows():
        if window.isActive and not window.isMinimized:
            # Lưu trạng thái của cửa sổ trước khi thu nhỏ nó
            windows_state.append((window, False))
            window.minimize()
        else:
            # Lưu trạng thái của cửa sổ trước khi thu nhỏ nó
            windows_state.append((window, True))
            window.minimize()
    def restore_windows():
        # Phục hồi lại trạng thái của các cửa sổ
        for window, was_minimized in windows_state:
            if not was_minimized:
                window.restore()

        # Hiển thị thanh tác vụ
        hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        
    return restore_windows
            
click_coordinates = None        
def show_image_cv2(screenshot_np, pt, w, h,isclickAround=False):
   
    hide_taskbar()
    # hide_other_windows()
    restore_function = hide_other_windows()
    current_window = win32gui.GetForegroundWindow()
    _, _, width, height = win32gui.GetWindowRect(current_window)
    win32gui.ShowWindow(current_window, win32con.SW_MINIMIZE)
    
    root = tk.Tk()
    root.attributes('-fullscreen',True)
    root.overrideredirect(True)
        
    def hide_window(event):
        # hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
        # win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        # for window in gw.getAllWindows():
        #     if window.isMinimized:
        #         window.restore()
        restore_function()
        root.quit()
    def get_mouse_position(event):
        global click_coordinates
        if isclickAround:
            x = event.x
            y = event.y
            # Xoá đi các dấu vẽ trước đó trên canvas
            canvas.delete("mark")
            click_coordinates = (x, y)
            print("Clicked Position:", x, y)
            # Vẽ dấu mới
            canvas.create_line(x - 10, y, x + 10, y, fill="red", tags="mark")  # Dấu cộng ngang
            canvas.create_line(x, y - 10, x, y + 10, fill="red", tags="mark")  # Dấu cộng dọc
    root.quit
            
    # root.bind("<Button-1>", hide_window)  # Click chuột trái
    root.bind("<Key>", hide_window)  # Bấm bất kỳ phím nào trên bàn phím
    # Tìm kích thước cửa sổ tối đa của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán tỉ lệ để điều chỉnh kích thước hình ảnh
    img_height, img_width, _ = screenshot_np.shape
    ratio = min(screen_width / img_width, screen_height / img_height)
    new_width = int(img_width * ratio)
    new_height = int(img_height * ratio)

    # Resize hình ảnh theo tỉ lệ
    resized_img = cv2.resize(screenshot_np, (new_width, new_height))

   
    # Chuyển đổi hình ảnh sang định dạng phù hợp cho Tkinter
    img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img)
    
    # Hiển thị hình ảnh trong cửa sổ Tkinter
    canvas = tk.Canvas(root, width=new_width, height=new_height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    if isclickAround:
        canvas.bind("<Button-1>", get_mouse_position)  # Bắt sự kiện nhấp chuột trên hình ảnh
    
    root.mainloop()
    
    return click_coordinates
def check_image_on_screen(image_path,sleep_time,show=False,threshold=0.7):
    
    # Lấy cửa sổ hiện tại
    time.sleep(sleep_time)
    current_window = gw.getActiveWindow()
    # Chụp ảnh của cửa sổ hiện tại
    if show:
        screenshot = pyautogui.screenshot()
    else:
        screenshot = ImageGrab.grab(bbox=current_window.box)
        
    
    
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
        # Hiển thị ảnh chụp màn hình có đánh dấu vị trí của template
        # Image.fromarray(cv2.rectangle(screenshot_np, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)).show()
        time.sleep(2)
        if show:
            show_image_cv2(screenshot_np, pt, w, h)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # Tính toạ độ của khung chứa template
        # h, w = template.shape
        top_left = max_loc
        
        return True
    else:
        return False

def check_image_on_screen_by_around_image(image_path,sleep_time,show=True,threshold=0.7):
    
    # Lấy cửa sổ hiện tại
    time.sleep(sleep_time)
    current_window = gw.getActiveWindow()
    # Chụp ảnh của cửa sổ hiện tại
    if show:
        screenshot = pyautogui.screenshot()
    else:
        screenshot = ImageGrab.grab(bbox=current_window.box)
        
    
    
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
        # Hiển thị ảnh chụp màn hình có đánh dấu vị trí của template
        # Image.fromarray(cv2.rectangle(screenshot_np, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)).show()
        time.sleep(2)
      
        return show_image_cv2(screenshot_np, pt, w, h,True)
        
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # # Tính toạ độ của khung chứa template
        # # h, w = template.shape
        # top_left = max_loc
        
        # return True
    else:
        return False
    
def check_image(image_path,time_sleep):
    if check_image_on_screen(image_path,time_sleep,show=True):
        print("Hình ảnh tồn tại trên màn hình của cửa sổ hiện tại.")
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.")
        
# image_path = "./screen_shot/test2.png"  # Đường dẫn đến hình ảnh bạn muốn tìm kiếm
# check_image(image_path,4)


# show_tasbar()   
def wait_time(num):
    time.sleep(num)
    
def wait_for_screen_stable(interval=1, timeout=None):
    previous_screenshot = pyautogui.screenshot()
    start_time = time.time()

    while True:
        current_screenshot = pyautogui.screenshot()

        # So sánh ảnh hiện tại với ảnh trước đó
        if current_screenshot == previous_screenshot:
            return True

        # Nếu đã qua thời gian timeout
        if timeout is not None and time.time() - start_time >= timeout:
            return False

        # Cập nhật ảnh trước đó và đợi một khoảng thời gian
        previous_screenshot = current_screenshot
        time.sleep(interval)

def wait_for_target_disappear(target_image, interval=1, timeout=None):
    start_time = time.time()
    
    while True:
        # Kiểm tra xem hình ảnh mục tiêu có hiển thị trên màn hình không
        if  check_image_on_screen(target_image,sleep_time=1,show=False) and timeout is not None and time.time() - start_time< timeout :
            print("Hình ảnh mục tiêu vẫn còn hiển thị trên màn hình.")
           
        elif check_image_on_screen(target_image,sleep_time=1,show=False) and timeout is not None and time.time() - start_time>= timeout :
            print("TimeOut:Hình ảnh mục tiêu vẫn còn hiển thị trên màn hình.")
            return False
        else:
            print("Hình ảnh mục tiêu ko còn hiển thị trên màn hình.")
            return False
        
        time.sleep(interval)

def wait_for_target_appear(target_image, interval=1, timeout=None):
    start_time = time.time()
    
    while True:
        # Kiểm tra xem hình ảnh mục tiêu có hiển thị trên màn hình không
        if  check_image_on_screen(target_image,sleep_time=interval,show=False) and timeout is not None and time.time() - start_time< timeout :
            print("Hình ảnh mục tiêu da hiển thị trên màn hình.")
            return False
        elif not check_image_on_screen(target_image,sleep_time=interval,show=False) and timeout is not None and time.time() - start_time>= timeout :
            print("TimeOut:Hình ảnh mục tiêu van chua hiển thị trên màn hình.")
            return False
        elif check_image_on_screen(target_image,sleep_time=interval,show=False) and timeout is not None and time.time() - start_time>= timeout :
            print("Hình ảnh mục tiêu da hiển thị trên màn hình.")
            return False
        
        else:
            print("Hình ảnh mục tiêu van chua hiển thị trên màn hình.")

        
        time.sleep(interval)       
# Đường dẫn đến hình ảnh mục tiêu
# target_image_path = "./screen_shot/test3.png"


# wait_for_target_appear(target_image_path,timeout=30)

    

