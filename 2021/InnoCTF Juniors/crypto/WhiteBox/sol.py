PNG_header = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0X0a, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44]

with open("image.png", "rb") as f:
    data = f.read()

key = ""
for i in range(len(PNG_header)):
    key += chr(PNG_header[i] ^ data[i])

res = []
for i in range(len(data)):
    res.append(data[i] ^ ord(key[i % len(key)]))

with open("res.png", "wb") as f:
    f.write(bytearray(res))
