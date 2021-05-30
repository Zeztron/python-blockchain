import hashlib
import json

def crypto_hash(data):
    """
    Return a sha-256 hash of the given data.
    """
    stringify_data = json.dumps(data)

    return hashlib.sha256(stringify_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")

if __name__ == '__main__':
    main()