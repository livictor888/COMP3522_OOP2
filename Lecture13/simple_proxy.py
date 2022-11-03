"""
This module demonstrates a simple proxy example
"""
import abc


class ServiceInterface(abc.ABC):
    """
    An interface for the Service. Both proxy and service must fully implement all
    abstract methods
    """

    @abc.abstractmethod
    def operation(self):
        pass


class Proxy(ServiceInterface):
    """
    Proxy contains a reference to the actual service. Any calls made to the proxy
    are directed to the actual service. Some pre and post code may be done before
    and after the call to service
    """

    def __init__(self, service):
        self.real_service = service

    def operation(self):
        print("doing proxy operation before")
        self.real_service.operation()
        print("doing proxy operation after")


class Service(ServiceInterface):
    """
    The actual service where the work is done
    """

    def operation(self):
        print("doing service operation code")


# instantiate real and proxy services, pass instance of real service to proxy
real_youtube = Service()
proxy_youtube = Proxy(real_youtube)

# client only interacts with proxy_youtube
proxy_youtube.operation()
