import argparse
import base64
import binascii
import codecs
import urllib.parse


def looks_like_text(s):
    #A: return True if s is not empty AND s.isprintable()
    return len(s) > 0 and s.isprintable()
    #Returns True only if the string is NOT empty AND every character is printable.


def try_hex(s):
    try:
        out = bytes.fromhex(s).decode()
    except (ValueError, UnicodeDecodeError):
        return None
    return out if looks_like_text(out) else None


def try_base64(s):
    #B: same pattern as try_hex, but use base64.b64decode(s, validate=True).
    #Catch (binascii.Error, ValueError, UnicodeDecodeError).
    try:
        out = base64.b64decode(s, validate=True).decode()
    except (binascii.Error, ValueError, UnicodeDecodeError):
        return None
    return out if looks_like_text(out) else None
    #makes Python reject anything that is not proper Base64, instead of quitly skipping the bad characters.


def try_url(s):
    #C: if "%" is not in s, return None. Otherwise return urllib.parse.unquote(s).
    if "%" not in s:
        return None
    return urllib.parse.unquote(s)


def decode_once(s):
    for name, fn in [("hex", try_hex), ("base64", try_base64), ("url", try_url)]:
        out = fn(s)
        if out is not None:
            return name, out
    return None, None


def main():
    parser = argparse.ArgumentParser(description="Auto-detect and decode a mystery string")
    parser.add_argument("text", help="the encoded string")
    args = parser.parse_args()

    s = args.text.strip()
    for layer in range(1, 6):          # peel up to 5 layers
        name, out = decode_once(s)
        if name is None:
            break
        print(f"Layer {layer}: {name} -> {out}")
        s = out
    print(f"ROT13 guess: {codecs.encode(s, 'rot13')}")


if __name__ == "__main__":
    main()