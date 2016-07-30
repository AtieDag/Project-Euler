# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.


class Node:
    botton_max_node = None
    botton_max_value = 0
    exist = {}

    @classmethod
    def set_children(cls):
        for key, node in cls.exist.items():
            if node.match[0] in Node.exist:
                left = Node.exist[node.match[0]]
                node.left = left
            if node.match[1] in Node.exist:
                right = Node.exist[node.match[1]]
                node.right = right

    def __init__(self, value=0, pos=0, index=1):
        self.left = None
        self.right = None
        self.pos = pos
        self.match = [index, index + 1]
        self.value = value
        self.path_sum = 0
        self.path_dir = None
        Node.exist[pos] = self

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
            self.path_sum = int(self.value) + int(Node.exist[0].value)
            self.path_dir = Node.exist[0]
        elif node.path_sum + int(self.value) > self.path_sum:
            # print("new value 2")
            self.path_sum = node.path_sum + int(self.value)
            self.path_dir = node
            if Node.botton_max_value <= self.path_sum:
                Node.botton_max_value = self.path_sum
                Node.botton_max_node = self
                # print("New  Pos: ", self.pos, " path_sum: ", self.path_sum, "value", self.value)

    def follow_node(self):
        print(int(self.value), end="+")
        if self.path_dir is not None:
            self.path_dir.follow_node()
        else:
            print("0")


def loop_pos():
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


def load_file(file_name):
    with open(file_name) as file:
        pos = 0
        for index, line in enumerate(file):
            for k, value in enumerate(line.split()):
                Node(int(value), pos, pos + index + 1)
                pos += 1


if __name__ == '__main__':
    load_file('Problem67.txt')
    Node.set_children()
    loop_pos()
    Node.botton_max_node.follow_node()
