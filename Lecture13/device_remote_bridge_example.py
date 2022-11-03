"""
Demonstrates the Bridge Pattern. An entity with two independent
dimensions - a Remote (Abstraction, Control layer) and a
Device (Implementation) is decoupled into two separate hierarchies.
These are then "bridged" using composition. Refer to the bridge_uml.png
diagram while reading this code.
"""
import abc


class IDevice(abc.ABC):
    """
    An interface for the Device dimension. This is the implementation
    layer that actually does all the work.
    """

    def __init__(self):
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    @abc.abstractmethod
    def enable(self):
        pass

    @abc.abstractmethod
    def disable(self):
        pass

    @abc.abstractmethod
    def get_volume(self):
        pass

    @abc.abstractmethod
    def set_volume(self, percent):
        pass

    @abc.abstractmethod
    def get_channel(self):
        pass

    @abc.abstractmethod
    def set_channel(self):
        pass


class Radio(IDevice):
    """
    A Radio Device. One of the possible devices (implementation) that
    can be matched to a remote.
    """
    def __init__(self):
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def __str__(self):
        return f"Radio: {self.enabled} , {self.volume}, {self.channel}"



class TV(IDevice):
    """
    A TV Device. One of the possible devices (implementation) that
    can be matched to a remote.
    """
    def __init__(self):
        self.volume = 50
        self.channel = "a_channel"
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def __str__(self):
        return f"TV: {self.enabled} , {self.volume}, {self.channel}"


class Remote:
    """
    The Remote class represents the Abstraction dimension (this doesn't
    have to be an ABC and may have child classes, not necessarily). In
    this case the Remote class sort of acts like a wrapper but this
    isn't mandatory. Depending on the needs of the system the
    implementation (e.g. IDevice) that this class is composed of can be
    used however it is needed.
    """

    def __init__(self, device: IDevice):
        self.set_device(device)

    def set_device(self, device):
        self.device = device #self.device bridge to the device

    def toggle_power(self):
        if self.device.enabled:
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.get_volume()*1.1)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume()*0.9)

    def change_channel(self, new_channel):
        self.device.set_channel(new_channel)

class AdvancedRemote(Remote):
    """
    A child of the Remote class. This is an example of how the
    abstraction dimension can have its own inheritance hierarchy
    independent of the implementation class. We only need to add a
    single class to allow for multiple combinations.
    """

    def mute(self):
        self.device.set_volume(0)


def main():
    # combination 1: TV Remote
    print("---- COMBO 1: TV Remote ----")
    tv = TV()
    my_remote = Remote(tv)
    print(my_remote.device)
    my_remote.change_channel("Cartoon Network")
    print(my_remote.device)
    my_remote.toggle_power()
    print(my_remote.device)
    print("\n")

    #combination 2: Advanced Radio Remote
    print("---- COMBO 2: Advanced Radio Remote ----")
    radio = Radio()
    my_remote = AdvancedRemote(radio)
    print(my_remote.device)
    my_remote.mute()
    print(my_remote.device)
    my_remote.toggle_power()
    print(my_remote.device)

    print("\n")
    print("---- COMBO 3: Advanced Radio Remote back to TV ----")
    my_remote.set_device(tv)
    my_remote.mute()
    print(my_remote.device)


if __name__ == '__main__':
    main()