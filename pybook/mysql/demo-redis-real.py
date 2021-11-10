import redis
import time

def publisher(channel):
    cli = redis.Redis(host = "127.0.0.1",port = 6379,password = "whf",db = 1)
    msg = ["C","Python","Java","Go"]
    for i in msg:
        cli.publish(channel, i)
    return 


# 死循环消费者
def customer(channel, sec=1):
    cli = redis.Redis(host = "127.0.0.1",port = 6379,password = "whf",db = 1)
    pub = cli.pubsub()
    pub.subscribe(channel)
    while True:
        msg = pub.get_message()
        if not msg:
            time.sleep(sec)
            continue
        print(msg)

# 阻塞消费者
# sleep太长，listen，没跑完就不动
def customer_new(channel):
    cli = redis.Redis(host = "127.0.0.1",port = 6379,password = "whf",db = 1)
    pub = cli.pubsub()
    pub.subscribe(channel)
    for msg in pub.listen():
        print(msg)