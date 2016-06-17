# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.


def load_file(file_name):
    b = []
    with open(file_name) as file:
        for index, line in enumerate(file):
            print(index)
            print(line)
    return b

if __name__ == '__main__':
    all_su = load_file('Problem18.txt')