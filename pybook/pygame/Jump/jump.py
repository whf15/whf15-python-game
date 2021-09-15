import PIL, numpy  # 图像处理模块
import matplotlib.pyplot as plt  # 画图模块
from matplotlib.widgets import Button  # 按钮模块
import warnings  # 屏蔽警告

warnings.filterwarnings("ignore")

import os  # 系统模块
import time  # 时间模块
import threading  # 子线程模块

coor = []  # 保存选中位置的坐标
ax = None  # 子视图变量
isAuto = False  # 标记是否启动了自动模式


# 获取手机截图
def get_screen_image():
    # 通过adb命令截取当前手机界面，然后将截图保存在手机的sd卡根目录下
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 将手机中截图保存在当前项目文件夹当中
    os.system('adb pull /sdcard/screen.png')
    # 将打开的图片转换多维数组,并返回
    return numpy.array(PIL.Image.open('screen.png'))


# 坐标轴单击事件,event用于获取单击坐标点，coor用于保存单击的起始坐标点与结束坐标点
def on_click(event):
    if isAuto == False:  # 判断在没有启动自动跳跃模式时
        if event.xdata != None and event.ydata != None:  # 判断获取的坐标点是否为空
            # 获取单击的坐标点并转换为float类型
            x = float(event.xdata)
            y = float(event.ydata)
            # 此处判断为了躲避重选与自动按钮的坐标
            if x > 70 and y > 70:
                # 将单击坐标轴上的x，y坐标点添加到coor列表中
                coor.append((x, y))
                if len(coor) == 1:
                    print('选中起点')
                else:
                    print('选中终点')
                global ax
                ax = figure.add_subplot(1, 1, 1)  # 添加一个子图，也就是绘制我们选中的点
                ax.plot(x, y, 'r*')  # 绘制红色的*号
                figure.canvas.draw()  # 重画
                # 如果coor列表长度等于2时，说明已经获取了单击的起始位置与结束位置的坐标点
                if len(coor) == 2:
                    # 调用计算方法，将起始位置与结束位置的坐标点传递过去，然后清空坐标点
                    jump_to_next(coor.pop(), coor.pop())
                    ax.lines.clear()  # 清除选中绘制点
                    # 通过线程进行更新
                    th = threading.Thread(target=update)
                    th.start()
    else:
        print('已开启自动模式！')


# 实现跳跃的方法
def jump_to_next(point1, point2):  # 计算炫的长度
    x1, y1 = point1;  # 起始点坐标
    x2, y2 = point2;  # 结束点坐标
    # 计算起始点与结束点的距离
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # 执行按压手机屏幕的命令，每个像素点1.35毫秒
    os.system('adb shell input swipe 550 1550 550 1550 {}'.format(int(distance * 1.35)))
    print('跳')


# 更新主窗体画面
def update():
    time.sleep(0.8)  # 休眠0.8秒
    print('更新')
    # 更新图片
    axes_image.set_array(get_screen_image())
    figure.canvas.draw()  # 重画


# 重选按钮的单击事件处理
def button_click(event):
    if len(coor) < 2 and ax != None:
        coor.clear()  # 清空选中坐标点
        ax.lines.clear()  # 清除选中绘制点
        figure.canvas.draw()  # 重画


def auto_click(event):
    # 通过线程启动自动模式
    th = threading.Thread(target=auto_mode)
    th.start()


import auto  # 自动跳文件
import random  # 随机数模块


# 自动模式
def auto_mode():
    global isAuto
    isAuto = True  # 标记开启自动模式
    print('请输入自动跳跃的次数？')
    print('然后按下Enter键！')
    info = input()
    for i in range(int(info)):
        # 获取截图
        auto.get_screenshot()
        # 生成图片对象
        img = PIL.Image.open('autojump.png')
        # 获取棋子，棋盘位置横向中心坐标
        piece_x, board_x = auto.find_piece_and_board(img)
        # 生成一个随机按压点
        press_point = (random.randint(*[815, 923]),
                       random.randint(*[1509, 1658]))
        # 进行跳
        auto.jump(piece_x, board_x, img, press_point)
        update()  # 更新画面
        time.sleep(2)  # 设置停留时间
        if (i + 1) == int(info):
            isAuto = False  # 标记关闭自动模式
            print('结束此次自动模式！')


if __name__ == "__main__":
    figure = plt.figure()  # 创建一个空白的图形对象
    axes_image = plt.imshow(get_screen_image(), animated=True)  # 将获取的图片显示在主窗体当中
    figure.canvas.mpl_connect('button_press_event', on_click)  # 设置主窗体单击事件
    reelect_button_position = plt.axes([0.79, 0.8, 0.1, 0.08])  # 重选按钮的位置大小
    m = numpy.array(PIL.Image.open('image/bt.png'))  # 按钮背景图片
    # 设置重选按钮背景图片
    reelect_button = Button(reelect_button_position, label='', image=m)
    reelect_button.on_clicked(button_click)  # 设置重选按钮的单击事件
    m1 = numpy.array(PIL.Image.open('image/bt1.png'))  # 自动按钮背景图片
    auto_button_position = plt.axes([0.79, 0.65, 0.1, 0.08])  # 自动跳按钮的位置大小
    auto_button = Button(auto_button_position, label='', image=m1)  # 设置自动跳按钮背景图片
    auto_button.on_clicked(auto_click)  # 设置自动按钮的单击事件
    plt.show()  # 显示主窗体
