"""
This example demonstrates a complicated way of multi threading
Code from: https://realpython.com/intro-to-python-threading/
"""

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(4)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()

    #  create multiple threads and begin them
    for index in range(8):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    #threads are going to start running because of the start()
    #  join each thread to wait for them to complete before reaching the end of the program
    print("Main 1")

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    print("Main 2")