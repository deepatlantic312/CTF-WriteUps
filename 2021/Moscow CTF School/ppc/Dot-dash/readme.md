# Dot-dash
_nc dot-dash.tasks.2021.ctf.cs.msu.ru 20009_

### Solution

```python
from pwn import remote
from math import radians, sin, cos, acos

MORSE_CODE_DICT = {'E': '.', 'N': '-.', 'S': '...', 'W': '.--',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', '#': '.......', '.': '.-.-.-'}

def morse_to_coordinates(morse_code):
    morse_code = morse_code.split()
    for letter in MORSE_CODE_DICT:
        for i, cod in enumerate(morse_code):
            if cod == MORSE_CODE_DICT[letter]:
                morse_code[i] = letter
    s = ''.join(morse_code).split('#')
    
    return (-float(s[0].replace('S', '')) if 'S' in s[0] else float(s[0].replace('N', '')),
            -float(s[1].replace('W', '')) if 'W' in s[1] else float(s[1].replace('E', '')),
            -float(s[2].replace('S', '')) if 'S' in s[2] else float(s[2].replace('N', '')),
            -float(s[3].replace('W', '')) if 'W' in s[3] else float(s[3].replace('E', '')))

def great_circle(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


r = remote("dot-dash.tasks.2021.ctf.cs.msu.ru", 20009)

print(r.recvline().decode())
r.sendline('Y')
while True:
    print(r.recvline().decode())
    r.sendline(str(round(great_circle(*morse_to_coordinates(decrypt_morse(r.recvline().decode()))), 5)).encode())
    print(r.recvline().decode())

```