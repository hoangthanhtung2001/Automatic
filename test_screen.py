from tkinter import *
import pyautogui
import datetime
def run_application():
 root = Tk()
 class Application():
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.file_path = None
        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=1)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)
        self.create_screen_canvas()

    def create_screen_canvas(self):
        self.master_screen.deiconify()
        root.withdraw()

        self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.snip_surface.pack(fill=BOTH, expand=YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.display_rectangle_position()

        # Lấy ảnh chụp không có border
        self.file_path = self.take_bounded_screenshot(self.start_x + 3, self.start_y + 3, self.current_x - self.start_x - 6, self.current_y - self.start_y - 6)

        self.exit_screenshot_mode()

    def exit_screenshot_mode(self):
        self.snip_surface.destroy()
        self.master_screen.withdraw()
        root.destroy()

    def on_button_press(self, event):
        # Lưu vị trí bắt đầu kéo chuột
        self.start_x = self.snip_surface.canvasx(event.x)
        self.start_y = self.snip_surface.canvasy(event.y)

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        # Vẽ hình chữ nhật tạm thời (không có border)
        self.update_temporary_rectangle()

    def display_rectangle_position(self):
        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)

    def update_temporary_rectangle(self):
        # Xóa hình chữ nhật cũ
        self.snip_surface.delete("temp_rect")
        # Vẽ hình chữ nhật mới
        self.snip_surface.create_rectangle(self.start_x, self.start_y, self.current_x, self.current_y, fill="", outline='red', width=3, tags="temp_rect")

    def take_bounded_screenshot(self, x1, y1, x2, y2):
        image = pyautogui.screenshot(region=(x1, y1, x2, y2))
        file_name = datetime.datetime.now().strftime("%f")
        file_path = file_name + ".png"
        image.save("./screen_shot/"+file_path)
        return file_path


 app = Application(root)
 root.mainloop()
 
