import sys


class Xor:
    def __init__(self) -> None:
        self.code = bytearray(
            b"\x08\x0f\x13^@GA\x17\x11]^Z\x03L\x11TCF\x04\x11\x17;BA\x08\x0c\x17\x19\x10{\x04\x0e\x0f^\x1e\x13\r\x07\x17B\x12T\x0eB\x17^\x12T\x0e\r\x04]W\x1d\x02\r\x0e\x1f\x10\x1ak\x12\x11X\\GI\x17\x11]^Z\x03L\x11TCF\x04\x11\x17\x1fGA\r\r\x13T\\\x1bC\n\x17EB@[MLV]\\\x06\x0e\x06\x1fQ\\\x0c@J\x1f@V\x00\x06K\x18\x1cW\x04\x01\x0cUW\x1bHK")

    def xor(self, key) -> bytearray:
        result = bytearray()

        for i in range(len(self.code)):
            data_byte = self.code[i]
            key_byte = key[i % len(key)]  # Cycle through the key
            ciphertext = data_byte ^ key_byte
            result.append(ciphertext)

        return result


def main() -> None:
    globals_dict = {}
    locals_dict = {}
    key = ''

    try:
        key = sys.argv[1].encode()
    except IndexError:
        print(f"[!] Please provide the secret passphrase as the only argument.")
        sys.exit(1)

    xor = Xor()

    try:
        exec(xor.xor(key), globals_dict, locals_dict)
    except SyntaxError:
        print(f"Wrong passphrase.")
        sys.exit(1)


if __name__ == "__main__":
    main()
