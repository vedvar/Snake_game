# Group #: G36
# Student names: Ved Varshney, Shawn Nagra
 
import threading
import queue
import time, random

def consumerWorker (queue):
    """target worker for a consumer thread"""

    for _ in range(itemsProduced):  # loop runs as the number of selected produced items
        item = queue.get()          # item is consumed from the buffer queue
        time.sleep(round(random.uniform(minDelay, maxDelay), 2)) # random delay from 100ms to 300ms
        print(f"DEBUG: {item} consumed") 
  
def producerWorker(queue):
    """target worker for a producer thread"""

    for i in range(itemsProduced):    # loop runs as the number of selected produced items
        item = random.randint( minItemNumber,  maxItemNumber)  # an item is produced
        queue.put(item)               # item is put into the buffer queue
        time.sleep(round(random.uniform(minDelay, maxDelay), 2)) # random delauy from 100-300ms
        print(f"DEBUG: {item} produced")

if __name__ == "__main__":
    buffer = queue.Queue()
    
    itemsProduced = 4 # a small number for testing purposes

    minItemNumber = 1  # minimum value produced item can take
    maxItemNumber = 99 # maximum value produced item can take

    minDelay = .1 # minimum delay after item consumed or produced is 100ms
    maxDelay = .3 # mmaximum delay after item consumed or produced is 300ms

    consumerThreadsNum = 5 # number of consumer thresad
    producerThreadsNum = 4 # numer of producer threads

    threadList = [] # Created empty list to use in for loops

    for indx in range(consumerThreadsNum): # loop appends all consumer threads to the thread list
        threadList.append(threading.Thread(target = consumerWorker, args = (buffer,)))

    for indx in range(producerThreadsNum): # loop appends all producer threads to the thread list
        threadList.append(threading.Thread(target = producerWorker, args = (buffer,)))

    for threads in threadList: # All threads are started
        threads.start()

    for threads in threadList: # All threads are joined
        threads.join()
    