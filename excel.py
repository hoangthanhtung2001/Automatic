import win32com.client
import win32gui, win32con
from window_app import open_window
import re
import difflib
def excel_list():
     # ------------------------------------------------------------------
    # Excelの定数を設定
    # ------------------------------------------------------------------
    # https://excel-ubara.com/EXCEL/EXCEL905.html
    # https://docs.microsoft.com/en-us/office/vba/api/excel(enumerations)
    # https://docs.microsoft.com/ja-jp/office/vba/api/excel(enumerations)
    # ------------------------------------------------------------------
    # Excelの定数を取得する方法もあるようです。
    # https://wacky.hatenadiary.com/entry/20091011/1255240572
    # ------------------------------------------------------------------
    # Excel Enum Constants
    # ------------------------------------------------------------------
    xlAbove = 0
    xlBelow = 1
    xlSolid = 1
    xlFirst = 0
    xlLast = 1
    xlLastCell = 11
    xlTopToBottom = 1
    xlLeftToRight = 2
    xlGeneral = 1
    xlAutomatic = -4105
    xlFormats = -4122
    xlNone = -4142
    xlCenter = -4108
    xlDistributed = -4117
    xlJustify = -4130
    xlBottom = -4107
    xlLeft = -4131
    xlRight = -4152
    xlTop = -4160
    xlRTL = -5004
    xlLTR = -5003
    xlContext = -5002
    # ------------------------------------------------------------------
    # Excel Enum XlAutoFillType
    # ------------------------------------------------------------------
    xlFillDefault = 0
    xlFillCopy = 1
    xlFillSeries = 2
    xlFillFormats = 3
    xlFillValues = 4
    xlFillDays = 5
    xlFillWeekdays = 6
    xlFillMonths = 7
    xlFillYears = 8
    xlLinearTrend = 9
    xlGrowthTrend = 10
    xlFlashFill = 11
    # ------------------------------------------------------------------
    # Excel Enum XlAutoFilterOperator
    # ------------------------------------------------------------------
    xlAnd = 1
    xlOr = 2
    xlTop10Items = 3
    xlBottom10Items = 4
    xlTop10Percent = 5
    xlBottom10Percent = 6
    xlFilterValues = 7
    xlFilterCellColor = 8
    xlFilterFontColor = 9
    xlFilterIcon = 10
    xlFilterDynamic = 11
    # ------------------------------------------------------------------
    # Excel Enum XLBordersIndex
    # ------------------------------------------------------------------
    xlDiagonalDown = 5
    xlDiagonalUp = 6
    xlEdgeLeft = 7
    xlEdgeTop = 8
    xlEdgeBottom = 9
    xlEdgeRight = 10
    xlInsideHorizontal = 12
    xlInsideVertical = 11
    # ------------------------------------------------------------------
    # Excel Enum XLBorderWeight
    # ------------------------------------------------------------------
    xlHairline = 1
    xlThin = 2
    xlThick = 4
    xlMedium = -4138
    # ------------------------------------------------------------------
    # Excel Enum XlCellType
    # ------------------------------------------------------------------
    xlCellTypeConstants = 2
    xlCellTypeBlanks = 4
    xlCellTypeLastCell = 11
    xlCellTypeVisible = 12
    xlCellTypeFormulas = -4123
    xlCellTypeComments = -4144
    xlCellTypeAllFormatConditions = -4172
    xlCellTypeSameFormatConditions = -4173
    xlCellTypeAllValidation = -4174
    xlCellTypeSameValidation = -4175
    # ------------------------------------------------------------------
    # Excel Enum XlColorIndex
    # ------------------------------------------------------------------
    xlColorIndexAutomatic = -4105
    xlColorIndexNone = -4142
    # ------------------------------------------------------------------
    # Excel Enum XlCutCopyMode
    # ------------------------------------------------------------------
    xlCopy = 1
    xlCut = 2
    # ------------------------------------------------------------------
    # Excel Enum XlDeleteShiftDirection
    # Excel Enum XlInsertShiftDirection
    # ------------------------------------------------------------------
    xlShiftUp = -4162
    xlShiftDown = -4121
    xlShiftToLeft = -4159
    xlShiftToRight = -4161
    # ------------------------------------------------------------------
    # Excel Enum XlDirection
    # ------------------------------------------------------------------
    xlUp = -4162
    xlDown = -4121
    xlToLeft = -4159
    xlToRight = -4161
    # ------------------------------------------------------------------
    # Excel Enum XlFileFormat
    # ------------------------------------------------------------------
    xlCSV = 6
    xlHtml = 44
    xlWorkbookDefault = 51
    xlOpenXMLWorkbook = 51
    xlOpenXMLWorkbookMacroEnabled = 52
    xlWorkbookNormal = -4143
    xlCurrentPlatformText = -4158
    # ------------------------------------------------------------------
    # Excel Enum XlFixedFormatType
    # ------------------------------------------------------------------
    xlTypePDF = 0
    xlTypeXPS = 1
    # ------------------------------------------------------------------
    # Excel Enum XlFixedFormatQuality
    # ------------------------------------------------------------------
    xlQualityStandard = 0
    xlQualityMinimum = 1
    # ------------------------------------------------------------------
    # Excel Enum XlFindLookIn
    # ------------------------------------------------------------------
    xlFormulas = -4123
    xlComments = -4144
    xlValues = -4163
    # ------------------------------------------------------------------
    # Excel Enum XlLineStyle
    # ------------------------------------------------------------------
    xlContinuous = 1
    xlDashDot = 4
    xlDashDotDot = 5
    xlSlantDashDot = 13
    xlDash = -4115
    xldot = -4118
    xlDouble = -4119
    xlLineStyleNone = -4142
    # ------------------------------------------------------------------
    # Excel Enum XlOrientation
    # ------------------------------------------------------------------
    xlHorizontal = -4128
    xlVertical = -4166
    xlDownward = -4170
    xlUpward = -4171
    # ------------------------------------------------------------------
    # Excel Enum XlPasteType
    # ------------------------------------------------------------------
    xlPasteValues = -4163
    xlPasteComments = -4144
    xlPasteFormulas = -4123
    xlPasteFormats = -4122
    xlPasteAll = -4104
    xlPasteValidation = 6
    xlPasteAllExceptBorders = 7
    xlPasteColumnWidths = 8
    xlPasteFormulasAndNumberFormats = 11
    xlPasteValuesAndNumberFormats = 12
    xlPasteAllUsingSourceTheme = 13
    xlPasteAllMergingConditionalFormats = 14
    # ------------------------------------------------------------------
    # Excel Enum XlSheetVisibility
    # ------------------------------------------------------------------
    xlSheetVisible = -1
    xlSheetHidden = 0
    xlSheetVeryHidden = 2
    # ------------------------------------------------------------------
    # Excel Enum XlSpecialCellsValue
    # ------------------------------------------------------------------
    xlNumbers = 1
    xlTextValues = 2
    xlLogical = 4
    xlErrors = 16
    # ------------------------------------------------------------------
    # Excel Enum XlSortDataOption
    # ------------------------------------------------------------------
    xlSortNormal = 0
    xlSortTextAsNumbers = 1
    # ------------------------------------------------------------------
    # Excel Enum XlSortMethod
    # ------------------------------------------------------------------
    xlPinYin = 1
    xlStroke = 2
    # ------------------------------------------------------------------
    # Excel Enum XlSortOrder
    # ------------------------------------------------------------------
    xlAscending = 1
    xlDescending = 2
    xlManual = -4135
    # ------------------------------------------------------------------
    # Excel Enum XlSortOrientation
    # ------------------------------------------------------------------
    xlSortColumns = 1
    xlSortRows = 2
    # ------------------------------------------------------------------
    # Excel Enum XlSortOn
    # ------------------------------------------------------------------
    xlSortOnValues = 0
    xlSortOnCellColor = 1
    xlSortOnFontColor = 2
    xlSortOnIcon = 3
    # ------------------------------------------------------------------
    # Excel Enum XlSortType
    # ------------------------------------------------------------------
    xlSortValues = 1
    xlSortLabels = 2
    # ------------------------------------------------------------------
    # Excel Enum XlUnderlineStyle
    # ------------------------------------------------------------------
    xlUnderlineStyleNone = -4142
    xlUnderlineStyleDouble = -4119
    xlUnderlineStyleSingle = 2
    xlUnderlineStyleSingleAccounting = 4
    xlUnderlineStyleDoubleAccounting = 5
    # ------------------------------------------------------------------
    # Excel Enum XlYesNoGuess
    # ------------------------------------------------------------------
    xlGuess = 0
    xlYes = 1
    xlNo = 2
    # ------------------------------------------------------------------

#suport_func
def search_string_in_array_by_string(array, target_string):
    for string in array:
        similarity = difflib.SequenceMatcher(None, string, target_string).ratio()
        if similarity >= 0.2:  # Điều chỉnh ngưỡng tùy ý
            return string
    return None

def search_string_in_array_complete_by_string(array, target_string):
    for string in array:
        similarity = difflib.SequenceMatcher(None, string, target_string).ratio()
        if similarity == 1:  # Điều chỉnh ngưỡng tùy ý
            return string
    return None

def maximum_excel_size():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

def search_string_in_array(array, target_string):
    for string in array:
        if string.find(target_string) != -1:
            return True
    return False

def search_string_in_array_complete(array, target_string):
    return target_string in array
#suport_func

#main_func
def excel_open(file_path,sheet_setting=0,sheet_name=None,maximum=True):
    xl = win32com.client.Dispatch("Excel.Application")

    indexes = [
        match.start() for match in re.finditer('\\\\',file_path)
    ]
    
    file_name = file_path[indexes[len(indexes)-1]+1:]

    workbook = xl.Workbooks.Open(file_path)
    xl.Visible = True  # Hiển thị ứng dụng Excel
    sheet_names = [sheet.Name for sheet in workbook.Sheets]
    if maximum:
        maximum_excel_size()
    if sheet_setting == 1 and sheet_name is not None:
        if search_string_in_array(sheet_names,sheet_name):
            xl.Sheets(sheet_name).Activate()
    if sheet_setting == 2 and sheet_name is not None:
        if search_string_in_array_complete(sheet_names,sheet_name):
            xl.Sheets(sheet_name).Activate()
    open_window(file_name)
    
    

def excel_close(file_path, close_type=1, new_path=None, file_type=None):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
   
    if close_type == 2:
        workbook.Close(SaveChanges=False)
        xl.Quit()
    elif close_type == 3 and new_path is not None:
        if file_type == 1:
            workbook.SaveAs(Filename=f"{new_path}\\outputSaveAs.xlsx", FileFormat=51)
            xl.Quit()
        elif file_type == 2:
            workbook.SaveAs(Filename=f"{new_path}\\outputSaveAs.xlsx", FileFormat=-4143)
            xl.Quit()
        elif file_type == 3:
            workbook.SaveAs(Filename=f"{new_path}\\outputSaveAs.csv", FileFormat=6)
            xl.Quit()
    else:
        workbook.Save()
        workbook.Close()
        xl.Quit()


def cell_choice(file_path, col, row):
    xl = win32com.client.Dispatch("Excel.Application")
    # indexes = [
    #     match.start() for match in re.finditer('\\\\',file_path)
    # ]
    
    # file_name = file_path[indexes[len(indexes)-1]+1:]
    # open_window(file_name)
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    
    # Assuming that col and row are integers
    
    col_index = xl.Range(f"{col}1").Column
    cell = xl.Cells(row, col_index)
    cell.Select()

def sheet_select(file_path,select_tye,sheet_name=None):
    xl = win32com.client.Dispatch("Excel.Application")
    
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    
    sheet_names = [sheet.Name for sheet in workbook.Sheets]
    if select_tye ==1 and sheet_name is not None:
        if search_string_in_array(sheet_names,sheet_name):
            result = search_string_in_array_by_string(sheet_names, sheet_name)
            xl.Sheets(result).Activate()
        else:
            print("Khong co sheet name nao trung khop")
    if select_tye ==2 and sheet_name is not None:
        if search_string_in_array_complete(sheet_names,sheet_name):
            result = search_string_in_array_complete_by_string(sheet_names, sheet_name)
            xl.Sheets(result).Activate()
        else:
            print("Khong co sheet name nao trung khop")
            

def shell_select_and_cell_choice(file_path,col,row,select_tye,sheet_name=None):
    xl = win32com.client.Dispatch("Excel.Application")
    
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    
    sheet_names = [sheet.Name for sheet in workbook.Sheets]
    if select_tye ==1 and sheet_name is not None:
        if search_string_in_array(sheet_names,sheet_name):
            result = search_string_in_array_by_string(sheet_names, sheet_name)
            xl.Sheets(result).Activate()
            cell_choice(file_path,col,row)
        else:
            print("Khong co sheet name nao trung khop")
    if select_tye ==2 and sheet_name is not None:
        if search_string_in_array_complete(sheet_names,sheet_name):
            result = search_string_in_array_complete_by_string(sheet_names, sheet_name)
            xl.Sheets(result).Activate()
            cell_choice(file_path,col,row)
        else:
            print("Khong co sheet name nao trung khop")   

def selection(file_path,col_name_1,row_start,col_name_2,row_end):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    col_index_1 = xl.Range(f"{col_name_1}1").Column
    col_index_2 = xl.Range(f"{col_name_2}1").Column
    
    xl.Range(xl.Cells(row_start, col_index_1), xl.Cells(row_end, col_index_2)).Select()


#suport_func

def row_select(file_path,row_start,row_end):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Rows(f"{row_start}:{row_end}").Select()
    
def col_select(file_path,start_col,end_col):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Columns(f"{start_col}:{end_col}").Select()

def insert_col(file_path,start_col,end_col):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Columns(f"{start_col}:{end_col}").Insert()

def insert_row(file_path,start_row,end_row):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Rows(f"{start_row}:{end_row}").Insert()

def delete_row(file_path,start_row,end_row):
    xlShiftUp = -4162
    xlShiftDown = -4121
    xlShiftToLeft = -4159
    xlShiftToRight = -4161
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Rows(f"{start_row}:{end_row}").Delete(xlShiftUp)

def delete_col(file_path,start_col,end_col):
    xlShiftUp = -4162
    xlShiftDown = -4121
    xlShiftToLeft = -4159
    xlShiftToRight = -4161
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Columns(f"{start_col}:{end_col}").Delete(xlShiftToRight)

def copy_col(file_path,start_col,end_col):
    
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Columns(f"{start_col}:{end_col}").Copy()
    
def copy_row(file_path,start_row,end_row):
    
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    xl.Rows(f"{start_row}:{end_row}").Copy()

def paste_value(file_path,col,row):
    xlPasteValues = -4163
    xlPasteComments = -4144
    xlPasteFormulas = -4123
    xlPasteFormats = -4122
    xlPasteAll = -4104
    xlPasteValidation = 6
    xlPasteAllExceptBorders = 7
    xlPasteColumnWidths = 8
    xlPasteFormulasAndNumberFormats = 11
    xlPasteValuesAndNumberFormats = 12
    xlPasteAllUsingSourceTheme = 13
    xlPasteAllMergingConditionalFormats = 14
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    col_index = xl.Range(f"{col}1").Column
    xl.Cells(row, col_index).PasteSpecial(xlPasteValues)

    xl.CutCopyMode = False
    
def col_index_to_col_name(col_index):
    dividend = col_index
    column_name = ''
    while dividend > 0:
        modulo = (dividend - 1) % 26
        column_name = chr(65 + modulo) + column_name
        dividend = (dividend - modulo) // 26
    return column_name

#suport_func

def copy_value(file_path,col,row):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    col_index = xl.Range(f"{col}1").Column
    xl.Cells(row, col_index).Copy()

def find_value_excel(file_path,find_value):
    xl = win32com.client.Dispatch("Excel.Application")
    if file_path is not None:
        workbook = xl.Workbooks.Open(file_path)
    else:
        workbook = xl.ActiveWorkbook
    sheet = workbook.ActiveSheet
    num_rows = sheet.UsedRange.Rows.Count
    num_cols = sheet.UsedRange.Columns.Count
    address = None
        # Duyệt qua tất cả các ô trong sheet để tìm kiếm giá trị
    for row in range(1, num_rows + 1):
            for col in range(1, num_cols + 1):
                cell_value = sheet.Cells(row, col).Value
                if cell_value == find_value:
                    # Trả về địa chỉ của ô nếu tìm thấy giá trị
                    address = sheet.Cells(row, col).Address
                    print(f"Giá trị row la :{row}")
                    print(f"Giá trị col la :{col_index_to_col_name(col)}")
                    print(f"Giá trị {find_value} được tìm thấy tại ô {address}")
                    cell_choice(file_path,col_index_to_col_name(col),row)
                    return address
            
            if address is not None:
                break
find_value_excel(file_path=None,find_value="中村 尚")

# copy_value(file_path=None,col="B",row=2)

# # copy_row(file_path=None,start_row=3,end_row=3)
# paste_value(file_path=None,col="A",row=2)
# delete_row(file_path=None,start_row=1,end_row=2)
# insert_row(file_path=None,start_row=1,end_row="2")
# insert_col(file_path=None,start_col="A",end_col="C")
# delete_col(file_path=None,start_col="A",end_col="C")
# col_select(file_path=None,start_col="A",end_col="C")

# row_select(file_path=None,row_start=1,row_end=5)
# def col_row_select_and_hanlde(file_path):
     
# excel_open(r"C:\Users\100125\Desktop\WisOCRエントリー枚数実績管理表.xlsm")


# cell_choice(r"C:\Users\100125\Desktop\WisOCRエントリー枚数実績管理表.xlsm","G",2)

# sheet_select(file_path=None,select_tye=2,sheet_name="サンプル")

# shell_select_and_cell_choice(file_path=None,select_tye=2,sheet_name="サンプル",col="G",row=6)

# selection(file_path=None,col_name_1="A",row_start="1",col_name_2="D",row_end="8")


#main_func
