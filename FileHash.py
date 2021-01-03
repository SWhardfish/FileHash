import hashlib

# BUFF_SIZE is configurable to suit your application
BUFF_SIZE = 65536  # read in 64kb chunks

md5 = hashlib.md5()
sha256 = hashlib.sha3_256()

with open('testfile.txt', 'rb') as f:
    while True:
        data = f.read(BUFF_SIZE)
        if not data:
            break
        md5.update(data)
        sha256.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA256: {0}".format(sha256.hexdigest()))
