class Node:
    def __init__(self, name, values=None):
        self.name = name
        self.values = values if values is not None else []
        self.children = {}
        self.size = 0

    def add_child(self, child_node):
        self.children[child_node.name] = child_node

    def get_size(self):
        if self.size > 0:
            return self.size
        total_size = sum(self.values)
        for child in self.children.values():
            total_size += child.get_size()
        self.size = total_size
        return self.size

    def __repr__(self):
        return f"Node(name={self.name}, values={self.values}, children={len(self.children)}, size = {self.size})"


def parse_file(filename):
    root = Node('/')
    directories = [root]

    current = root
    stack = [root]

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                if line.startswith("$ cd"):
                    dir = line.split()[2]
                    if dir == '..':
                        stack.pop(0)
                        current = stack[0]
                    elif dir == '/':
                        stack = [root]
                        current = root
                    else:
                        current = current.children[dir]
                        stack.insert(0, current)
                elif line.startswith("dir"):
                    dir = line.split()[1]
                    node = Node(dir)
                    directories.append(node)
                    current.add_child(node)
                elif line[0].isdigit():
                    size = line.split()[0]
                    current.values.append(int(size))

    root.get_size()
    return root, directories


def part1(root, directories):
    dirs = [node for node in directories if node.get_size() <= 100000]
    return sum(d.size for d in dirs)


def part2(root, directories):
    free_space = 70000000 - root.size
    space_to_free = 30000000 - free_space
    to_del = min([node for node in directories if node.get_size() >= space_to_free], key=lambda node: node.size)
    return to_del.size


# Example usage
filename = "../../input/2022/q07.txt"
root, directories = parse_file(filename)
# print(root)
print(directories)
print(part1(root, directories))
print(part2(root, directories))
