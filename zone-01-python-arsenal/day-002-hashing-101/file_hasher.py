import argparse
import hashlib
import hmac

CHUNK_SIZE = 65536  # read 64 KB at a time


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        # Read the file in chunks and feed each chunk into h.update(chunk). f.read(CHUNK_SIZE) returns b"" (empty) at the end of the file.
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Verify a file's SHA-256 checksum")
    parser.add_argument("file", help="path to the file to check")
    parser.add_argument("expected", help="the SHA-256 hash the publisher posted")
    args = parser.parse_args()

    actual = sha256_of_file(args.file)
    
    expected = args.expected.strip().lower()

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    if hmac.compare_digest(actual, expected):
        print("MATCH: file is authentic")
    else:
        print("MISMATCH: do not trust this file")


if __name__ == "__main__":
    main()