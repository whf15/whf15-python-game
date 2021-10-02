from lxml import etree

with open('index_1.html', 'r', encoding='utf-8') as r:
    content = r.read()

tree = etree.HTML(content)

#案例一
res_1 = tree.xpath('/html/head/title')
# print(res_1)
# print(res_1[0].text)

#案例二 基于属性定位
res_2 = tree.xpath('/html/body/div[@class="others"]')
# print(res_2)

#案例三 获取元素后数字定位
res_3 = tree.xpath('/html/body/div[@class="others"]/ul/li')  #多个标签出现可以使用[1开始]
# print(res_3)

#那么如何继续按照这个逻辑向下找呢？ 因为li里还有a a  是我们的终极目标
# for li in res_3:
#     a_res = li.xpath('./a/@href') #注意这里的. 这个代表当前的li标签
#     print(a_res)

#案例四 跳级式定位 即从某个标签开始向下看 所有层级满足条件的
res_5 = tree.xpath('/html//div[@class="others"]//a/@href')  #多个标签出现可以使用[1开始]
# print(res_5)
# for x in res_5:
#     print(x.text)

#案例五
res_6 = tree.xpath('/html//div[@class="others"]//li[2]/a')  #多个标签出现可以使用[1开始]
print(res_6[0].text)
# for x in res_5:
#     print(x.text)






#
# res2 = tree.xpath('/html//div') #多连 多个层级 bs4的空格
# print(res2)
#
# res3 = tree.xpath('//div') #开头//多连 任意位置
# print(res3)
#
# res4 = tree.xpath('//div[@class="general"]') #属性定位 @属性 = 值
# print(res4)
#
# res5 = tree.xpath('//div[@class="general"]/p[1]') #属性定位 @属性 = 值 /延伸所有标签 注意 从1开始不是0开始 索引定位
# print(res5[0].text) #第一种获取text方式
#
# res6 = tree.xpath('//div[@class="general"]/p[2]/text()') #属性定位 @属性 = 值 /延伸所有标签 注意 从1开始不是0开始 索引定位
# print(res6)
#
#
# res7 = tree.xpath('//div[@class="others"]/ul/li[5]//text()') #
# print(res7)
#
#
# #取属性
# res8 = tree.xpath('//img/@src') #@  是属性
# print(res8)
#
#
# res9= tree.xpath('//a/@href') #@  是属性
# print(res9)
#


# 当前解析的源码 ./ <li><a></a><li/> li.xpath('./a/text()')