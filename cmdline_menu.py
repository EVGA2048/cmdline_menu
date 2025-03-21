#import time





def initialize_menu_type(menu_type):
    global menuType
    if menu_type not in ["small", "medium", "large"]:
        print("无效的菜单类型. 选择 'small', 'medium', 或者 'large'.")
        print("cmdlineMENU初始化失败，菜单类型已缺省为small！")
        menuType = "small"
    print("debug: menuType设置为" + menu_type)
    menuType = menu_type








def clear_cmdline_x10():                                    #调用此函数生成10行空格用于清屏
    for _ in range(10):
        print(" ")

def short_border():
    print("+-----+-----+-----+-----+-----+-----+")

def medium_border():
    print("+-----+-----+-----+-----+-----+-----+-----+-----+")

def large_border():
    print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")

def drawBorder():
    if menuType == "short":
        short_border()
    
    if menuType == "medium":
        medium_border()
    
    if menuType == "large":
        large_border()
    
def create_option(sequence_number, option_text):
    if menuType == "short":
        print("    ")
        print("["+ sequence_number +"]" + option_text)

    if menuType == "medium":
        print("            ")
        print("            ["+ sequence_number +"]" + option_text)

    if menuType == "large":
        print("            ")
        print("            ["+ sequence_number +"]" + option_text)

def read_selection():
    selection = int(input("请输入选项序号："))
    return selection

def singlespace():
    print(" ")

def raw_text(text):
    print(text)
