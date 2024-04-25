Introduction  

This program will execute XOR encrypted ciphertext (Python code) when provided the right passphrase or key, in memory. In this example, the encrypted code outputs, “Hello, lets go to google.com.” to the terminal. It then creates a connection to google.com and retrieves the homepage using urllib3.request. The Python code is only decrypted in memory, so if the script were discovered, the ciphertext will prevent anyone without the correct key from viewing the instructions.  

What is XOR encryption?  

Think of your Python instructions as strings of zeros and ones. Each zero or one represents a bit of information. XOR (Exclusive OR) is a special operation that compares these strings bit by bit:  

If both bits are the same (0 and 0, or 1 and 1), the result is 0.  
If the bits are different (0 and 1, or 1 and 0), the result is 1.  

To encrypt, you “XOR” your Python code with a key, meaning the operation performs this bitwise comparison for every corresponding bit in the Python code. This results in a scrambled version of the Python code or a “ciphertext.”  

Decrypting is simple: you perform the same XOR operation again with the same key. Since XOR is its own inverse, the scrambled bits are flipped back to their original state and the secret Python code is then processed and run with exec().  

In this script (pyxor.py), the software retrieves the Python code ciphertext that has been provided, then decrypts this code in memory, and then runs the decrypted code stored in memory.  

A corresponding Python file (xor_encrypt.py) is provided so that a user can encrypt Python instructions into a bytearray payload. This payload is provided to “pyxor.py”.  

Usage Summary  

```
python xor_encrypt.py <key>  
> python xor_encrypt abc123
```

```
> python .\pyxor.py abc123
Hello, lets go to google.com.
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp, " name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/ 
...
```
