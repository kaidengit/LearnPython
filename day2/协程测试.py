import gevent
import time
from gevent import monkey
monkey.patch_all()

def kang():
    for i in range(5):
        print(i)
        time.sleep(5)

def dong(url):
    print(url)
    # time.sleep(2)

if __name__ == "__main__":
    for i in range(5):
        g1 = gevent.spawn(kang)
        print("kangdong")

    gevent.joinall([g1,])

    # for i in range(20):
    #     kang(i)
    #     dong(i)