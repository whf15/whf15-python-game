#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr.Stick Man Races for the Exit")#把窗口标题设置为”“
        self.tk.resizable(0, 0)#让窗口的大小固定（不能改变大小）
        self.tk.wm_attributes("-topmost", 1)#把窗口移到所有其他窗口之前
        self.canvas = Canvas(self.tk, width=500, height=500,                             highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        
        self.bg = PhotoImage(file="background1.gif")#装载PhotoImage对象（背景图片）
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h,                         image = self.bg, anchor='nw')
        self.sprites = []
        self.running = True
    
    #做出游戏的动画
    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites: #遍历所有精灵列表
                    sprite.move()
            self.tk.update_idletasks() #让tk对象重新绘屏幕并休息百分之一秒
            self.tk.update()
            time.sleep(0.01)
            

        


# In[10]:


#创建一个用来指定物体在游戏屏幕上位置的类 ...左上(x1，y1）右下（x2,y2）
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    '''
       if   co1.x1 > co2.x1 and co1.x1 < co2.x2:
            return True
        
        elif co1.x2 > co2.x1 and co1.x2 < co2.x2:
            return True
        elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
            return True
        elif co2.x2 > co1.x1 and co2.x2 < co1.x2:   #书本上写了co1.x1
            return True
        else:
            return False #这两个坐标对象在水平位置上没有交叉
       
    '''
def within_x(co1, co2):
        #判断第一个坐标对象的最左边是否在第二个坐标对象的最左边和最右边之间
       
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2)                 or (co1.x2 > co2.x1 and co1.x2 < co2.x2)                 or (co2.x1 > co1.x1 and co2.x1 < co1.x2)                 or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False
    
def within_y(co1, co2):
        #判断第一个坐标对象y1的最左边是否在第二个坐标对象的最左边和最右边之间
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2)                 or (co1.y2 > co2.y1 and co1.y2 < co2.y2)                 or (co2.y1 > co1.y1 and co2.y1 < co1.y2)                 or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
        return True
    else:
        return False
        
    #判断是否相遇
def collided_left(co1, co2):
        #左侧相遇
    if within_y(co1, co2):
        if co1.x1 <=co2.x2 and co1.x1 >=co2.x1:
            return True
    return False
    
def collided_right(co1, co2):
        #右侧相遇
    if within_y(co1, co2):
        if co1.x2 <=co2.x2 and co1.x2 >=co2.x1:
            return True
    return False
    
def collided_top(co1, co2):
        #顶部侧相遇
    if within_x(co1, co2):
        if co1.y1 <=co2.y2 and co1.y1 >=co2.y1:
            return True
    return False
    
    # 跳下来   
def collided_bottom(y, co1, co2):
        #底部相遇
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False


# In[11]:


#创建精灵类
class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
        
    def move(self):
        pass
    def coords(self):
        return self.coordinates

#添加平台类
class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y,                 image=self.photo_image, anchor='nw')#对齐方式，左对齐”w”，右对齐”e”，顶对齐”n”，底对齐”s”
        self.coordinates = Coords(x, y, x + width, y + height)


# In[12]:


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        #装载火柴人
        self.images_left = [
            PhotoImage(file="figure-L1.gif"),
            PhotoImage(file="figure-L2.gif"),
            PhotoImage(file="figure-L3.gif")
        ]
        self.images_right = [
            PhotoImage(file="figure-R1.gif"),
            PhotoImage(file="figure-R2.gif"),
            PhotoImage(file="figure-R3.gif")
        ]
        self.image = game.canvas.create_image(200, 470,                 image=self.images_left[0], anchor='nw')
        
        self.x = -2                      #火柴人运动时的水平位置（x1, x2）
        self.y = 0                       #火柴人运动时的水平位置（y1, y2）
        #对x坐标减去2，对于y坐标没有变量，这样火柴人就会想左跑
        self.current_image = 0           #保存当前显示在屏幕上的图形的索引位置
        self.current_image_add = 1       #保存的索引位置来得到下一个索引位置
        self.jump_count = 0              #计数器，在火柴人跳跃时用到
        self.last_time = time.time()     #上一次移动火柴人的时间
        self.coordinates = Coords()      #设置为Coords类的对象
        
        #与键盘按键绑定
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)
        
        #让火柴人向左转和向右转,事件对象event object ，evt
        #数字大小时火柴人移动的速度
    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2
        
    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2
        
    def jump(self, evt):
        if self.y == 0:  #说明白此时火柴人没有跳跃
            self.y = -4
            self.jump_count = 0 #不会无限跳
        
        #创建动画函数
    def animate(self):
        if self.x != 0 and self.y == 0: 
            #判断是否在移动或者跳跃
            if time.time() - self.last_time > 0.1: #为下次改变图形做准备
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        
        if self.x < 0:
            #火柴人向左
            if self.y != 0: #有没有在跳跃（等于0说明没有跳），换成步子大的图片
                self.game.canvas.itemconfig(self.image,                                 image = self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image,                                     image = self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image,                                     image = self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image,                                     image = self.images_right[self.current_image])
        
    def coords(self):
        xy = self.game.canvas.coords(self.image) #返回当前图形 的x, y位置
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27 #创建的火柴人图形为27*30
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates
                 
        #让火柴人移动
    def move(self):
        self.animate()
        if self.y < 0: #火柴人在跳跃中，负值说明向上移动（画布的顶部为0，底部为500）
            self.jump_count += 1
            if self.jump_count > 20: #不能跳太高
                 self.y = 4
        if self.y > 0:
            self.jump_count -= 1
            
        co = self.coords()
            #布尔值用来判断是否撞了东西或者是否在下落
        left = True
        right = True
        top = True
        bottom = True
        falling = True
            
            #火柴人正在下落时，y大于0，需判断他的y2是否大于game对象的变量canvans_height
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom =False
        elif self.y < 0 and co.y1 <=0:
            self.y = 0
            top = False
            
            #火柴人是否撞到了画布的两侧
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right =False
                
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left =False
            
            #与其他精灵相撞P231
        for sprite in self.game.sprites:
            if sprite ==self: #如果这个精灵使我自己火柴人不是墙壁，
                continue
            sprite_co = sprite.coords()
                
                #没有撞到顶部，正在跳跃，顶部撞到其他精灵，此时继续下落
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False
                
                #bottom是否设置好，火柴人是否下落，他的脚是否碰到其他
            if bottom and self.y > 0 and collided_bottom(self.y ,                             co, sprite_co):
                self.y = sprite_co.y1 - co.y2   #P232
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False
                    
                #bottom已设为T,火柴人是否应该下落，没有下落，底部没有碰到画布，头部撞到平台的顶部
            if bottom and falling and self.y == 0                         and co.y2 < self.game.canvas_height                         and collided_bottom(1, co, sprite_co):
                falling = False
                
                #向左还是向右
            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.game.running = False
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                right = False
                if sprite.endgame:
                    self.game.running = False
            
        if falling and bottom and self.y == 0                     and co.y2 < self.game.canvas_height:
            self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)
                
        
                          
            


# In[13]:


class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y,                 image = self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, +(width / 2), y + height)
        self.endgame = True


# In[14]:


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="platform3.gif"),0, 480, 100 ,10)
platform2 = PlatformSprite(g, PhotoImage(file="platform3.gif"),150, 440, 100 ,10)
platform3 = PlatformSprite(g, PhotoImage(file="platform3.gif"),300, 400, 100 ,10)
platform4 = PlatformSprite(g, PhotoImage(file="platform3.gif"),300, 160, 100 ,10)
platform5 = PlatformSprite(g, PhotoImage(file="platform2.gif"),175, 350, 66 ,10)
platform6 = PlatformSprite(g, PhotoImage(file="platform2.gif"),50, 300, 66 ,10)
platform7 = PlatformSprite(g, PhotoImage(file="platform2.gif"),170, 120, 66 ,10)
platform8 = PlatformSprite(g, PhotoImage(file="platform2.gif"),45, 60, 66 ,10)
platform9 = PlatformSprite(g, PhotoImage(file="platform1.gif"),170, 250, 32 ,10)
platform10 = PlatformSprite(g, PhotoImage(file="platform1.gif"),230, 200, 32 ,10)

g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)

door = DoorSprite(g, PhotoImage(file="door1.gif"),45 ,30, 40, 35)
g.sprites.append(door)

sf = StickFigureSprite(g)
g.sprites.append(sf)
g.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




