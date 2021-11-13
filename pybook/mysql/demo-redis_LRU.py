from  collections import deque
 
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
 
class LRUCache(object):
    def __init__(self,capacity):
        """
        LRU缓存置换算法
        :param capacity:
        """
        self.capacity = capacity
        self.size = 0
        self.map = {} # 哈希表找元素位置
        self.list = deque(maxlen=capacity) # 双端队列移除、插入头部
 
    def get(self,key):
        """获取元素"""
        # 元素不存在的逻辑
        if key not in self.map:
            return None
        # 元素存在逻辑
        node = self.map.get(key)
        self.list.remove(node) # 移除
        self.list.appendleft(node) # 插入到头部
 
        return node.val
 
    def put(self,key,value):
        """添加元素"""
        ## 元素存在逻辑,update
        if key in self.map:
            node = Node(key,value)
            node.val = value
            self.map[key] = node
            # 移除节点，插入到头部
            self.list.remove(node)
            self.list.appendleft(node)
            return
 
        ##  元素不存在逻辑
        # 1. 链表已满
        if self.size >= self.capacity:
            # 删除热度最低的元素,更新哈希表
            oldnode = self.list.pop()
            self.map.pop(oldnode.key)
            self.size -=1
 
        # 将该节点插到头部，更新哈希表
        node = Node(key,value)
        self.list.appendleft(node)
        self.map[key] = node
        self.size +=1
 
    def printList(self):
        """打印当前链表"""
        listTemp = self.list.copy() # 当前列表的复制
        while len(listTemp) > 0:
            print(listTemp.popleft().val)
 
if __name__ == '__main__':
    lruCache = LRUCache(3)
    lruCache.put(1,1)
    lruCache.printList()
    lruCache.put(2,2)
    lruCache.printList()
    print(lruCache.get(2))
    lruCache.put(3,3)
    lruCache.printList()
 