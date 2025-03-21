import cmdline_menu






menuType = "medium"
cmdline_menu.initialize_menu_type(menuType)
cmdline_menu.clear_cmdline_x10()
cmdline_menu.drawBorder()
cmdline_menu.raw_text("            菜单标题")
cmdline_menu.create_option("1","选项1")
cmdline_menu.create_option("2","选项2")
cmdline_menu.singlespace()
cmdline_menu.drawBorder()
option = cmdline_menu.read_selection()

match option:
    case 1:
        print("选择的结果为选项1")
    case 2:
        print("选择的结果为选项2")