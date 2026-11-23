import base64
import codecs
import urllib.parse

# 1. Base64: decode the string from challenge #1, then re-encode it
b64 = "RW5jb2RpbmcgaXMgbm90IGVuY3J5cHRpb24="
    #base64.b64decode(b64) gives bytes; add .decode() to get text. Print it.
print(base64.b64decode(b64).decode())

# 2. Hex: decode challenge #2
hex_str = "416e796f6e652063616e20726576657273652074686973"
#bytes.fromhex(hex_str).decode()
print(bytes.fromhex(hex_str).decode())

# 3. URL: decode challenge #3
url_str = "user%3Dandy%26role%3Dadmin%20%26%20token%3D1234%20%3Cscript%3E"
    #urllib.parse.unquote(url_str)
print(urllib.parse.unquote(url_str))

# 4. ROT13: decode challenge #4
rot = "Pnrfne jbhyq or cebhq"
    #codecs.encode(rot, "rot13")  (running ROT13 twice undoes it)
print(codecs.encode(rot, "rot13"))

# 5. Prove it's reversible: encode your own name to Base64 and back
    #base64.b64encode("Andy".encode()).decode()
encoded = base64.b64encode("Andy".encode()).decode()
print(encoded)
print(base64.b64decode(encoded).decode())