# cmdline_menu 命令行菜单
# developed by EVGA2048
用于快速搭建python命令行程序的交互界面

特点：
1.*不需要添加额外的requirements
2.*使主程序代码看起来整洁
3.*原理简单易上手

使用方法：
1. 使用git clone将仓库克隆到本地
2. 将cmdline_menu.py添加到项目文件夹中
3. 在需要打印菜单的程序中import cmdline_menu
4. 在初始化部分设置menu菜单的规格（小 中 大）
5. 调用cmdline_menu.函数即可使用

项目仓库中的example_main.py为一个示例主程序

若有建议或出现任何问题，请提交pr

函数说明：
    
    在使用前，请先用以下三行代码进行初始化：
    menuType = "small"
    border_style = "dashed"
    cmdline_menu.initialize_menu_type(menuType,border_style) #返回菜单尺寸和边框样式



    clear_cmdline_x10()
    生成10行空格起到清屏而不会清除之前消息记录的作用，连用两次效果最佳



    drawBorder(menuType,border_style) 
    绘制边框，传入初始化时赋值的菜单尺寸和边框样式

    #边框样式分为 dashed 和 solid 两种
    #solid  +------------------------+
    #dashed +----+----+----+----+----+

    #菜单尺寸分为 small medium large 三种
    #+-----+-----+-----+-----+-----+-----+
    #+-----+-----+-----+-----+-----+-----+-----+-----+
    #+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

    #主菜单建议使用medium，一些确认选项的菜单可以用small

    也可以手动选择尺寸直接绘制
    small_border(border_style)
    medium_border(border_style)
    large_border(border_style)



    header_space(menuType)
    用于更改缩进长度，在手动更改菜单大小后，绘制前请先执行此函数



    create_option(sequence_number, option_text)
    用于创建带序号的选项
    显示效果如下
    
    create_option("1", "这是选项1")
    [1] 这是选项1



    read_selection()
    用于读取用户输入选项，配合match效果最佳
    使用示例：
    
    [......菜单部分函数......]
    option = read_selection()
    match option:
        case 1:
            选择选项1后执行的程序
        case 2:
            选择选项2后执行的程序

    显示效果：
    +---------------+
    [1] 选项1
    [2] 选项2
    +---------------+
    请输入选项序号：



    read_keyboardInput(title)
    读取用户输入的文本，将title替换为你想问的
    比如"请输入密码："



    raw_text(text)
    生成一行带缩进的文本



    welcome_panel(motd)
    用于在主菜单上显示的欢迎面板，可以显示系统用户名和日期
    不多解释了，原代码很好理解罢（
    def welcome_panel(motd):
    singlespace()
    print(headerSpace + f"欢迎!  {username}     今天是 {formatted_date}")
    singlespace()
    raw_text(motd)

