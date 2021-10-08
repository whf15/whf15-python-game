infomation = [
    ['mike4', 40, 'wanmen'],
    ['mike2', 20, 'wanmen'],
    ['mike1', "30", ''],
]

# with open('1.txt', 'a', encoding='utf-8') as add:
#     # add.write('123123'+'\n')
#     for x in infomation:
#         add.write(str(x) +'\n')

with open('1.txt','r',encoding='utf-8') as r:
    # print(r.readlines())
    for i in r.readlines():
        new = i
        for x in new:
            print(x)
        # print(i)
        # print(type(eval(i)))
        # print(type(i))

