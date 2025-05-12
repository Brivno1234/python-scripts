import time
import random


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


timer = ExecutionTime()
sample_list = []

for i in range (1,1000000):
        if i % 2 == 0:
            sample_list.append(random.randint(1,888888))
            
for i in range(10):
    print(11111)
            
print("finished in {}seconds.".format(timer.duration()))