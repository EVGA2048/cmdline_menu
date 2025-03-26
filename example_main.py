import cmdline_menu





menuType = "small"
cmdline_menu.initialize_menu_type("small")



cmdline_menu.clear_cmdline_x10()
cmdline_menu.drawBorder("small")
cmdline_menu.raw_text("            菜单标题")
cmdline_menu.singlespace()
cmdline_menu.raw_text("输入任意选项继续...")
cmdline_menu.create_option("1","选项1")
cmdline_menu.create_option("2","选项2")
cmdline_menu.singlespace()
cmdline_menu.drawBorder("small")
option = cmdline_menu.read_selection()



def main_menu():
    global option
    global menuType
    cmdline_menu.drawBorder(menuType)
    cmdline_menu.welcome_panel("今天想做点什么呢？")
    cmdline_menu.create_option("1","打印Hello World")
    cmdline_menu.create_option("2","更改菜单尺寸")
    cmdline_menu.create_option("3","显示菜单尺寸")
    cmdline_menu.singlespace()
    cmdline_menu.drawBorder(menuType)

    option = cmdline_menu.read_selection()

    match option:
        case 1:
            global pause_key
            cmdline_menu.clear_cmdline_x10()
            cmdline_menu.drawBorder(menuType)
            print("Hello World")
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            main_menu()
        case 2:
            change_menu_type()
        case 3:
            cmdline_menu.drawBorder(menuType)
            print("debug: menuType=" + menuType)
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("请按任意键继续")
            pause_key = input()
            main_menu()

def change_menu_type():
    global option
    global menuType
    cmdline_menu.clear_cmdline_x10()
    cmdline_menu.drawBorder(menuType)
    cmdline_menu.singlespace()
    cmdline_menu.raw_text("当前菜单尺寸为" + menuType)
    cmdline_menu.singlespace()
    cmdline_menu.raw_text("是否进行更改？")
    cmdline_menu.create_option("1","更改为small")
    cmdline_menu.create_option("2","更改为medium")
    cmdline_menu.create_option("3","更改为large")
    cmdline_menu.create_option("0","不更改")
    cmdline_menu.singlespace()
    cmdline_menu.drawBorder(menuType)

    option = cmdline_menu.read_selection()

    match option:
        case 1:
            menuType = "small"
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType)
            menuType = "small"
        case 2:
            menuType = "medium"
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType)
            menuType = "medium"
        case 3:
            menuType = "large"
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("已更改菜单尺寸为" + menuType)
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType)
            menuType = "large"
        case 0:
            cmdline_menu.drawBorder(menuType)
            cmdline_menu.raw_text("未作出任何修改")
            cmdline_menu.singlespace()
            cmdline_menu.raw_text("按任意键返回")
            cmdline_menu.drawBorder(menuType)
            pause_key = input()
    
    main_menu()

match option:
    case 1:
        main_menu()
    case 2:
        main_menu()
            

