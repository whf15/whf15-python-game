import redis
import sys
from utils.logger import logger
import time

def process_message(id, fields):
    logger.info(f"consumer info: [{consumer_name}] {id} = {fields}")


def stream_message():
    """stream and groups info"""
    logger.info(f'stream info: {r.xinfo_stream(stream_name)}')
    logger.info(f'groups info: {r.xinfo_groups(stream_name)}')

# 这里我把写成从外部命令获取一个消费者名字，方便启动多个消费者
# 所以命令要加上一个消费者参数，如: python stream.py consumer-0
ARGV = sys.argv[1:]
if len(ARGV) == 0:
    logger.error("Please specify a consumer name")
    sys.exit()

consumer_name = ARGV[0]
stream_name = "convert"
group_name = "convert-group"

pool = redis.ConnectionPool(
    host='localhost', port=6379, decode_responses=True)  # decode_responses=True 这样写存的数据是字符串格式
r = redis.StrictRedis(connection_pool=pool)

def mock_redis():
    """mock data"""
    if r.exists(stream_name):
        r.delete(stream_name)
    r1 = r.xadd(stream_name, {'name': 'jack'})
    r2 = r.xadd(stream_name, {'name': 'Tom'})
    r3 = r.xadd(stream_name, {'name': 'Will'})

    # 创建 stream group
    r.xgroup_create(stream_name, group_name, id=0)  # 0 从开始消费, $ 从尾部消费
    logger.info(f'stream info: {r.xinfo_stream(stream_name)}')

mock_redis()  # 这里记得是在模拟数据哦，自取

lastid = '0-0'  # 一开始从 0 读取历史记录, 以防止服务崩溃遗漏

logger.info(f"Consumer {consumer_name} starting...")
stream_message()
check_backlog = True
while True:
    if check_backlog:
        consumer_id = lastid
    else:
        consumer_id = '>'

    # block 0 时阻塞等待, 其他数值表示读取超时时间
    items = r.xreadgroup(group_name, consumer_name, {stream_name: consumer_id}, block=0, count=1)  

    if not items:  # 如果 block 不是 0或者为空, 会需要这段
        logger.info("Timeout!")
        stream_message()
        time.sleep(3)  # 空值等待 3s
        continue
    elif len(items[0][1]) == 0:
        check_backlog = False

    for id, fields in items[0][1]:
        process_message(id, fields)
        try:
            # 0 / 0  # 这个模拟处理崩溃
            # 这里是你要做的事情，封一个函数这里调用即可
            pass
        except Exception as e:
            logger.exception(e)
            continue
        finally:
            lastid = id  # 无论是出错还是正常执行完毕,都要去读取下一个,否则可能会无限循环读取处理报错的数据
        r.xack(stream_name, group_name, id)
    time.sleep(2)  # 间隔时长，自取

class SubRedis(object):
    def __init__(self):
        if not hasattr(SubRedis, 'pool'):
            SubRedis.getRedisCoon()  # 创建redis连接池
        self._coon = redis.Redis(connection_pool=SubRedis.pool)

    @staticmethod
    def getRedisCoon():
    SubRedis.pool = redis.ConnectionPool(host=redisInfo['SubRedisAddress'],password=redisInfo['SubRedisPassword'],port=redisInfo['SubRedisPort'],db=redisInfo['db'])

    #返回一个channel的具体信息: 订阅者数量,最后送达的msg的ID...
    def channel_info(self,channel):
        return self._coon.xinfo_stream(channel)

    #返回一个channel的具体订阅群组的信息（这里是返回订阅者，因为每一个群组只有一个消费者）
    def channel_consumers_info(self,channel):
        InfoList = self._coon.xinfo_groups(channel)
        for GroupDict in InfoList:
            GroupDict.pop("consumers")
        return InfoList

    #创建消费者
    def create_consumer_group(self,name,channel):
        ret = self._coon.xgroup_create(channel,name,id="$")
        if ret == True:
            print self.channel_consumers_info(channel)
        else:
            logging.error("create consumer %s fill,ret %s" %(name,ret))

    #往某一个channel发送消息
    def publish(self,channel,msg):
        msgid = self._coon.xadd(channel,msg)
        return msgid

    #一个已经存在的消费者订阅一个频道
    def subscribe(self,name,channel):
        channel_consumers_infolist = self.channel_consumers_info(channel)
        for consumer_dict in channel_consumers_infolist:
            if name in consumer_dict.values():
                logging.warning("consumer %s has already subscribed %s" %(name, channel))
                return
        self.create_consumer_group(name,channel)
        print "%s subscribe %s success,channel %s info:"%(name,channel,channel),self.channel_consumers_info(channel)
        return
