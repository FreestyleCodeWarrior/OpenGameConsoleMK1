"""
slice_range = tuple((i*8, i*8+8) for i in range(2))
def write_image(lines):
    for x in range(8):
        for y in range(2):
            print(1+x,"0b{}{}{}{}{}{}{}{}".format(*lines[x][slice_range[y][0]:slice_range[y][1]]))

lines = [
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
    [1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,],
]

write_image(lines)
"""

rows = 1,4,15,2,8,13
lencs = 2

for r in rows:
    for l in range(lencs):
        if r in range(8*l, 8*l+8):
            print(r, "cs", l, "on")
            break
