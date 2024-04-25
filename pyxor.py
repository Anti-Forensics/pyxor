import sys


class Xor:
    def __init__(self):
        self.code = bytearray(
            b"\x11\x10\n_F\x1bC\n\x06]^\\CKiUWUA\x15\x0cC^WIKY;\x12\x13AB\x11TFF\x13\x0cC\x13E\\\x13\x0e\x07\x13")

    def xor(self, key):
        result = bytearray()

        for i in range(len(self.code)):
            data_byte = self.code[i]
            key_byte = key[i % len(key)]  # Cycle through the key
            xor_result = data_byte ^ key_byte
            result.append(xor_result)

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
        world_func = locals_dict['world']
        print(world_func())
    except SyntaxError:
        print(f"Wrong passphrase.")
        sys.exit(1)


if __name__ == "__main__":
    main()
