"""
This example demonstrates a simplified way of multi threading
Code from: https://realpython.com/intro-to-python-threading/
"""

import concurrent.futures
import time
import logging

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    """
    Sets up a ThreadPoolExecutor context manager using the with statement to manage 
    creation and destruction of the thread pool
    
    Tells the context manager how many worker threads it wants in the pool
    Use the map function to map 3 thread_function to the executor
    
    This will automatically start and join the threads 
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as executor:
        executor.map(thread_function, range(14))