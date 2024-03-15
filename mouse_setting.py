import pyautogui
import time
from screen import get_location_object
import os 
import glob
from wait import check_image_on_screen_by_around_image
# Di chuyển chuột đến tọa độ (x, y)
def find_latest_png_in_directory(directory):
    # Tạo đường dẫn đầy đủ đến thư mục
    full_directory_path = os.path.abspath(directory)

    # Tìm tất cả các file PNG trong thư mục
    png_files = glob.glob(os.path.join(full_directory_path, '*.png'))

    if not png_files:
        return None  # Không có file PNG nào trong thư mục

    # Sắp xếp danh sách các file PNG theo thứ tự thời gian sửa đổi (mới nhất đến cũ nhất)
    png_files.sort(key=os.path.getmtime, reverse=True)

    # Trả về đường dẫn của file PNG mới nhất
    return png_files[0]

def mouse_movement_around_Image(x,y):
    pyautogui.moveTo(x, y)

def mouse_click_by_around_Image(x,y):
    pyautogui.click(x=x,y=y)

def right_click_around_Image(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button="right")

def double_click_around_Image(x,y):
    pyautogui.doubleClick(x,y)

def three_click_around_Image(x,y):
    pyautogui.tripleClick(x,y)

def click_and_drag_around_Image(x,y,x2,y2):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button="left",x=x,y=y)
    pyautogui.moveTo(x2, y2)
    pyautogui.mouseUp(button='left',x=x2,y=y2)

def mouse_scroll_up_around_Image(count,x,y):
    if count>0:
            pyautogui.moveTo(x, y)
            pyautogui.scroll(count,x=x,y=y)
    else:
            pyautogui.scroll(0)
            
def mouse_scroll_down_around_Image(count,x,y):
    if count<0:
            pyautogui.moveTo(x, y)
            pyautogui.scroll(count,x=x,y=y)
    else:
            pyautogui.scroll(0)
            

def mouse_movement(image_path):
    if get_location_object(image_path) != 0:
        x,y=get_location_object(image_path)
        pyautogui.moveTo(x, y)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.")


def mouse_click(image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        pyautogui.click(x=x,y=y)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.")

def right_click(image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click(button="right")
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.")
    
def double_click(image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        pyautogui.doubleClick(x,y)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.")
        
def three_click(image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        pyautogui.tripleClick(x,y)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.") 
    
def click_and_drag(image_path_1,image_path_2):
    if get_location_object(image_path_1) != 0 and get_location_object(image_path_2):
        x,y =get_location_object(image_path_1)
        x2,y2= get_location_object(image_path_2)
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button="left",x=x,y=y)
        pyautogui.moveTo(x2, y2)
        pyautogui.mouseUp(button='left',x=x2,y=y2)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.") 

def mouse_scroll_up(count,image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        if count>0:
            pyautogui.moveTo(x, y)
            pyautogui.scroll(count,x=x,y=y)
        else:
            pyautogui.scroll(0)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.") 
    

def mouse_scroll_down(count,image_path):
    if get_location_object(image_path) != 0:
        x,y =get_location_object(image_path)
        if count<0:
            pyautogui.moveTo(x, y)
            pyautogui.scroll(count,x=x,y=y)
        else:
            pyautogui.scroll(0)
    else:
        print("Hình ảnh không tồn tại trên màn hình của cửa sổ hiện tại.") 
    



