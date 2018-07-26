from queue import Queue
from threading import *
import requests
from requests import request

class my_Thread(Thread):

    def __init__(self,name,queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):

        while True:

            if queue.empty():
                print("Queue Status : Empty")

            x = str(queue.get())

            url = "http://127.0.0.1:8000/api/colleges/" + x + "/"

            print("name = ", self.name,x)

            data = request('get', url).json()

            print(data)

if __name__=="__main__":

    queue = Queue()

    for i in range(100):
        t = my_Thread(str(i),queue)
        t.start()

    for i in range(221,232):
        queue.put(i)

    queue.join()