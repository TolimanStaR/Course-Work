import math

d, rad, orb = map(int, input().split())

p = (d + 2 * orb) / 2

s = math.sqrt(abs(p * (p - orb) * (p - orb) * (p - d)))

h = (2 * s) / d

print('Escape' if h >= rad else 'Trouble')