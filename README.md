# FileEncryptor
A module is used to encrypt and decrypt a file

# USAGE
## FileEncryptor
Encrypt and decrypt a arbitrary file
<details> 
<summary> Click to see details </summary>

### @Constructor
```Py
__init__(self, cipher: Cipher, buffer_size:int = 1000)
```
**Parameters**
* `cipher`: a object in module [Cipher](https://github.com/huykingsofm/LocalVNetwork/blob/master/Cipher.py). This is type of Cipher which encrypt and decrypt your file.

* `buffer_size`: the maximum size of content which file stream read each time.

### @Method
```Py
encrypt(self, bytes_generator: BytesGenerator)
```
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

**Return**  
The content of encrypted file as bytes object

### @Method
```Py
encrypt_yield(self, bytes_generator: BytesGenerator)
```
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

**Return**  
The content of encrypted file as iterator of bytes

### @Method
```Py
encrypt_to(self, bytes_generator: BytesGenerator, ou_filename: str)
```
Encrypt content from `BytesGenerator` and save it to a file.  
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

* ou_filename: the file contains encrypted content of original file.

**Return**  
No return

### @Method
```Py
decrypt(self, bytes_generator: BytesGenerator)
```
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

**Return**  
The content of decrypted file as bytes object

### @Method
```Py
decrypt_yield(self, bytes_generator: BytesGenerator)
```
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

**Return**  
The content of decrypted file as iterator of bytes

### @Method
```Py
encrypt_to(self, bytes_generator: BytesGenerator, ou_filename: str)
```
Decrypt content from `BytesGenerator` and save it to a file.  
**Parameters**  
* bytes_generator: a [`BytesGenerator`](./BytesGenerator.py) which generates block of bytes from bytes itself or file stream.

* ou_filename: the file contains decrypted content of original file.

**Return**  
No return

</details>

## BMPEncryptor (subclass of FileEncryptor)
Encrypt and decrypt a bitmap image while still maintains format of file  

*All methods is same the its parent (FileEncryptor), but the parameter `BytesGenerator` must be replace with `BMPImage` in [`ImageGenerator`](./ImageGenerator.py) module*

# Example
## Example of BMPEncryptor
```Py
from Cipher import AES_CTR
from FileEncryptor import FileEncryptor
from BytesGenerator import BytesGenerator
    
key = b"0123456789abcdef"
nonce = b"0011223344556677"
cipher = AES_CTR(key)
cipher.set_param(0, nonce)

file_generator = BytesGenerator("file", "./test_files/fingerprint_test.BMP")
file_enc = BMPEncryptor(cipher)
file_enc.encrypt_to(file_generator, "./test_files/tset_tnirpregnif.bmp")
```
## Example of BMPEncryptor
```Py
from Cipher import AES_CTR
from ImageGenerator import BMPImage
from FileEncryptor import BMPEncryptor
    
key = b"0123456789abcdef"
nonce = b"0011223344556677"
cipher = AES_CTR(key)
cipher.set_param(0, nonce)

bmp_img = BMPImage("./test_files/fingerprint_test.BMP")
bmp_enc = BMPEncryptor(cipher)
bmp_enc.encrypt_to(bmp_img, "./test_files/tset_tnirpregnif.bmp")
```