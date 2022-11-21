"""
This module depicts how to create a custom thread by inheriting from
the Thread class.
"""
import requests
import threading
import time
import logging


class SiteDownloader:
    """
    SiteDownloader is responsible for maintaining a session and
    downloading the site at the specified address.
    """
    def __init__(self, session):
        self.session = session

    def download_site(self, url):
        with self.session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


class SiteDownloadThread(threading.Thread):
    """
    This thread is responsible for creating a web session and
    downloading sites.
    """

    # keeps track of the next unique id
    id = 0

    @classmethod
    def increment_id(cls):
        """
        Increments the unique id and returns it. Should be used to provide
        each thread a unique id.
        :return:
        """
        cls.id += 1
        return cls.id

    def __init__(self, sites):
        """
         :param sites: a sequence type containing strings, the url's to
         download
         """
        super().__init__()
        self.sites = sites
        self.id = self.increment_id()

    def download_all_sites(self):
        """
        Start a web session and download the specified sites.
        """
        with requests.Session() as session:
            site_downloader = SiteDownloader(session)
            for url in self.sites:
                logging.info(f"Thread {self.id}: Downloading {url}")
                site_downloader.download_site(url)

    def run(self):
        """
        Executes the thread so that it can download the sites.
        """
        self.download_all_sites()

def main():
    """
    Defines a list of sites and sets up the threads to download them
    """
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ]
    logging.info("Main      : before creating threads")
    start_time = time.time()
    threads = [SiteDownloadThread(sites * 20) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    duration = time.time() - start_time
    print(f"Downloaded 160 sites in {duration} seconds")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
