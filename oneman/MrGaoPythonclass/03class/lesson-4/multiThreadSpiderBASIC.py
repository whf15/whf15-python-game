from threading import Thread


total_task = [1,2,3,4,5,6,7,8,9,10]

def task_distribution(total):
    a = total[0:int(len(total)/2)]
    b = total[int(len(total)/2):]
    # print(a,b ,sep='\n')
    return a, b
task1 , task2 = task_distribution(total_task)
# print(task1,task2)

def spider1(task):
    print(task)

def spider2(task):
    print(task)


t1 = Thread( target=spider1, args=(task1,) )
t2 = Thread( target=spider2, args=(task2,) )

t1.start()
t2.start()

t1.join()
t2.join()

print('任务完成')



