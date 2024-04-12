import base64
import numpy as np
import random

from coubeh import key_function_generation_inverse_function_fast as key_function_generation_inverse_function_fast

class Xylophone:
    def __init__(self, blipblop: str):
        self.blipblop = blipblop
        self.bloopbloop = None
        self.zorblatt = None
        self.bloop = None

    def flibber(self):
        self.bloopbloop = base64.b64decode(self.blipblop).decode('utf-8')
        self.bloop = self.bloopbloop[::-1]
        return self.bloopbloop

    def plumbumble(self):
        buzzy = np.random.rand(3, 3)
        jibbly = np.random.rand(3, 3)
        snorfle = np.random.rand(3, 3)
        buzzy = np.add(buzzy, snorfle)
        self.zorblatt = np.dot(buzzy, jibbly)
        np.savetxt("zorblatt.csv", self.zorblatt, delimiter=",")
        return self.zorblatt
    
    def get_zorblatt(self):
        return self.zorblatt

import base64
def shift_bytes(byte_seq, shift=1):
    return bytes([(b + shift) % 256 for b in byte_seq])

# Function to XOR two byte sequences
def xor_bytes(byte_seq1, byte_seq2):
    return bytes([b1 ^ b2 for b1, b2 in zip(byte_seq1, byte_seq2)])

# Inverse procedure: Reconstructing the original base64 string
def reconstruct_original(base64_key1, base64_key2):
    # Decode the base64 keys
    key1 = base64.b64decode(base64_key1)
    key2 = base64.b64decode(base64_key2)
    
    # Reverse the shifts to obtain the original bytes
    original_part1 = shift_bytes(key1, shift=-3)  # Reverse shift for part1
    original_part2 = shift_bytes(key2, shift=-7)  # Reverse shift for part2
    
    # Combine the two parts to get the original byte sequence
    reconstructed_bytes = original_part1 + original_part2
    
    # Return the base64 encoded result (same as the original)
    return base64.b64encode(reconstructed_bytes).decode('utf-8')

class FlibberWobber:
    def __init__(self):
        self.narp = None
        self.xylophone = None
        self.wibble = None

    def set_narp(self):
        self.narp = input("Enter code: ")

    def ziggazagg(self, blorp: int, splork: str):
        if blorp > 0:
            splork = self.ziggazagg(blorp - 1, splork)
        return splork[::-1]

    def flibble(self):
        key2 = key_function_generation_inverse_function_fast()
        self.narp = reconstruct_original(self.narp, key2)
        self.xylophone = Xylophone(self.narp)
        adversarial_policy = self.xylophone.plumbumble()
        splorp = self.ziggazagg(3, self.narp)
        # np.dot(adversarial_policy)
        self.wibble = self.xylophone.flibber()
        return self.wibble

    def wobbly(self):
        return self.wibble + " | End of Wobbly Operation"

class Quizzlestick:
    def __init__(self):
        self.bloopa = None
        self.bloopb = None

    def mumble(self, florp, blorp):
        return np.dot(florp, blorp)

class Zorpinator:
    def __init__(self):
        self.flubber = FlibberWobber()
        self.quizzlestick = Quizzlestick()
        self.final_bloop = None

    def sproing(self):
        self.flubber.set_narp()
        self.final_bloop = self.flubber.flibble()
        return self.final_bloop

if __name__ == "__main__":
    zorp = Zorpinator()
    bloop = zorp.sproing()
    print(f"Final uncoded url: {bloop}")
