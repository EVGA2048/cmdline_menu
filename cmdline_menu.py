#Developed by xxAp2005

#import time
# 导入datetime模块
import datetime

import os


#检测是否执行初始化
initialized = "false"

#获取系统用户名
username = os.getlogin()

#初始化头空格全局变量
headerSpace = "    "

# 获取当前日期
current_date = datetime.date.today()

# 格式化日期
formatted_date = current_date.strftime("%Y-%m-%d")


#从目标程序获取菜单类型
def initialize_menu_type(menu_type):
    global initialized
    global menuType
    if menu_type not in ["small", "medium", "large"]:
        print("无效的菜单类型. 选择 'small', 'medium', 或者 'large'.")
        print("cmdlineMENU初始化失败，菜单类型已缺省为small！")
        menuType = "small"
    print("debug: menuType设置为" + menu_type)
    menuType = menu_type
    initialized = "true"
    print("debug:initialized = " + initialized + " menuType=" + menuType)




def clear_cmdline_x10():                                    #生成10行空格用于清屏
    for _ in range(10):
        print(" ")



def small_border():                                         #打印小尺寸边框
    print("+-----+-----+-----+-----+-----+-----+")

def medium_border():                                        #打印中尺寸边框
    print("+-----+-----+-----+-----+-----+-----+-----+-----+")

def large_border():                                         #打印大尺寸边框
    print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")



def drawBorder(menuType):                                           #打印边框
    if menuType == "small":
        small_border()
    
    if menuType == "medium":
        medium_border()
    
    if menuType == "large":
        large_border()



def header_space(menuType):
    global headerSpace
    if menuType == "small":
        headerSpace = "    "
    
    if menuType == "medium":
        headerSpace = "        "

    if menuType == "large":
        headerSpace = "            "
    


def create_option(sequence_number, option_text):            #新建选项
    global menuType
    if menuType == "small":
        print("    ")
        print(headerSpace + "["+ sequence_number +"]" + option_text)

    if menuType == "medium":
        print("            ")
        print(headerSpace + "            ["+ sequence_number +"]" + option_text)

    if menuType == "large":
        print("            ")
        print(headerSpace + "            ["+ sequence_number +"]" + option_text)



def read_selection():                                       #读取选项
    selection = int(input("请输入选项序号："))
    return selection



def singlespace():                                          #换行
    print(" ")



def raw_text(text):                                         #打印文本
    print(headerSpace + text)



def welcome_panel(motd):
    singlespace()
    print(headerSpace + "欢迎!  " + username + "     现在是 " + formatted_date)
    singlespace()
    raw_text(headerSpace + motd)
