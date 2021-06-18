# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:37:11 2021

@author: whfo
"""

import os
 
course_list = []  # 存储课程信息字典，课程信息用字典存，再用列表存储字典
 
# 菜单
def display_menu():
    print("=" * 15 + "学生管理系统"      + "=" * 15)
    print("-" * 15 + "功能菜单"         + "-" * 17)
    print(" " * 15 + "1.录入学生信息"    + " " * 15)
    print(" " * 15 + "2.删除学生信息"    + " " * 15)
    print(" " * 15 + "3.查询学生信息"    + " " * 15)
    print(" " * 15 + "4.修改学生信息"    + " " * 15)
    print(" " * 15 + "5.保存学生信息数据" + " " * 15)
    print(" " * 15 + "6.显示学生所有信息" + " " * 15)
    print(" " * 15 + "7.统计学生人数"    + " " * 15)
    print(" " * 15 + "8.排序"           + " " * 15)
    print(" " * 15 + "0.退出系统"       + " " * 15)
    print("-" * 40)
 
# 选择序号的获得
def get_choice():
    selected_key = input("请输入功能对应的数字：")
    return selected_key
  
# 检查课学生id是否重复或者有误
def check_id(new_id):
    flag = True
    while flag:
        if new_id.isdigit():
            for i in range(len(course_list)):
                if course_list[i]['id'] == new_id:
                    new_id = check_id(input("您输入的学生id重复，请重新输入："))
            flag = False
        else:
            new_id = input("您输入的学生id有误，请重新输入：")
    return new_id
 
# 添加课程信息
def add_course():
    print('-----------欢迎使用录入功能------------')
    new_info = {}
    new_id = check_id(input("请输入学号ID(如：1001)："))
    new_info['id'] = new_id
    new_name = input("请输入学生姓名：")
    new_info['name'] = new_name
    new_english = input("请输入英语成绩：")
    new_info['english_result'] = new_english
    new_python = input("请输入Python成绩：")
    new_info['python_result'] = new_python
    new_Java = input("请输入Java成绩：")
    new_info['java_result'] = new_Java
    course_list.append(new_info)
    add_again = input("是否继续录入（yes/no）")
    if add_again == "yes":
        add_course()
    #print(course_list)
    print("学生信息录入成功！")
    print('------------处理后的课程数据------------')
    print('学生ID',' ','姓名',' ','English成绩',' ','Python成绩',' ','Java成绩')
    for course in course_list:   
        print(course['id'],' '*8, course['name'],' '*5, course['english_result'], ' '*8,course['python_result'], ' '*5,course['java_result'])
 
# 打开课程信息数据
def find_all():
    print('-------------恭喜你，打开数据成功-------------')
    print('------------处理后的课程数据------------')
    print('学生ID',' ','姓名',' ','English成绩',' ','Python成绩',' ','Java成绩')
    for course in course_list:   
        print(course['id'],' '*8, course['name'],' '*5, course['english_result'], ' '*8,course['python_result'], ' '*5,course['java_result'])
 
# 删除课程信息
def del_course():
    del_id_is = input("请输入要删除的课程编号：")
    flag = False
    index = 0
    for i in range(len(course_list)):
        if course_list[i]['id'] == del_id_is:
            flag = True
            index = i
            break
    if flag:
        course_list.pop(index)
        print('-------------恭喜你，删除数据成功-------------')
        print('------------处理后的课程数据------------')
        print('学生ID',' ','姓名',' ','English成绩',' ','Python成绩',' ','Java成绩')
        for course in course_list:   
            print(course['id'],' '*8, course['name'],' '*5, course['english_result'], ' '*8,course['python_result'], ' '*5,course['java_result'])
         
# 查询单个课程信息
def find_course():
    find_id_is = input("请输入要查询的课程编号：")
    flag = False
    index = 0
    for i in range(len(course_list)):
        if course_list[i]['id'] == find_id_is:
            flag = True
            index = i
            break
    if flag:
        print('------------处理后的课程数据------------')
        print('学生ID',' ','姓名',' ','English成绩',' ','Python成绩',' ','Java成绩')
        print(course_list[index]['id'],' '*8, course_list[index]['name'],' '*5,course_list[index]['english_result'],' '*8, course_list[index]['python_result'], ' '*5,course_list[index]['java_result'])
    else:
        print('该学生未找到！')
 
# 保存课程信息
def save_cou():
    course= str(course_list)
    with open("course.txt", "w", encoding="utf-8") as f:
        f.write(course)
    
    print("保存成功！文件位置在"+os.getcwd())
    print('处理后的课程数据')
    print('学生ID',' ','姓名',' ','English成绩',' ','Python成绩',' ','Java成绩')
    for course in course_list:   
        print(course['id'],' '*8, course['name'],' '*5, course['english_result'], ' '*8,course['python_result'], ' '*5,course['java_result'])
 
# 恢复数据
def recover_data():
    global course_list
    try:
        with open("course.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content != '':
                course_list = eval(content)   
    except:
        f = open("course.txt", "w")
        f.write("[]")
 
def main():
    recover_data()
    exit_course = True
    while exit_course:
        display_menu()
        key = get_choice()
        if key == '1':
            add_course()
        elif key == '2':
            del_course()
        elif key == '3':
            find_course()
        elif key == '4':
            save_cou()
        elif key == '5':
            find_all()
        elif key == '0':
            exit_course=input('确定退出吗？（yes/no）:')
            if exit_course == "yes":
                exit()
            else:
                pass
        else:
            print("请输入正确的数值！")
 
if __name__ =="__main__":
    main()
