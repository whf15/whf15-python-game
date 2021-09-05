#!/usr/bin/env python
# coding: utf-8

# # 第十六章之线程与进程
#     进程（process）是计算机中一运行程序的实体，是程序（指令和数据）的真正运行实例

# # 使用multiprocessing模块创建进程
# from multiprocessing import Process
# #子进程
# def whfo(interval):
#     print("我是紫禁城")
# #主程序
# def main():
#     print("主进程开始")
#     p = Process(target=whfo,args=(1,))
#     p.start()
#     print("主进程结束")

# 
# 
# if __name__ == "__main__":
#     main()

# ### 上述代码先实例化Process类，然后使用p.start()方法启动子进程，开始执行whfo()函数
# ### 因为Idea自身的问题，不会输出子进程的内容，命令行python+文件名可运行

# # -*- coding：utf-8 -*-
# from multiprocessing import Process
# import time
# import os

# #两个子进程将会调用的两个方法
# def child_1(interval):
#     print("子进程(%s)开始执行，父进程为（%s）"%(os.getpid(),os.getppid))
#     t_start = time.time() #计时开始
#     time.sleep(interval)  #程序将会被挂起interval秒
#     t_end = time.time()   #计时结束
#     print("子进程（%s）执行时间为'%0.2f'秒"%(os.getpid(),t_end - t_start))
#     
# def child_2(interval):
#     print("子进程(%s)开始执行，父进程为（%s）"%(os.getpid(),os.getppid))
#     t_start = time.time()    #计时开始
#     time.sleep(interval)     #程序将会被挂起interval秒
#     t_end = time.time()      #计时结束
#     print("子进程（%s）执行时间为'%0.2f'秒"%(os.getpid(),t_end - t_start))
# 
# if __name__ == '__main__':
#     print("------父进程开始执行------")
#     print("父进程PID： %s"% os.getpid())
#     p1 = Process(target=child_1,args=(1,))
#     p2 = Process(target=child_2,args=(2,))
#     p1.start()
#     p2.start()
#     # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
#     print("p1.is_alive = %s"%p1.is_alive())
#     print("p2.is_alive = %s"%p2.is_alive())
#     #输出p1和p2进程的别名和PID
#     print("p1.name = %s" %p1.name)
#     print("p1.pid = %s" %p1.pid)
#     print("p2.name = %s" %p2.name)
#     print("p2.pid = %s" %p2.pid)
#     print("-----等待子进程------")
#     p1.join()
#     p2.join()
#     print("-----父进程执行结束-----")

# In[5]:





# ### 第一次实例化Process类时，会为name属性默认赋值为“Process-1”,第二次则默认为“Process-2”,但是由于在实例化进程p2时，设置了name属性为“mrsoft”

# ## 使用Process子类创建进程

# # -*- coding：utf-8 -*-
# from multiprocessing import Process
# import time
# import os

# #j继承Precess类
# class SubProcess(Process):
#     #由于Process类本身也有__init__初始化方法，这个子类相当于重写了父类这个方法
#     def __init__(self,interval,name=""):
#         Process.__init__(self)    # 调用Process符类的胡世华方法
#         self.interval = interval # 接受参数interval
#         if name:                 # 判断传递的参数name是否存在
#             self.name = name     # 如果传递参数name，则为子进程创建name属性，否则使用默认属性
#     #重写了Process类的run（）方法
#     def run(self):
#         print("子进程(%s)开始执行，父进程为（%s）"%(os.getpid(),os.getppid))
#         t_start = time.time()    #计时开始
#         time.sleep(interval)     #程序将会被挂起interval秒
#         t_end = time.time()      #计时结束
#         print("子进程（%s）执行时间为'%0.2f'秒"%(os.getpid(),t_end - t_start))
# if __name__ == '__main__':
#     print("------父进程开始执行------")
#     print("父进程PID： %s"% os.getpid())
#     p1 = SubProcess(interval=1)
#     p2 = SubProcess(interval=2,name="mrsoft")
#     # 对一个不包含target属性的Process类执行start()方法，就会运行这个类的run()方法
#     # 会执行p1.run()
#     p1.start()
#     p2.start()
#     # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
#     print("p1.is_alive = %s"%p1.is_alive())
#     print("p2.is_alive = %s"%p2.is_alive())
#     #输出p1和p2进程的别名和PID
#     print("p1.name = %s" %p1.name)
#     print("p1.pid = %s" %p1.pid)
#     print("p2.name = %s" %p2.name)
#     print("p2.pid = %s" %p2.pid)
#     print("-----等待子进程------")
#     p1.join()
#     p2.join()
#     print("-----父进程执行结束-----")

# In[ ]:





# ## 使用进程池Pool创建进程
#     如果要创建几十个或者上百个进程，则需要实例化过呢个多个Process类，使用multiprocessing模块提供的pool类

# In[1]:


# -*- coding=utf-8 -*-
from multiprocessing import Pool
import os, time


# In[2]:


def task(name):
    print('子进程（%s）执行task %s ....'%(os.getpid() , name))
    time.sleep(1)


# In[ ]:


if __name__=='__main__':
    print('父进程（%s）.' % os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))
    print('等待所有子进程结束...')
    p.close()
    p.join()
    print('所有子进程结束')


# In[ ]:




