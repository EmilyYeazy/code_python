from math import sqrt, floor
tiles = int(input())
side_length = sqrt(tiles)
side_length = floor(side_length)
print(f"The largesst square had a side length of {side_length}.")