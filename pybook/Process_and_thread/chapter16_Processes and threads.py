#!/usr/bin/env python
# coding: utf-8

# # 第十六章之线程与进程
#     进程（process）是计算机中一运行程序的实体，是程序（指令和数据）的真正运行实例

# In[8]:


# 使用multiprocessing模块创建进程
from multiprocessing import Process
#子进程
def whfo(interval):
    print("我是紫禁城")
#主程序
def main():
    print("主进程开始")
    p = Process(target=whfo,args=(1,))
    p.start()
    print("主进程结束")


# In[9]:




if __name__ == "__main__":
    main()


# ### 因为Idea自身的问题，不会输出子进程的内容，命令行python+文件名可运行

# In[ ]:




