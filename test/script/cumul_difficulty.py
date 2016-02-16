import sys

# https://en.bitcoin.it/wiki/Difficulty

DIFFICULTY_1 = 0x00000000FFFF0000000000000000000000000000000000000000000000000000

# based on http://www.righto.com/2014/02/bitcoin-mining-hard-way-algorithms.html#ref3
def targetFromBits(bits):
    exp = bits / 0x1000000  # 2**24
    mant = bits & 0xffffff
    return mant * 256**(exp - 3)

# print hex(targetFromBits(0x1b0404cb))
# sys.exit(0)

with open("../headers/blockchain_headers") as f:
    f.seek(72)
    rev_diff_bits = f.read(4)
    diff_bits = rev_diff_bits[::-1]

    diff_num = targetFromBits(int(diff_bits.encode('hex'), 16))

    # diff_hex = hex(diff_num)
    # print diff_hex

    print DIFFICULTY_1 / diff_num
    # f.seek(80 * startBlock)
    # bhBytes = f.read(80 * count)
