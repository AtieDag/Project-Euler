# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down.
# There are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# from joblib import Parallel, delayed
# import multiprocessing


class Node:
    routes = 0
    size = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbour_down = None
        self.neighbour_right = None

    def set_neighbour(self, down, right):
        self.neighbour_down = down
        self.neighbour_right = right

    def next_node(self):
        # print("Pos: X" + str(self.x) + " Y" + str(self.y))
        if self.neighbour_down is not None:
            self.neighbour_down.next_node()
        if self.neighbour_right is not None:
            self.neighbour_right.next_node()
        if self.x == Node.size and self.y == Node.size:
            Node.routes += 1
            print("Node routes {0}".format(Node.routes))


if __name__ == '__main__':
    Size = 20
    Node.size = Size
    Matrix = []
    # Create nodes
    for i in range(Size + 1):
        Matrix.append([])
        for j in range(Size + 1):
            Matrix[i].append(Node(i, j))

    # Connect neighbours
    for row in Matrix:
        for n in row:
            # print("X " + str(n.x) + " Y " + str(n.y))
            if Size > n.x and Size > n.y:
                n.set_neighbour(Matrix[n.x + 1][n.y], Matrix[n.x][n.y + 1])
            elif n.x == Size and n.y == Size:
                pass
            elif n.x == Size:
                n.set_neighbour(None, Matrix[n.x][n.y + 1])
            elif n.y == Size:
                n.set_neighbour(Matrix[n.x + 1][n.y], None)

    # Start Executing
    print(Node.routes)
