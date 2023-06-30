"""
# Journey Python - Chapter 40
# Data compression using bz2.
"""
import bz2
def gen_data(chunks=10, chunksize=1000):
    for _ in range(chunks):
        yield b"z" * chunksize

comp = bz2.BZ2Compressor()
out = b""

for chunk in gen_data():
    out = out + comp.compress(chunk)

out = out + comp.flush()
print(out)