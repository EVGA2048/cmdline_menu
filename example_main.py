#+----+----+----+----+----+----+----+----+----+----+----+
#                     CMDLINE_MENU
# 这是一个示例程序
# Developed by xxAp2005
# Last Update 2025/4/6Sat
# 
#+----+----+----+----+----+----+----+----+----+----+----+

import cmdline_menu
import time
import datetime

cmdline_menu.switch_sound()





#初始化cmdline_menu
#声明边框样式和菜单尺寸的全局变量
menuType = "small"
border_style = "dashed"

#边框样式分为 dashed 和 solid 两种
#solid  +------------------------+
#dashed +----+----+----+----+----+

#菜单尺寸分为 small medium large 三种
#+-----+-----+-----+-----+-----+-----+
#+-----+-----+-----+-----+-----+-----+-----+-----+
#+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

cmdline_menu.initialize_menu_type(menuType,border_style) #返回菜单尺寸和边框样式



cmdline_menu.clear_cmdline_x10()                   #清屏
cmdline_menu.drawBorder(menuType,border_style)     #绘制上边框
cmdline_menu.raw_text("            菜单标题")       #单行文字
cmdline_menu.singlespace()                         #单行空格
cmdline_menu.raw_text("输入任意选项继续...")        #单行文字
cmdline_menu.create_option("1","选项1")            #设置选项
cmdline_menu.create_option("2","选项2")            #设置选项
cmdline_menu.singlespace()                         #单行空格
cmdline_menu.drawBorder(menuType,border_style)     #绘制下边框
option = cmdline_menu.read_selection()             #读取选项
cmdline_menu.switch_sound()

#主菜单菜单
def main_menu():
    global option
    global menuType
    cmdline_menu.drawBorder(menuType,border_style)         #绘制上边框
    cmdline_menu.welcome_panel("今天想做点什么呢？")         #显示用户名称和日期的预设欢迎面板
    cmdline_menu.create_option("1","打印large尺寸的world")  #设置选项
    cmdline_menu.create_option("2","更改菜单尺寸")          #设置选项
    cmdline_menu.create_option("3","显示菜单尺寸")          #设置选项
    cmdline_menu.create_option("4","获取输入内容")          #设置选项
    cmdline_menu.create_option("5","带状态信息的打印示例")   #设置选项
    cmdline_menu.create_option("6","时间和日期示例")   #设置选项
    cmdline_menu.singlespace()                             #单行空格
    cmdline_menu.drawBorder(menuType,border_style)         #绘制下边框

    option = cmdline_menu.read_selection()                 #读取选项
    cmdline_menu.switch_sound()
    #对输入选项做出操作
    match option:
        case 1:
            global pause_key
            menuType = "large"
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            print("World")
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            cmdline_menu.switch_sound()
            main_menu()
        case 2:
            cmdline_menu.clear_cmdline_x10()
            change_menu_type()
        case 3:
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            print("debug: menuType=" + menuType)
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            cmdline_menu.switch_sound()
            main_menu()
        case 4:
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.singlespace()
            cmdline_menu.singlespace()
            print("获取输入内容")
            cmdline_menu.singlespace()
            cmdline_menu.singlespace()
            cmdline_menu.drawBorder(menuType,border_style)

            inputcontent = cmdline_menu.read_keyboardInput("请输入内容：")
            cmdline_menu.switch_sound()
            
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.singlespace()
            cmdline_menu.singlespace()
            print("您输入的内容为：")
            print(inputcontent)
            cmdline_menu.singlespace()
            cmdline_menu.singlespace()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            cmdline_menu.switch_sound()
            cmdline_menu.clear_cmdline_x10()
            main_menu()

        case 5:
            cmdline_menu.clear_cmdline_x20()
            cmdline_menu.echo_info("INFO","正在打印状态输出示例")
            time.sleep(0.5)
            cmdline_menu.echo_info("WARN","模拟输出警告信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("WARN","模拟输出警告信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("WARN","模拟输出警告信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("ERROR","模拟输出错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("ERROR","模拟输出错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("ERROR","模拟输出错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("FATAL","模拟输出严重错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("FATAL","模拟输出严重错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("FATAL","模拟输出严重错误信息")
            time.sleep(0.5)
            cmdline_menu.echo_info("INFO","示例已完成")
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            cmdline_menu.switch_sound()
            cmdline_menu.clear_cmdline_x10()
            main_menu()


        case 6:
            time_and_date_panel()

#子面板 - 更改菜单尺寸
def change_menu_type():
    global option
    global menuType
    cmdline_menu.clear_cmdline_x10()
    cmdline_menu.drawBorder(menuType,border_style)
    cmdline_menu.singlespace()
    cmdline_menu.raw_text("当前菜单尺寸为" + menuType)
    cmdline_menu.singlespace()
    cmdline_menu.raw_text("是否进行更改？")
    cmdline_menu.create_option("1","更改为small")
    cmdline_menu.create_option("2","更改为medium")
    cmdline_menu.create_option("3","更改为large")
    cmdline_menu.create_option("0","不更改")
    cmdline_menu.singlespace()
    cmdline_menu.drawBorder(menuType,border_style)

    option = cmdline_menu.read_selection()
    cmdline_menu.switch_sound()

    match option:
        case 1:
            menuType = "small"
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.header_space("small")
        case 2:
            menuType = "medium"
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.header_space("medium")
        case 3:
            menuType = "large"
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.header_space("large")
        case 0:
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType,border_style)
            cmdline_menu.raw_text("未作出任何修改")
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType,border_style)
            pause_key = input()
    #返回主菜单
    cmdline_menu.clear_cmdline_x10()
    main_menu()

def time_and_date_panel():
    while True:
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        cmdline_menu.drawBorder("medium","dashed")
        cmdline_menu.welcome_panel("日期和时间")
        cmdline_menu.singlespace()
        cmdline_menu.raw_text("当前时间    " + str(formatted_time))
        cmdline_menu.singlespace()
        cmdline_menu.drawBorder("medium","dashed")
        time.sleep(1)
        cmdline_menu.full_clear()

    

#运行主菜单
main_menu()
        
            

