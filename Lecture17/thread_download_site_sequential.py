"""
This example demnonstrates  an I/O bound problem of downloading a site
which takes up the bulk of the processing time.
Code from: https://realpython.com/python-concurrency/#what-is-parallelism
"""

import requests
import time
import threading

def download_site(url, session):
    """
    Downlaods the content from the given url.
    :param url: a string, site to download
    :param session: Request.Session object
    :return: None
    """
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url} by thread "
              f"{threading.current_thread().name}")


def download_all_sites(sites):
    """
    Downloads the content for each and every site in the given iterable.
    :param sites: an iterable, a sequence of urls
    :return: None
    """
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


def main():
    """
    Creates a request to download 160 sites.
    """
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice"
            ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


if __name__ == '__main__':
    main()