from mt19937 import MT19937

def uint32_t(n):
  return n & 0xffffffff

def untemper(y):
  y ^= y >> 18 & 0x3fff

  m = 4022730752
  y ^= (m >> 15 & 0x7fff & (y & 0x7fff)) << 15
  y ^= (m >> 30 & 0x7fff & (y >> 15 & 0x7fff)) << 30
  y ^= uint32_t((m >> 45 & 0x7fff & (y >> 30 & 0x7fff)) << 45)

  m = 2636928640
  y ^= (m >> 7 & 0x7f & (y & 0x7f)) << 7
  y ^= (m >> 14 & 0x7f & (y >> 7 & 0x7f)) << 14
  y ^= (m >> 21 & 0x7f & (y >> 14 & 0x7f)) << 21
  y ^= uint32_t((m >> 28 & 0x7f & (y >> 21 & 0x7f)) << 28)

  y ^= (y >> 11) & 0x1ffc00
  y ^= (y & 0x1fffff) >> 11

  return y

def temper(y):
  y ^= y >> 11
  y ^= y << 7 & 2636928640
  y ^= y << 15 & 4022730752
  y ^= y >> 18

  return y

mt = MT19937(42)
tempered_state = [mt.random() for _ in range(624)]
untempered_state = list(map(untemper, tempered_state))

assert untempered_state == mt.mt

cloned = MT19937(0xdeadbeef)
cloned.mt = untempered_state

for _ in range(100): assert cloned.random() == mt.random()
