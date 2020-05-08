import threading
import time
lis = []
lis2 = []
n = 10

class myThread (threading.Thread):
   def __init__(self, threadID, name, data):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.data = data

   def run(self):
      lis.append(self.data)

multi_time = []
for x in range(0, n):
    t1 = time.perf_counter()
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    thread3 = myThread(3, "Thread-3", 3)
    thread4 = myThread(4, "Thread-4", 4)
    thread5 = myThread(5, "Thread-5", 5)
    thread6 = myThread(6, "Thread-6", 6)


    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()

    multi_time.append(time.perf_counter() - t1)

print("Multithreaded:")
print(multi_time)

single_time = []
for x in range(0, n):
    l1 = time.perf_counter()
    
    lis2.append(1)
    lis2.append(2)
    lis2.append(3)
    lis2.append(4)
    lis2.append(5)
    lis2.append(6)

    single_time.append(time.perf_counter() - l1)

print("Single threaded:")
print(single_time)