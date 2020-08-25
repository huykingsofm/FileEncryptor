import io

class InvalidArgument(Exception): ...

class BytesGenerator(object):
    def __init__(self, obj_type, value):
        all_obj_types = ["file", "bytearray", "stream"]
        if obj_type not in all_obj_types:
            raise InvalidArgument(f"obj_type must be in {all_obj_types}")

        self.type = obj_type
        if obj_type == "file":
            if not isinstance(value, str):
                raise InvalidArgument("File name must be a str")

            self.stream = open(value, "rb")
        
        if obj_type == "bytearray":
            if not isinstance(value, bytearray) and not isinstance(value, bytes):
                raise InvalidArgument("Expected bytes or bytearray object")
    
            self.stream = value
            if isinstance(value, bytes):
                self.stream = bytearray(self.stream)

        if obj_type == "stream":
            if not isinstance(value, io.BufferedIOBase):
                raise InvalidArgument("Stream must be a file which open in binary mode")

            cursor = value.tell()
            value.read(1)
            value.seek(cursor)
            self.stream = value

    def read(self, buffer_size = 1024):
        if self.type == "file" or self.type == "stream":
            return self.stream.read(buffer_size)
        
        if self.type == "bytearray":
            value = self.stream[:buffer_size]
            del self.stream[:buffer_size]
            return value

    def close(self):
        if self.type == "file" or self.type == "stream":
            self.stream.close()
            del self.stream
        
        if self.type == "bytearray":
            del self.stream

    def iter(self, buffer_size = 1024):
        while True:
            data = self.read(buffer_size)
            if not data:
                break
            yield data
        self.close()

