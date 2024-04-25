"""
This program will generate ciphertext from the instructions stored in the "code" variable.
"""
import sys


def xor(key, code):
    result = bytearray()

    for i in range(len(code)):
        data_byte = code[i]
        key_byte = key[i % len(key)]  # Cycle through the key
        ciphertext = data_byte ^ key_byte
        result.append(ciphertext)

    return result


def main() -> None:
    code = b'''import urllib.request
print("Hello, lets go to google.com.")
print(urllib.request.urlopen("https://google.com").read().decode())'''

    try:
        key = sys.argv[1].encode()
    except IndexError:
        print(f"[!] Please provide the secret passphrase as the only argument.")
        sys.exit(1)

    print(xor(key, code))


if __name__ == "__main__":
    main()
