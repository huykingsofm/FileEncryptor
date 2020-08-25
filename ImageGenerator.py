from itertools import tee
from BytesGenerator import BytesGenerator

class ImageGeneratorException(Exception): ...
class ImageFormatError(ImageGeneratorException): ...

class BMPImage(object):
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "rb") as stream:
            header = stream.read(14)
            if header[0:2] != b"BM":
                raise ImageFormatError("This is not BMP file")
            self.start_of_image = int.from_bytes(header[-4:], "little")

    def create_generator(self):
        stream = open(self.filename, "rb")
        stream.seek(self.start_of_image)
        return BytesGenerator("stream", stream)

    def get_header(self):
        with open(self.filename, "rb") as stream:
            return stream.read(self.start_of_image)

if __name__ == "__main__":
    # Test your code
    fou = open("fgp_t_o.bmp", "wb")
    bmp = BMPImage("fingerprint_test.bmp")

    fou.write(bmp.get_header())
    for a in bmp.create_generator().iter():
        fou.write(a)
    fou.close()
    pass