"""
Video manipulation package. A placeholder complex package to demonstrate
the facade pattern. Courtesy of
https://refactoring.guru/design-patterns/facade
"""

class VideoFrame:
    pass


class VideoFile:

    def __init__(self, filename):
        print(f"Video file object create from {filename}")


class Codec:
    pass


class OggCompressionCodec(Codec):

    def __init__(self):
        print("OGG Codec created")


class MPEG4CompressionCodec(Codec):

    def __init__(self):
        print("MPEG4 Codec created")


class CodecFactory:

    def extract(self, video):
        print(f"Creating codec from video file")
        return MPEG4CompressionCodec()


class BitrateReader:

    @staticmethod
    def read( filename, source_codec):
        print(f"reading {filename} via a {source_codec.__class__.__name__} "
              f"into a buffer")

    @staticmethod
    def convert(buffer, dest_codec):
        print(f"writing file from {buffer} and converting it via "
              f"{dest_codec.__class__.__name__}")


class AudioMixer:
    def fix(self, video):
        print(f"Fixing audio levels in converted video")
