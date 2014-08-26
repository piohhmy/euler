# Starting in top left corner, only being able to to move to the right and down,
# how many routes are in a 20x20 grid?

from nose.tools import *

def test_2x2_grid_has_6_routes():
    x = 0
    y = 0
    path = [(x,y)]
    while True:
        path.append
        

def find_next_path(x, y):
    if x + 1 > 2:
        return (x,y)
    else:
        return [(x,y)].append(find_next_path(x+1, y))

    if y + 1 > 2:
        return (x,y)
    else:
        return [(x,y)].append(find_next_path(x, y+1))


def generate_grid(xmax,ymax):
    return [Node(x,y) for x in range(xmax) for y in range(ymax)]

def can_connect(curr, neighbor):
    if neighbor.x - curr.x == 1 and neighbor.y - curr.y == 0:
        return True
    if neighbor.x - curr.x == 0 and neighbor.y - curr.y == 1:
        return True
    return False


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_to = []

    def connect(self, other):
        self.connected_to.append(other)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Node({0}, {1})".format(self.x, self.y)

def solve_p015():
    grid = generate_grid(21,21)
    for node in grid:
        for pot_neighbor in grid:
            if can_connect(node, pot_neighbor):
                node.connect(pot_neighbor)

    return find_paths(grid[0])

def memoize(func):
    memoized_results = {}
    def wrapper(*args):
        if args not in memoized_results:
            memoized_results[args] = func(*args)
        return memoized_results[args]
    return wrapper

@memoize
def find_paths(node):
    if node.x == 20 and node.y == 20:
        return 1
    if not node.connected_to:
        return 0

    total = 0
    for neighbor in node.connected_to:
         total += find_paths(neighbor)

    return total

if __name__ == '__main__':
    print solve_p015()
