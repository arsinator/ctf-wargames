from mt19937 import MT19937
from struct import pack

def encrypt_MT19937(plaintext, key):
  assert key in range(0, 2 ** 16)

  ciphertext = b''
  mt = MT19937(key)

  byte_count = 0
  while byte_count < len(plaintext):
    if byte_count % 4 == 0:
      keystream = pack('>I', mt.random())

    ciphertext += \
      bytes([plaintext[byte_count] ^ keystream[byte_count % 4]])

    byte_count += 1

  return ciphertext

def decrypt_MT19937(ciphertext, key):
  return encrypt_MT19937(ciphertext, key)
