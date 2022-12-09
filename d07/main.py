import pathlib


class Node():
    "Node in the file tree"
    def __init__(self, name, parent=None) -> None:
        self.children_dir = {}
        self.size = 0
        self.name = name
        self.parent = parent
        self.children_files = []


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        commands = [line.strip() for line in fd.readlines()]

    root_node = build_tree(commands)

    compute_dir_sizes(root_node)
    
    pretty_print_tree(root_node)

    sum_dirsizes = sum_of_dirsizes(root_node, at_most=100000)
    print("Sum of dirsizes at most 100000 in size =", sum_dirsizes)

    dir_to_delete = smallest_deletable_folder(root_node)
    print("Directory to delete has size:", dir_to_delete)


def smallest_deletable_folder(node):
    available_space = 70000000 - node.size
    threshold = 30000000
    space_to_free = threshold - available_space
    sizes = find_folder_sizes(node)
    sizes.sort()
    for size in sizes:
        if size >= space_to_free:
            return size


def find_folder_sizes(node):
    sizes = [node.size]
    for child in node.children_dir:
        sizes.extend(find_folder_sizes(node.children_dir[child]))
    return sizes


def sum_of_dirsizes(node, at_most):
    total_size = 0
    for child in node.children_dir:
        total_size += sum_of_dirsizes(node.children_dir[child], at_most)
        if node.children_dir[child].size <= at_most:
            total_size += node.children_dir[child].size
    return total_size


def compute_dir_sizes(node):
    size = 0
    for child in node.children_dir:
        size += compute_dir_sizes(node.children_dir[child])
    size += sum(node.children_files)
    node.size = size
    return size


def build_tree(commands):
    root_node = Node(name="/")
    for command in commands:
        if command[:4] == '$ cd':
            dest = command.split()[-1]
            if dest == "/":
                curr_node = root_node
            elif dest == '..':
                curr_node = curr_node.parent
            elif dest in curr_node.children_dir:
                curr_node = curr_node.children_dir[dest]
            else:
                curr_node.children_dir[dest] = Node(name=dest, parent=curr_node)
                curr_node = curr_node.children_dir[dest]
        elif command[:4] == '$ ls':
            pass
        elif command[:3] == 'dir':
            dir_name = command.split()[-1]
            if not dir_name in curr_node.children_dir:
                curr_node.children_dir[dir_name] = Node(name=dir_name, parent=curr_node)
        else:
            file_size = int(command.split()[0])
            curr_node.children_files.append(file_size)

    return root_node


def pretty_print_tree(node, indent = 0):
    print("  "*indent, node.name, ":", node.size)
    for child in node.children_dir:
        pretty_print_tree(node.children_dir[child], indent+2)


if __name__ == "__main__":
    main()
