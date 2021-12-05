# function values with its first and second derivation

import math
def derivation(x):
    f = math.cos(2 * x)
    g = - 2 * math.sin(2 * x)
    h = - 4 * math.cos(2 * x)
    return f, g, h

print(derivation(math.pi))
f, g, h = derivation(math.pi)
print(f'{f:.4f}, {g:.4f}, {h:.4f}')
