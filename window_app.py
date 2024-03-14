import subprocess
import os
import shutil
from keyboard_setting import mutiply_keyboard_with_custom_press
import time
import win32gui
import win32con

def start_app(path):
    subprocess.Popen(path,shell=True)
    
def open_folder(pathname):
    os.startfile(os.path.realpath(pathname))
    
def close_folder(pathname):
    os.startfile(os.path.realpath(pathname))
    time.sleep(2)
    mutiply_keyboard_with_custom_press('ctrl','w')

def move_a_file(source_file_path,destination_file_path):
    shutil.move(source_file_path,destination_file_path)

def move_a_directory(soucre_folder_path,destination_folder_path):
    shutil.move(soucre_folder_path,destination_folder_path)

def copy_a_file(source_file_path,destination_file_path):
    shutil.copy(source_file_path,destination_file_path)
    
def copy_a_folder(source_file_path,destination_file_path):
    # print(source_file_path.)
    index = source_file_path.rfind("\\")  # Tìm vị trí của kí tự "\"
    if index != -1:  # Đảm bảo rằng kí tự "\" được tìm thấy
        result = source_file_path[index+1:]  # Cắt chuỗi từ vị trí của kí tự "\" đến hết
        new_destination_file_path = destination_file_path +'\\'+result
        shutil.copytree(source_file_path,new_destination_file_path)
    else:
        print("Không tìm thấy kí tự '\\'")

def delete_file(file_path):
    os.remove(file_path)
    
def delete_folder(folder_path):
    shutil.rmtree(folder_path)


def check_file_existence(folder_path, allowed_extensions=None):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Thư mục không tồn tại!")
        return False
    
    files = os.listdir(folder_path)
    
    if allowed_extensions is not None:
        filtered_files = [file for file in files if os.path.isfile(os.path.join(folder_path, file)) and file.endswith(allowed_extensions)]
    else:
        filtered_files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
    
    if filtered_files:
        print("Có file trong thư mục.")
        # print("Danh sách các file:")
        # for file in filtered_files:
        #     print(os.path.join(folder_path, file))
        return True
    else:
        print("Không có file trong thư mục.")
        return False
def get_information_from_folder(type,folder_path,file_name=None,type_data=None):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Thư mục không tồn tại!")
        return False
    if type == 1:
        files = os.listdir(folder_path)
    
        if file_name is not None:
            filtered_files = [file for file in files if os.path.isfile(os.path.join(folder_path, file)) and file.endswith(file_name)]
        else:
            filtered_files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
    
        if filtered_files:
            print("Có file trong thư mục.")
            print("Danh sách các file:")
            if type_data is not None:
                for file in filtered_files:
                    print(file)
            else:
                for file in filtered_files:
                    print(os.path.join(folder_path, file))
            return True
        else:
            print("Không có file trong thư mục.")
            return False   
    if type == 2:
        subfolders = get_subfolders(folder_path)
        if subfolders:
            if file_name is not None:
                for subfolder in subfolders:
                    index = subfolder.rfind("\\")
                    if index != -1:  # Đảm bảo rằng kí tự "\" được tìm thấy
                        result = subfolder[index+1:]  # Cắt chuỗi từ vị trí của kí tự "\" đến hết
                        if result == file_name:
                            print(subfolder)
                            break
                    else:
                        print("Khong co ten folder chi dinh dinh")
            else:
                if type_data is not None :
                    for subfolder in subfolders:
                        index = subfolder.rfind("\\")
                        if index != -1:  # Đảm bảo rằng kí tự "\" được tìm thấy
                            result = subfolder[index+1:]  # Cắt chuỗi từ vị trí của kí tự "\" đến hết
                            print(result)
                else:
                    for subfolder in subfolders:
                        print(subfolder) 

def get_subfolders(folder_path):
    subfolders = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
            # subfolders.extend(get_subfolders(item_path))  # Gọi đệ quy để lấy thêm thư mục con của thư mục hiện tại
    return subfolders


def find_window(window_title):
    hwnds = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnds)

    for hwnd in hwnds:
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_title in window_text:
                return hwnd
    return None

def open_window(window_title, exact_match=False, starts_with=False):
    hwnd = None
    if exact_match:
        hwnd = win32gui.FindWindow(None, window_title)
    elif starts_with:
        hwnd = find_window_startswith(window_title)
    else:
        hwnd = find_window(window_title)

    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    else:
        print("Không tìm thấy cửa sổ có tiêu đề chứa '{}'".format(window_title))

def find_window_startswith(window_title):
    hwnds = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnds)

    for hwnd in hwnds:
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text.startswith(window_title):
                return hwnd
    return None


# chuoi_can_tim = "按分手順書.xlsx - Excel"

# print("Mở cửa sổ có tiêu đề bao gồm chuỗi chỉ định:")
# open_window(chuoi_can_tim)

# print("\nMở cửa sổ có tiêu đề chính xác bằng chuỗi chỉ định:")
# open_window(chuoi_can_tim, exact_match=True)

# print("\nMở cửa sổ có tiêu đề bắt đầu bằng chuỗi chỉ định:")
# open_window(chuoi_can_tim, starts_with=True)
# def bring_window_to_front(window_title):
#     # Duyệt qua tất cả các cửa sổ hiện có
#     hwnds = []
#     win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnds)

#     for hwnd in hwnds:
#         if win32gui.IsWindowVisible(hwnd):
#             # Lấy tiêu đề của cửa sổ
#             window_text = win32gui.GetWindowText(hwnd)
#             if window_title in window_text:
#                 # Đưa cửa sổ lên phía trước
#                 win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
#                 win32gui.SetForegroundWindow(hwnd)
#                 return

# # Chuỗi cần tìm trong tiêu đề của cửa sổ
# chuoi_can_tim = "メモ帳"

# # Gọi hàm để đưa cửa sổ chứa chuỗi cần tìm lên phía trước
# bring_window_to_front(chuoi_can_tim)

# get_information_from_folder(1,r"C:\Users\100125\Desktop\check")          
# folder_path = r"C:\Users\100125\Desktop\check"
# allowed_extensions = (".pdf")
# check_file_existence(folder_path,allowed_extensions)
# Đuôi file cần kiểm tra (có thể là danh sách)

# copy_a_folder(r"C:\Users\100125\Desktop\check1",r"C:\Users\100125\Desktop\check")

# move_a_directory(r"C:\Users\100125\Desktop\check1",r"C:\Users\100125\Desktop\check")

# move_a_file(r"C:\Users\100125\Desktop\check.txt",r"C:\Users\100125\Desktop\check")

# start_app(r"C:\Users\100125\Desktop\Excel.lnk")

# open_folder(r"C:\Users\100125\Desktop\説明書")
# close_folder(r"C:\Users\100125\Desktop\説明書")