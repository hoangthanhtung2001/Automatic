from wait import check_image_on_screen
import time


def while_conditional(conditional_name:list,conditional_value:list,equal="=",run_program=None,conditional_type=1):
    
   def check_conditional(equal,conditional_type,conditional_name,conditional_value):
    if equal == "=":
        if conditional_type ==1:
            result = all(conditional_name[i] == conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] == conditional_value[i] for i in range(len(conditional_name)))
            return result
        
    elif equal =="!=":
        if conditional_type ==1:
          result = all(conditional_name[i] != conditional_value[i] for i in range(len(conditional_name)))
          return result
        else:
          result = any(conditional_name[i] != conditional_value[i] for i in range(len(conditional_name)))
          return result 
           
    elif equal ==">":
        if conditional_type ==1:
            result = all(conditional_name[i] > conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] > conditional_value[i] for i in range(len(conditional_name)))
            return result
            
    elif equal =="<":
        if conditional_type ==1:
            result = all(conditional_name[i] < conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] < conditional_value[i] for i in range(len(conditional_name)))
            return result
        
    elif equal ==">=":
        if conditional_type ==1:
            result = all(conditional_name[i] >= conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] >= conditional_value[i] for i in range(len(conditional_name)))
            return result
    elif equal =="<=":
        if conditional_type ==1:
            result = all(conditional_name[i] <= conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] <= conditional_value[i] for i in range(len(conditional_name)))
            return result
            
    elif equal =="in":
        if conditional_type ==1:
            result = all(conditional_name[i] in conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] in conditional_value[i] for i in range(len(conditional_name)))
            return result
    else:
        if conditional_type ==1:           
            result = all(conditional_name[i] not in conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] not in conditional_value[i] for i in range(len(conditional_name)))
            return result
     
   while check_conditional(equal,conditional_type,conditional_name,conditional_value):
        run_program()
        time.sleep(1)
        check_conditional(equal,conditional_type,conditional_name,conditional_value)
   print("Exit Loop")
    # print(result)
    
def while_conditional_with_image_disappear(image_file_path,run_program):
    result =True
    while result:
        run_program()
        time.sleep(1)
        result = check_image_on_screen(image_file_path,1)
    print("Exit Loop") 
def while_conditional_with_image_appear(image_file_path,run_program):
    result =False
    while not result:
        run_program()
        time.sleep(1)
        result = check_image_on_screen(image_file_path,1) 
    print("Exit Loop")
def test():
    print("Loop dang dien ra")   

while_conditional_with_image_disappear("./screen_shot/test.png",test)
# while_conditional([1,1],[1,0],">",test,2)

def if_conditional(conditional_name:list,conditional_value:list,equal="=",run_program=None,conditional_type=1):
    
   def check_conditional(equal,conditional_type,conditional_name,conditional_value):
    if equal == "=":
        if conditional_type ==1:
            result = all(conditional_name[i] == conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] == conditional_value[i] for i in range(len(conditional_name)))
            return result
        
    elif equal =="!=":
        if conditional_type ==1:
          result = all(conditional_name[i] != conditional_value[i] for i in range(len(conditional_name)))
          return result
        else:
          result = any(conditional_name[i] != conditional_value[i] for i in range(len(conditional_name)))
          return result 
           
    elif equal ==">":
        if conditional_type ==1:
            result = all(conditional_name[i] > conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] > conditional_value[i] for i in range(len(conditional_name)))
            return result
            
    elif equal =="<":
        if conditional_type ==1:
            result = all(conditional_name[i] < conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] < conditional_value[i] for i in range(len(conditional_name)))
            return result
        
    elif equal ==">=":
        if conditional_type ==1:
            result = all(conditional_name[i] >= conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] >= conditional_value[i] for i in range(len(conditional_name)))
            return result
    elif equal =="<=":
        if conditional_type ==1:
            result = all(conditional_name[i] <= conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] <= conditional_value[i] for i in range(len(conditional_name)))
            return result
            
    elif equal =="in":
        if conditional_type ==1:
            result = all(conditional_name[i] in conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] in conditional_value[i] for i in range(len(conditional_name)))
            return result
    else:
        if conditional_type ==1:           
            result = all(conditional_name[i] not in conditional_value[i] for i in range(len(conditional_name)))
            return result
        else:
            result = any(conditional_name[i] not in conditional_value[i] for i in range(len(conditional_name)))
            return result
     
   if check_conditional(equal,conditional_type,conditional_name,conditional_value):
        run_program()
    # print(result)
    
# if_conditional([1,1],[1,0],">",test,2)
def if_conditional_with_image_appear(image_file_path,run_program):
    result = check_image_on_screen(image_file_path,1)
    if result:
        run_program()
    print("Exit Loop") 
    
# if_conditional_with_image_appear("./screen_shot/test.png",test)

