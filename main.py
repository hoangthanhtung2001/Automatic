from window_app import start_app
from screen import screen_shot
from wait import wait_time,wait_for_screen_stable,wait_for_target_appear,check_image_on_screen
from keyboard_setting import write_data,keyboard_press_single,mutiply_keyboard_with_custom_press
from mouse_setting import mouse_click_by_around_Image
import win32gui
import win32con


url = "https://www.google.co.jp/"
find_key="RPA"
current_window = win32gui.GetForegroundWindow()
_, _, width, height = win32gui.GetWindowRect(current_window)
# Thu nhỏ cửa sổ
win32gui.ShowWindow(current_window, win32con.SW_MINIMIZE)
start_app("C:\Program Files\Google\Chrome\Application\chrome.exe")
wait_for_target_appear("./screen_shot/image.png",4,30)
mouse_click_by_around_Image(492,19)
wait_time(1)
mouse_click_by_around_Image(492,19)
wait_time(1)
mouse_click_by_around_Image(492,19)
wait_time(1)
mouse_click_by_around_Image(291,19)
wait_time(1)
mouse_click_by_around_Image(255,19)
wait_time(1)
mouse_click_by_around_Image(783,436)
wait_time(1)
write_data(find_key)
wait_time(1)
keyboard_press_single('enter')
# win32gui.SetForegroundWindow(current_window)
# win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_SHOWNORMAL)







