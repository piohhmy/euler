# Starting in top left corner, only being able to to move to the right and down,
# how many routes are in a 20x20 grid?

from nose.tools import *

def test_1x1_grid_has_2_routes():
    grid = Grid()
    grid.add(Node(0,0))
    grid.add(Node(0,1))
    grid.add(Node(1,0))
    grid.add(Node(1,1))

    routes = grid.find_routes((0,0), (1,1))

    assert_equal(routes, 2)

def test_2x2_grid_has_6_routes():
    grid = Grid()
    grid.add(Node(0,0))
    grid.add(Node(0,1))
    grid.add(Node(0,2))
    grid.add(Node(1,0))
    grid.add(Node(1,1))
    grid.add(Node(1,2))
    grid.add(Node(2,0))
    grid.add(Node(2,1))
    grid.add(Node(2,2))

    routes = grid.find_routes((0,0), (2,2))

    assert_equal(routes, 6)
        
def memoize(func):
    memoized_results = {}
    def wrapper(*args):
        if args not in memoized_results:
            memoized_results[args] = func(*args)
        return memoized_results[args]
    return wrapper

def generate_nodes(xmax,ymax):
    return [Node(x,y) for x in range(xmax+1) for y in range(ymax+1)]

class Grid(object):
    def __init__(self):
        self.nodes = [] 

    def find_routes(self, start_coor, end_coor):
        start_node = self.find_node(start_coor)
        end_node = self.find_node(end_coor)

        if start_node == None or end_node == None:
            return None
        return self._route(start_node, end_node)

    def find_node(self, coor):
        for node in self.nodes:
            if node.x == coor[0] and node.y == coor[1]:
                return node

    @memoize 
    def _route(self, start, end):
        if start.x == end.x and start.y == end.y:
            return 1
        if not start.connected_to:
            return 0

        total = 0
        for neighbor in start.connected_to:
             total += self._route(neighbor, end)

        return total

    def add(self, newnode):
        for node in self.nodes:
            newnode.connect(node)
            node.connect(newnode)
        self.nodes.append(newnode)


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_to = []

    def connect(self, other):
        if self._can_connect(other):
            self.connected_to.append(other)
            return True
        return False

    def _can_connect(self, other):
        if other.x - self.x == 1 and other.y - self.y == 0:
            return True
        if other.x - self.x == 0 and other.y - self.y == 1:
            return True
        return False

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Node({0}, {1})".format(self.x, self.y)

def solve_p015():
    nodes = generate_nodes(20,20)
    grid = Grid()
    for node in nodes:
        grid.add(node)

    return grid.find_routes((0,0), (20,20))

if __name__ == '__main__':
    print(solve_p015())
