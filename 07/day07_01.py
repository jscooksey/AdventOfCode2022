# Imports
from anytree import Node, RenderTree, Resolver, search


# Function definition
def tally(node: Node):
    add_size = node.size
    for folder in node.ancestors:
        folder.size = folder.size + add_size


# Read all lines
with open("input.txt") as f:
    lines = f.read().splitlines()

# Setup global variables
root = Node("root", folder=True, size=0)
r = Resolver()
node_current = root

# Work through all lines
for line in lines:

    # If its a new file
    if line[0].isdigit():
        val = line.split()
        size = int(val[0])
        name = val[1]
        file = Node(name, parent=node_current, folder=False, size=size)
        tally(file)

    # If its a new folder
    if line.startswith("dir "):
        path = line[4:]
        Node(path, parent=node_current, folder=True, size=0)

    # If its a command
    if line.startswith("$ cd "):
        path = line[5:]
        if path == "/":
            node_current = root
        elif path == "..":
            node_current = node_current.parent
        else:
            node_current = r.get(node_current, path=path)


# Get all the large folders and calculate total folder size
large_folders = search.findall(root, filter_=lambda node: node.size >= 100000 and node.folder)

total = 0

for folder in large_folders[1:]:
    total = total + folder.size

print(f"The answer is {total}")

# Show the tree
# print(RenderTree(root))
