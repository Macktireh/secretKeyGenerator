import sys
import string
import secrets


RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)"
DELETE_TABLE = str.maketrans('', '', '",;.|\\\'"')


def get_random_secret_key(length=64, allowed_chars=RANDOM_STRING_CHARS) -> str:
    return "".join(secrets.choice(allowed_chars) for _ in range(length))


def main() -> None:
    try:
        argv: list = sys.argv[1:]

        if not argv:
            return print(get_random_secret_key())

        length: int = int(argv[0])
        allowed_chars: str = argv[1] if len(argv) > 1 else string.printable
        allowed_chars = allowed_chars.translate(DELETE_TABLE).replace("'", "").replace('"', '').replace('\\', '').replace('/', '')

        return print(get_random_secret_key(length, allowed_chars))
    except ValueError:
        print(f"ValueError : the expected value is an integer but the received value is '{argv[0]}'.")
        sys.exit(2)
    except Exception as e:
        print(f"Exception : {e}")
        sys.exit(2)


if __name__ == '__main__':
    main()
