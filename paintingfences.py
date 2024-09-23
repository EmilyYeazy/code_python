section1 = input()
section2 = input()
section3 = input()

from math import ceil
cans = len(section1)+len(section2)+len(section3)
pack = ceil(cans/12)
price = pack*14.95

print(f"Cans needed: {cans}")
print(f"Packs needed: {pack}")
print(f"Price cost: ${price}")