import os
def encrypt(message,key):
    message = message.encode()
    out = []
    for i in range(len(message)):
        out+= [message[i]^key[i%len(key)]]
    return bytes(out).hex()

FLAG = "GPNCTF{fake_flag}"
key = os.urandom(5)
d=str(encrypt(FLAG,key))


c = "d24fe00395d364e12ea4ca4b9f2da4ca6f9a24b2ca729a399efb2cd873b3ca7d9d1fb3a66a9b73a5b43e8f3d"

pre_flag = 'GPNCTF{'
key = ""
out2 = []
for i in range(len(pre_flag)):
    out2 += [ord(c[i]) ^ord(pre_flag[i])]
    key += chr(out2[i])
print("key:" ,key)

flag = ""
for i in range(len(c)):
    code = ord(c[i]) ^ ord(key[i%len(key)])
    flag += chr(code)
print("flag:", flag)

