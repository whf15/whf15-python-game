from bs4 import BeautifulSoup


with open('index_1.html', 'r', encoding='utf-8') as r:
    content = r.read()

soup = BeautifulSoup(content,'lxml')

##指名道姓
res_1 = soup.find_all(name='a') #.attrs['href'] .text
# print(res_1)
# for x in res_1:
#     print(x.text, '----' ,x.attrs['href'])

#叠加提取
res_2 = soup.find_all(name='div', attrs={'class':'others'})# #可以使用这种方式 (name='div',id ='_others')
# print(res_2)
# final_2 = res_2[0].find_all(name='a')
# print(final_2)
#
# for x in final_2:
#     print(x.text,x.attrs['href'])

#路径规则法 直接路径
res_3 = soup.select('#_others > ul > li > a') #  .定位类 #定位id  也可以直接tagName标签名字
# print(res_3)

#路径规则法 跳级路径
res_4 = soup.select('#_others > ul a') #  .定位类 #定位id  也可以直接tagName标签名字
# print(res_4)

#路径规则法 锁定属性的标签可以出现在路径的任何位置
res_5 = soup.select('body .others > ul a') #  .定位类 #定位id  也可以直接tagName标签名字
# print(res_5)

#路径规则法 标签路径
res_6 = soup.select('html div a') #  .定位类 #定位id  也可以直接tagName标签名字
print(res_6)













# for  link in res_2:
#     print(link.attrs['href'])
#     # requests.get().content
#     # with open('na','wb') as w:
#     #     w.write(res )

