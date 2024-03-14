from datetime import datetime, timedelta
import math
import re
def variable(a):
    return a


def get_date_and_time(day_step=0, month_step=0, month_day_type=True, out_put='yyyy/mm/dd', date_setting=0):
    # Lấy ngày và giờ hiện tại
    current_date = datetime.now()
    
    # Nếu không có sự thay đổi trong date_setting, day_step và month_step, trả về ngày hiện tại
    if date_setting == 0 and day_step == 0 and month_step == 0:
        formatted_date = current_date.strftime('%Y/%m/%d')
    else:
        # Thay đổi ngày nếu day_step khác 0
        current_date += timedelta(days=day_step)
        
        # Thay đổi tháng nếu month_step khác 0
        current_date += timedelta(days=30 * month_step)
        
        # Trả về ngày đầu hoặc cuối tháng nếu date_setting được chỉ định
        if date_setting == 1:
            current_date = current_date.replace(day=1)
        elif date_setting == 2:
            current_date = current_date.replace(day=1)
            current_date += timedelta(days=32)
            current_date = current_date.replace(day=1) - timedelta(days=1)
        
        # Định dạng ngày tháng nếu được yêu cầu
        if month_day_type:
            formatted_date = current_date.strftime('%Y/%m/%d')
        else:
            formatted_date = current_date.strftime('%Y/%-m/%-d')

    # Trả về theo định dạng yêu cầu
    if out_put == 'yyyy/mm/dd':
        return formatted_date
    elif out_put == 'yy/mm/dd':
        return formatted_date[2:]
    elif out_put == 'yyyymmdd':
        return formatted_date.replace('/', '')
    elif out_put == 'yymmdd':
        return formatted_date[2:].replace('/', '')
    elif out_put == 'yyyy/mm':
        return formatted_date[:-3]
    elif out_put == 'yy/mm':
        return formatted_date[2:-3]
    elif out_put == 'yyyymm':
        return formatted_date[:-6] + formatted_date[-3:]
    elif out_put == 'yymm':
        return formatted_date[2:-6] + formatted_date[-3:]
    elif out_put == 'mm/dd':
        return formatted_date[5:]
    elif out_put == 'mmdd':
        return formatted_date[5:].replace('/', '')
    elif out_put == 'yyyy':
        return formatted_date[:4]
    elif out_put == 'mm':
        return formatted_date[5:7]
    elif out_put == 'dd':
        return formatted_date[8:]
    elif out_put == 'hhmm':
        return current_date.strftime('%H%M')
    elif out_put == 'hhmmss':
        return current_date.strftime('%H%M%S')
    elif out_put == 'ngày trong tuần':
        return current_date.strftime('%A')

# # Sử dụng hàm với các giá trị mặc định
# print(get_date_and_time(date_setting=0,day_step=-1))

def push_string(*args):
    result = ''
    for s in args:
        if s is not None:
            result += s
    return result


def change_string(text,type_change=None,before_change_charector = None,after_change_charector = None):
    if type_change == 1 and before_change_charector is not None and after_change_charector is not None:
        return text.replace(before_change_charector,after_change_charector)
    elif type_change == 2:
        return text.replace('\n', '')
    elif type_change == 3:
        return text.replace(' ', '')
    else:
        return text



def math_func(value1,value2,type_math=1,type_return=None,round_index=0):
    if not isinstance(value1,int) and not isinstance(value1,float):
        value1 = 0
        print("Value1 khong phai so")
    if not isinstance(value2,int) and not isinstance(value2,float):
        value2 = 0
        print("Value2 khong phai so")
    if type_math == 2:
        result = value1 -value2
        if type_return ==1:
            return round(result,round_index)
        elif type_return ==2:
            return round(math.floor(result),round_index)
        elif type_return ==3:
            return round(math.ceil(result),round_index)
        else:
            return result
    elif type_math == 3:
        result = value1*value2
        if type_return ==1:
            return round(result,round_index)
        elif type_return ==2:
            return round(math.floor(result),round_index)
        elif type_return ==3:
            return round(math.ceil(result),round_index)
        else:
            return result
    elif type_math == 4:
        result = value1/value2
        if type_return ==1:
            return round(result,round_index)
        elif type_return ==2:
            return round(math.floor(result),round_index)
        elif type_return ==3:
            return round(math.ceil(result),round_index)
        else:
            return result
    else:
        result = value1+value2
        if type_return ==1:
            return round(result,round_index)
        elif type_return ==2:
            return round(math.floor(result),round_index)
        elif type_return ==3:
            return round(math.ceil(result),round_index)
        else:
            return result



# Cat lay chuoi
def substring_from_charector_before(text,find_charector,type=1,charector_index=1):
    indexes = [
        match.start() for match in re.finditer(find_charector, text)
    ]
    if charector_index > len(indexes):
        print("Khong tim thay vi tri tai index chi dinh")
        return
    
    index = indexes[charector_index-1]
    
    if type == 2:
        return text[:index+1] #chuoi tra ve bao gom ca ki tu chi dinh
    else:
        return text[:index] #chuoi tra ve khong bao gom ki tu chi dinh
    
# print(substring_from_charector_before("texth23h",'h',charector_index=2))
def substring_from_charector_after(text,find_charector,type=1,charector_index=1):
    indexes = [
        match.start() for match in re.finditer(find_charector, text)
    ]
    if charector_index > len(indexes):
        print("Khong tim thay vi tri tai index chi dinh")
        return
    
    index = indexes[charector_index-1]
    
    if type == 2:
        return text[index+1:] #chuoi tra ve bao gom ca ki tu chi dinh
    else:
        return text[index:] #chuoi tra ve khong bao gom ki tu chi dinh
    
# print(substring_from_charector_after("texth23h",'h',charector_index=1,type=2))
