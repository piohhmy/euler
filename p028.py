def spiral_corners(size):
    yield 1
    for x in range(3, size+1, 2):
        base_corner = x**2
        corner_diff = x-1
        for corner in (3,2,1,0):
            yield base_corner-corner_diff*corner

def solve_p026():
    return sum(spiral_corners(1001))

if __name__ == '__main__':
    print solve_p026()
