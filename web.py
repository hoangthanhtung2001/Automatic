import csv
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from varriable import substring_from_charector_after
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-session-crashed-bubble")

def append_to_csv(filename, data, columns):
    # Kiểm tra xem tệp CSV đã tồn tại hay chưa
    file_exists = os.path.exists(filename)

    # Mở tệp CSV ở chế độ append (nếu tệp đã tồn tại) hoặc tạo một tệp mới
    with open(filename, "a", newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)

        # Nếu tệp CSV mới được tạo, ghi tên cột
        if not file_exists:
            writer.writeheader()

        # Tạo một dictionary mới từ dữ liệu và cột
        row_data = {column: value for column, value in zip(columns, data)}

        # Ghi dữ liệu vào tệp CSV
        writer.writerow(row_data)
        

csv_columns = ["Mã số", "Tên tỉnh", "Kanji","Hiragana","Thủ phủ","Vùng","Đảo","Diện tích"]  # Thay bằng tên cột thực tế

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://nhatban.net.vn/thu-vien/47-tinh-thanh-pho-o-nhat-ban.html")
# # # Chờ cho trang web thay đổi hoàn toàn
# WebDriverWait(driver, 30).until(
#     EC.staleness_of(driver.find_element(By.TAG_NAME, 'tr'))
# )

list_Elements = driver.find_elements(By.TAG_NAME,'tr')
if list_Elements:
    list_Elements_expect_firts = list_Elements[1:]

print(len(list_Elements_expect_firts))
m=0
dataArr =[]
while m<len(list_Elements_expect_firts):
    td_Elements=list_Elements_expect_firts[m].find_elements(By.TAG_NAME,'td')
    n=0
    while n<len(csv_columns):
        text= td_Elements[n].get_attribute("textContent").strip()
        dataArr.append(text)
        n=n+1
    try:
        append_to_csv("./data.csv",dataArr,csv_columns)
    except UnicodeEncodeError:
        for textValue in dataArr:
            print('error value',textValue)
    dataArr=[]
    m=m+1

df = pd.read_csv("./data.csv")
print(df) 


# time.sleep(1)
        
# ul_Elements = driver.find_element(By.CSS_SELECTOR,"ul.menu-list")
# if ul_Elements:
#     li_Element=ul_Elements.find_element(By.ID,"item-0")
#     if ul_Elements:
#         ActionChains(driver)\
#             .click(li_Element)\
#             .perform()

# input_name = driver.find_element(By.ID,"userName")
# input_email = driver.find_element(By.ID,"userEmail")
# input_current_address = driver.find_element(By.ID,"currentAddress")
# input_permanent_address = driver.find_element(By.ID,"permanentAddress")
# input_submit = driver.find_element(By.ID,"submit")
# if input_name:
#     ActionChains(driver)\
#         .send_keys_to_element(input_name,"Hoang Thanh Tung")\
#         .perform()
        
# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element_value((By.ID, "userName"), "Hoang Thanh Tung")
# )

# if input_email:
#     ActionChains(driver)\
#         .send_keys_to_element(input_email,"abc@gmail.com")\
#         .perform()
        
# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element_value((By.ID, "userEmail"), "abc@gmail.com")
# )

# if input_current_address:
#     ActionChains(driver)\
#         .send_keys_to_element(input_current_address,"qweokwqoekwqope")\
#         .perform()

# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element_value((By.ID, "currentAddress"), "qweokwqoekwqope")
# )

# if input_permanent_address:
#     ActionChains(driver)\
#         .send_keys_to_element(input_permanent_address,'opwqopwqeopqw')\
#         .perform()
        
# WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element_value((By.ID, "permanentAddress"), "opwqopwqeopqw")
# )

# if input_submit:
#     ActionChains(driver)\
#         .click(input_submit)\
#         .perform()
             
# time.sleep(2)




# name_Value = driver.find_element(By.ID,'name')
# if name_Value:
#     dataArr.append(substring_from_charector_after(name_Value.get_attribute("textContent"),":",2))
    
# email_Value = driver.find_element(By.ID,'email')
# if email_Value:
#     dataArr.append(substring_from_charector_after(email_Value.get_attribute("textContent"),":",2))
# currentAddress_Value = driver.find_element(By.CSS_SELECTOR,'p#currentAddress')
# if currentAddress_Value:
#     dataArr.append(substring_from_charector_after(currentAddress_Value.get_attribute("textContent").strip(),":",2))
# permanentAddress_Value = driver.find_element(By.CSS_SELECTOR,'p#permanentAddress')
# if permanentAddress_Value:
#     dataArr.append(substring_from_charector_after(permanentAddress_Value.get_attribute("textContent").strip(),":",2))

# append_to_csv("./data.csv",dataArr,csv_columns)

# time.sleep(2)



driver.quit()
