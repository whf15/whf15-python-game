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

# In[1]:


# -*- coding：utf-8 -*-
from multiprocessing import Process
import time
import os


# In[3]:


#两个子进程将会调用的两个方法
def child_1(interval):
    print("子进程(%s)开始执行，父进程为（%s）"%(os.getpid(),os.getppid))
    t_start = time.time() #计时开始
    time.sleep(interval)  #程序将会被挂起interval秒
    t_end = time.time()   #计时结束
    print("子进程（%s）执行时间为'%0.2f'秒"%(os.getpid(),t_end - t_start))
    
def child_2(interval):
    print("子进程(%s)开始执行，父进程为（%s）"%(os.getpid(),os.getppid))
    t_start = time.time()    #计时开始
    time.sleep(interval)     #程序将会被挂起interval秒
    t_end = time.time()      #计时结束
    print("子进程（%s）执行时间为'%0.2f'秒"%(os.getpid(),t_end - t_start))


# In[5]:


if __name__ == '__main__':
    print("------父进程开始执行------")
    print("父进程PID： %s"% os.getpid())
    p1 = Process(target=child_1,args=(1,))
    p2 = Process(target=child_2,args=(2,))
    p1.start()
    p2.start()
    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print("p1.is_alive = %s"%p1.is_alive())
    print("p2.is_alive = %s"%p2.is_alive())
    #输出p1和p2进程的别名和PID
    print("p1.name = %s" %p1.name)
    print("p1.pid = %s" %p1.pid)
    print("p2.name = %s" %p2.name)
    print("p2.pid = %s" %p2.pid)
    print("-----等待子进程------")
    p1.join()
    p2.join()
    print("-----父进程执行结束-----")


# ### 第一次实例化Process类时，会为name属性默认赋值为“Process-1”,第二次则默认为“Process-2”,但是由于在实例化进程p2时，设置了name属性为“mrsoft”

# In[ ]:




