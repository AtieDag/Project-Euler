# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.


class Node:
    top_node = None
    botton_max_node = None
    botton_max_value = 0
    exist = {}

    def __init__(self, value=0, pos=0, index=1):
        self.left = None
        self.right = None
        self.pos = pos
        self.match = [index, index + 1]
        self.value = value
        self.path_sum = 0
        self.path_dir = None
        Node.exist[pos] = self

    def insert(self, value, pos, index=1):
        if self.value:
            # Fill node
            if pos in self.match:
                # print("insert: value ", value, " pos: ", pos, " index ", index)

                if pos in Node.exist:
                    exist = Node.exist[pos]
                else:
                    exist = None

                if self.match.index(pos) == 0:
                    if exist is None:
                        self.left = Node(value, pos, index)
                    else:
                        self.left = exist
                elif self.match.index(pos) == 1:
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

    def maximum_patch(self, node):
        # print("---------------------------------------")
        # print("Node Pos: ", node.pos, " path_sum: ", node.path_sum, "value", node.value)
        # print("Part Pos: ", self.pos, " path_sum: ", self.path_sum, "value", self.value)
        if node.path_sum > self.path_sum:
            # print("new value")
            self.path_sum = node.path_sum + int(self.value)
            self.path_dir = node
            if Node.botton_max_value <= self.path_sum:
                Node.botton_max_value = self.path_sum
                Node.botton_max_node = self
        elif self.path_sum == 0:
            # print("start")
            self.path_sum = int(self.value) + int(Node.top_node.value)
            self.path_dir = Node.top_node
        elif node.path_sum + int(self.value) > self.path_sum:
            # print("new value 2")
            self.path_sum = node.path_sum + int(self.value)
            self.path_dir = node
            if Node.botton_max_value <= self.path_sum:
                Node.botton_max_value = self.path_sum
                Node.botton_max_node = self
                # print("New  Pos: ", self.pos, " path_sum: ", self.path_sum, "value", self.value)

    def loop_pos1(self):
        pos_number = 0
        for key, value in Node.exist.items():
            a = value
            if a is None:
                break
            else:
                if a.left is not None:
                    a.left.maximum_patch(a)
                if a.right is not None:
                    a.right.maximum_patch(a)
            pos_number += 1

    def loop_pos_(self):
        pos_number = 0
        while True:
            a = self.childe_pos(pos_number)
            if a is None:
                break
            else:
                if a.left is not None:
                    a.left.maximum_patch(a)
                if a.right is not None:
                    a.right.maximum_patch(a)
            pos_number += 1

    def childe_pos_(self, pos):
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

    def follow_node(self):
        print(self.value, end="+")
        if self.path_dir is not None:
            self.path_dir.follow_node()
        else:
            print("0")


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
    next_node.loop_pos()
    Node.botton_max_node.follow_node()
