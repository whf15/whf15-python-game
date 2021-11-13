 
import time
class HeapNode(object):
    """
        数据堆的节点
    """
 
    def __init__(self, data):
        """ 数据堆节点初始化 """
        self.index = 0
        self.data = data
        self.use_times = 1
 
    def __str__(self):
        return self.data
 
    def __gt__(self, other):
        """ 大于运算符 """
        return self.use_times > other.use_times
 
    def __lt__(self, other):
        """ 小于运算符 """
        return self.use_times < other.use_times
 
    def destory(self):
        """ 数据释放 """
        self.data = None
        self.use_times = 1
 
 
class EasyHeap(object):
    """
        简单的堆结构, 不用内置的原因是内置的堆操作列表事件复杂度为O(n)
    """
 
    def __init__(self, opacity):
        """ 数据结构的初始化 """
        # 参数初始化
        self._opacity = opacity
        self._heap = [None for i in range(self._opacity)]
        self._size = 0
 
    def _get_parent(self, index):
        """ 获取父节点 """
        if index <= 0:
            return None
        parent_index = (index - 1) / 2
        return self._heap[parent_index]
 
    def _get_left_child(self, index):
        """ 获取左孩子 """
        if 2 * index + 1 < self._size:
            return self._heap[2 * index + 1]
        return None
 
    def _get_right_child(self, index):
        """ 获取右节点 """
        if 2 * index + 2 < self._size:
            return self._heap[2 * index + 2]
        return None
 
    def _heapfix_up(self, node):
        """ 节点上升 """
        if not node:
            return
        index = node.index
 
        # 节点上升
        parent_node = self._get_parent(index)
        if parent_node and node < parent_node:
            self._exchange_node(parent_node, node)
            self._heapfix_up(node)
 
    def _heapfix_down(self, node):
        """ 节点下降 """
        if not node:
            return
        index = node.index
 
        # 挑选父子节点中最小的节点
        min_child = node
        left_node = self._get_left_child(index)
        min_child = left_node if left_node and left_node < min_child else min_child
        right_node = self._get_right_child(index)
        min_child = right_node if right_node and right_node < min_child else min_child
        
        # 选择最小的节点进行下降
        if min_child is not node:
            self._exchange_node(min_child, node)
            self._heapfix_down(node)
 
    def _exchange_node(self, node1, node2):
        """ 交换两个节点 """
        node1.index, node2.index = node2.index, node1.index
        self._heap[node1.index] = node1
        self._heap[node2.index] = node2
 
    def heapfix(self, node):
        """ 调整节点位置 """
        self._heapfix_up(node)
        self._heapfix_down(node)
 
    def get_head(self):
        """ 获取头部节点 """
        if self._size <= 0:
            return None
        return self._heap[0]
 
    def heappop(self):
        """ 推出头部节点 """
        if self._size <= 0:
            return None
 
        # 交换头尾节点
        head_node = self._heap[0]
        tail_node = self._heap[self._size - 1]
        self._exchange_node(head_node, tail_node)
        self._size -= 1
 
        # 节点调整
        self.heapfix(self._heap[0])
 
        return head_node
 
    def heappush(self, node):
        """ 将节点加到到堆中 """
        node.index = self._size
        self._heap[self._size] = node
        self._size += 1
 
        # 节点调整
        self.heapfix(self._heap[self._size - 1])
 
    def get_size(self):
        """ 获取堆的尺寸 """
        return self._size
 
    def show_heap(self):
        """ 显示整个堆 """
        result = []
        for node in self._heap:
            node and result.append([node.data.get('_key'), node.use_times, node.index])
        print( '======', result)
 
    def destory(self):
        """ 缓存的清空 """
        for node in self._heap:
            node and node.destory()
 
 
class LFUCache(object):
    """
        最近最少使用的缓存策略类
    """
 
    def __init__(self, cache_time, opacity):
        """
            最近未使用策略缓存
        """
        # 缓存类的参数设置
        self._dity_time = cache_time
        self._opacity = opacity
 
        # 数据缓存类的内部变量
        self._data_map = {}    # {key: Node}
        self._heap = EasyHeap(self._opacity)  # 数据堆
 
    def push_data(self, key, data):
        """
            数据的存储
        """
        if not isinstance(data, dict):
            return
 
        # 数据进来的时候的时间戳
        data['_key'] = key
        data['_time_stamps'] = int(time.time())
 
        # 数据已经在字典中直接更新
        if key in self._data_map:
            if self._data_map[key]:
                self._data_map[key].data = data
                return
            else:
                self._data_map.pop(key, 0)
 
        # 将数据插入到最小堆中
        node = HeapNode(data)
        if self._heap.get_size() >= self._opacity:
            removed_node = self._heap.heappop()
            if removed_node and removed_node.data:
                self._data_map.pop(removed_node.data.get('_key'), 0)
        self._heap.heappush(node)
        self._data_map[key] = node
 
    def get_data(self, key):
        """
            数据的访问
        """
        # 检出数据的时间戳
        node = self._data_map.get(key)
        if not node or not node.data:
            return None
 
        time_stamp = node.data.get('_time_stamps', 0)
        if time.time() - time_stamp < self._dity_time:
            node.use_times += 1
            self._heap.heapfix(node)
            return node.data
        else:
            return None
 
    def destory(self):
        """
            缓存的清空
        """
        self._data_map.clear()
        self._heap.destory()
 