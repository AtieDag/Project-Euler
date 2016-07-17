# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.


class Node:
    top_node = None

    def __init__(self, value, pos=0, index=1):
        self.left = None
        self.right = None
        self.pos = pos
        self.match = [index, index + 1]
        self.value = value

    def childe_pos(self, pos):
        if self.pos == pos:
            return self
        else:
            found = None
            if self.right is not None:
                found = self.right.childe_pos(pos)
            if self.left is not None and found is None:
                found = self.left.childe_pos(pos)
            if found is not None:
                return found

    def check_side(self):
        left = self.child_sum_l()
        right = self.child_sum_r()
        if left >= right:
            return 0
        else:
            return 1

    def child_sum_l(self, node_sum=0):
        node_sum += int(self.value)
        if self.left is not None:
            return self.left.child_sum_l(node_sum)
        return node_sum

    def child_sum_r(self, node_sum=0):
        node_sum += int(self.value)
        if self.right is not None:
            return self.right.child_sum_r(node_sum)
        return node_sum

    def insert(self, value, pos, index=1):
        # print("insert: value ", value, " pos: ", pos, " index ", index)
        if self.value:
            # Fill node
            if pos in self.match:
                exist = Node.top_node.childe_pos(pos)
                if self.match.index(pos) == 0:
                    if exist is None:
                        self.left = Node(value, pos, index)
                    else:
                        self.left = exist
                else:
                    if exist is None:
                        self.right = Node(value, pos, index)
                    else:
                        self.right = exist
            else:
                if self.left:
                    self.left.insert(value, pos, index)
                if self.right:
                    self.right.insert(value, pos, index)

        else:
            Node.top_node = self
            self.value = value

    def maximum_patch(self):

        print(self.value, end="+")
        if self.left is None or self.right is None:
            return 0
        if self.check_side() == 0:
            self.left.maximum_patch()
        else:
            self.right.maximum_patch()


def load_file(file_name):
    root = Node(None)
    with open(file_name) as file:
        pos = 0
        for index, line in enumerate(file):
            for k, value in enumerate(line.split()):
                root.insert(value, pos, pos + index + 1)
                pos += 1
    return root


if __name__ == '__main__':
    all_nodes = load_file('Problem18.txt')
    next_node = Node.top_node
    next_node.maximum_patch()
