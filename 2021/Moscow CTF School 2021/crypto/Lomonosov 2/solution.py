from binascii import unhexlify
from Crypto.Util.number import long_to_bytes
from pwn import xor
from math import log

p = ...
n = ...
enc_flag = b'...'

enc_flag = unhexlify(enc_flag)

key = 0
for power in range(1, int(log(n, p))):
    key += n // (p ** power)
key = long_to_bytes(key)
flag = xor(enc_flag, key).decode()
flag = flag[:flag.find("}") + 1]
print(flag)
