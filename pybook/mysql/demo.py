import redis 
import time

#连接客户端
cli = redis.Redis(
    host = "127.0.0.1",
    port = 6379,
    password = "whf",
    db = 1
)

#实例化多播对象
pub = cli.pubsub()

#订阅频道
pub.subscribe("hello_world")
time.sleep(1)
print(pub.get_message())

#发布消息
cli.publish("hwllo_world","hi")
print(pub.get_message())
