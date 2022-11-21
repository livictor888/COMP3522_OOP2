"""
This example demonstrates a race condition fixed with locks and context managers
Code from: https://realpython.com/intro-to-python-threading/
"""

import logging
import time
import concurrent.futures
import threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s about to lock", name)
        # self._lock.acquire() #manually get lock

        # use lock context manager to automatically lock and release
        with self._lock:
            logging.info("Thread %s has lock", name)
            local_copy = self.value
            logging.info("Thread %s: pre-increment - local_copy %d self.value %d", name, local_copy, self.value)
            local_copy += 1
            logging.info("Thread %s: post-increment - local_copy %d self.value %d", name, local_copy, self.value)
            logging.info("Thread %s sleep", name)
            time.sleep(2)
            self.value = local_copy
            logging.info("Thread %s: assign to self.value - local_copy %d self.value %d", name, local_copy, self.value)
            logging.info("Thread %s about to release lock", name)
        # self._lock.release() # manually release lock
        logging.info("Thread %s after release", name)
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