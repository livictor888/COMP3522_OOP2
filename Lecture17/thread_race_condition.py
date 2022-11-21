"""
This example demonstrates a race condition that can occur with two threads
Code from: https://realpython.com/intro-to-python-threading/
"""

import logging
import time
import concurrent.futures


class FakeDatabase:

    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value  #0
        logging.info("Thread %s: pre-increment - local_copy %d self.value %d", name, local_copy, self.value)
        local_copy += 1 #local = 1
        logging.info("Thread %s: post-increment - local_copy %d self.value %d", name, local_copy, self.value)
        logging.info("Thread %s sleep", name)
        time.sleep(0) # t1 t2 sleeping
        #thread 1 wake up
        self.value = local_copy
        logging.info("Thread %s: assign to self.value - local_copy %d self.value %d", name, local_copy, self.value)
        logging.info("Thread %s: finishing update", name)

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    # create two threads, where both have equal access to the database
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)


if __name__ == '__main__':
    main()