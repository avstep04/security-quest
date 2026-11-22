import hashlib
from importlib.metadata import FileHash

message = "Cyber Quest Day 2"

# 1. Hash `message` with md5, sha1 and sha256.
#    Print the algorithm name, the hex digest, and len() of the digest.

md5_hash = hashlib.md5(message.encode()).hexdigest()
print("MD5:   ", md5_hash, len(md5_hash))

sha1_hash = hashlib.sha1(message.encode()).hexdigest()
print("SHA-1:   ", sha1_hash, len(sha1_hash))

sha256_hash = hashlib.sha256(message.encode()).hexdigest()
print("SHA-256:   ", sha256_hash, len(sha256_hash))

# 2. Avalanche effect: hash "hello" and "Hello" with sha256 and print both.
sha256_hash1 = hashlib.sha256("hello".encode()).hexdigest()
print("SHA-256 (hello):   ", sha256_hash1, len(sha256_hash1))

sha256_hash2 = hashlib.sha256("Hello".encode()).hexdigest()
print("SHA-256 (Hello):   ", sha256_hash2, len(sha256_hash2))
#    How many characters stayed the same?
print(sum(a == b for a, b in zip(sha256_hash1, sha256_hash2)), "of 64 characters match")

# 3. Hash Practice via browser
#Running Sha1 and both results are in fact identical, which is a known collision in SHA1. The two files are different but have the same SHA1 hash.
    #Get-FileHash $HOME\Downloads\shattered-1.pdf -Algorithm SHA1
    #Get-FileHash $HOME\Downloads\shattered-2.pdf -Algorithm SHA1
#Running Sha256 and both results are different, which is expected since SHA256 is more secure and does not have known collisions like SHA1.
    #Get-FileHash $HOME\Downloads\shattered-1.pdf -Algorithm SHA256
    #Get-FileHash $HOME\Downloads\shattered-2.pdf -Algorithm SHA256