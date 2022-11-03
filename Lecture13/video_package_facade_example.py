"""
This module depicts the Facade pattern. The facade pattern provides a
simple interface to a complex interface/system/API. This hides
implementation details and only provides the interface that the rest of
the system needs.
"""
import video_manipulation_package as video_pkg


class VideoConverter:
    """
    The Facade. The VideoConverter defines a simple interface to the
    complicated video_manipulation_package. The VideoConverter deals
    with the interface provided by this complex package so that the
    rest of the system won't have to.
    """

    @staticmethod
    def convert(filename, dest_format="MP4"):
        """
        A simple interface that hides the complicated /complex procedure
        to convert a video file.
        :param filename: a string, path to the file
        :param dest_format: a string, MP4 or OGG
        :return: a VideoFile in the specified format.
        """
        video_file = video_pkg.VideoFile(filename)
        source_codec = video_pkg.CodecFactory().extract(video_file)

        if dest_format == "MP4":
            dest_codec = video_pkg.MPEG4CompressionCodec()
        else:
            dest_codec = video_pkg.OggCompressionCodec()

        buffer = video_pkg.BitrateReader.read(filename, source_codec)
        result = video_pkg.BitrateReader.convert(buffer, dest_codec)
        result = video_pkg.AudioMixer().fix(result)
        return result


def main():
    VideoConverter.convert("dog_bloopers.mp4", ".ogg")


if __name__ == '__main__':
    main()