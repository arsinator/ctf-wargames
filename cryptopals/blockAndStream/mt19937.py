def uint32_t(x): return x & 0xffffffff
class MT19937:
  def __init__(self, seed):
    self.index = 624
    self.mt = [0 for _ in range(624)]

    self.mt[0] = seed

    for i in range(1, 624):
      self.mt[i] = \
        uint32_t(1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i)

  def random(self):
    if self.index >= 624: self.twist()

    y = self.mt[self.index]

    y = y ^ y >> 11
    y = y ^ y << 7 & 2636928640
    y = y ^ y << 15 & 4022730752
    y = y ^ y >> 18

    self.index += 1

    return uint32_t(y)

  def twist(self):
    for i in range(624):
      y = uint32_t((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff))
      self.mt[i] = self.mt[(i + 397) % 624] ^ y >> 1

      if y % 2 == 0: self.mt[i] &= 0x9908b0df

    self.index = 0

