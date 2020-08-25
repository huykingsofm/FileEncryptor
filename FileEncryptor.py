from ImageGenerator import BMPImage

class FileEncryptor(object):
    def __init__(self, cipher, buffer_size = 1000):
        self.cipher = cipher
        self.buffer_size = buffer_size

    def encrypt(self, bytes_generator):
        ciphertext = b""
        for block in bytes_generator.iter(self.buffer_size):
            if not block:
                break

            cipherblock = self.cipher.encrypt(block, finalize = False)
            ciphertext += cipherblock

        last_cipherblock = self.cipher.encrypt(b"", finalize = True)
        ciphertext += last_cipherblock
        return ciphertext

    def encrypt_yield(self, bytes_generator):
        for block in bytes_generator.iter(self.buffer_size):
            if not block:
                break

            cipherblock = self.cipher.encrypt(block, finalize = False)
            yield cipherblock

        last_cipherblock = self.cipher.encrypt(b"", finalize = True)
        yield last_cipherblock

    def encrypt_to(self, bytes_generator, ou_filename):
        with open(ou_filename, mode= "wb") as stream:
            for block in self.encrypt_yield(bytes_generator):
                stream.write(block)

    def decrypt(self, bytes_generator):
        plaintext = b""
        for block in bytes_generator.iter(self.buffer_size):
            if not block:
                break
            
            plainblock = self.cipher.decrypt(block, finalize = False)
            plaintext += plainblock
        
        last_plainblock = self.cipher.decrypt(b"", finalize = True)
        plaintext += last_plainblock
        return plaintext

    def decrypt_yield(self, bytes_generator):
        for block in bytes_generator.iter(self.buffer_size):
            if not block:
                break
            
            plainblock = self.cipher.decrypt(block, finalize = False)
            yield plainblock
        
        last_plainblock = self.cipher.decrypt(b"", finalize = True)
        yield last_plainblock
        
    def decrypt_to(self, bytes_generator, ou_filename):
        with open(ou_filename, "wb") as stream:
            for block in self.decrypt_yield(bytes_generator):
                stream.write(block)

class BMPEncryptor(FileEncryptor):
    def encrypt(self, bmp_img: BMPImage):
        header = bmp_img.get_header()
        cipher_payload = super().encrypt(bmp_img.create_generator())
        return header + cipher_payload
    
    def encrypt_yield(self, bmp_img: BMPImage):
        yield bmp_img.get_header()
        for block in super().encrypt_yield(bmp_img.create_generator()):
            yield block

    def decrypt(self, bmp_img: BMPImage):
        header = bmp_img.get_header()
        payload = super().decrypt(bmp_img.create_generator())
        return header + payload

    def decrypt_yield(self, bmp_img: BMPImage):
        yield bmp_img.get_header()
        for block in super().decrypt_yield(bmp_img.create_generator()):
            yield block
            

if __name__ == "__main__":
    # Test your code
    from Cipher import XorCipher, AES_CTR, NoCipher
    from BytesGenerator import BytesGenerator
    import os
    
    key = b"0123456789abcdef"
    nonce = b"0011223344556677"
    nonce = os.urandom(16)
    cipher = AES_CTR(key)
    cipher.set_param(0, nonce)

    #cipher = XorCipher(b"2")
    #cipher.set_param(0, b"1")
    #cipher = NoCipher()

    bmp_img = BMPImage("fingerprint_test.BMP")
    bmp_enc = BMPEncryptor(cipher)
    bmp_enc.encrypt_to(bmp_img, "fp.bmp")
    pass