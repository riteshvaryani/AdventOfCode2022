import os
class Node:
    def __init__(self, name, size=0, dir=False):
        self.size = size
        self.dir = dir
        self.name = name
        self.parent = None
        self.mapped_files_and_dir = dict()

def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_13_14.txt')
    root = Node('/')
    current = root
    with open(abs_file_path) as f:
         lines = f.readlines()
    lineIndex = 0
    while lineIndex < len(lines):
        line = lines[lineIndex]
        operations = line.split()
        if line.startswith("$"):
            if operations[1] == 'cd':
                if operations[2] == '/':
                    current = root
                elif operations[2] == '..':
                    current = current.parent
                    if current.parent == None:
                        current = root
                else:
                    current = current.mapped_files_and_dir[operations[2]]
        else:
            if operations[0] == 'dir':
                if operations[1] in current.mapped_files_and_dir:
                    continue
                else:
                    new_node = Node(operations[1])
                    new_node.dir=True
                    new_node.parent= current
                    current.mapped_files_and_dir[operations[1]]=new_node
            else:
                if operations[1] in current.mapped_files_and_dir:
                    continue
                else:
                    new_node = Node(operations[1])
                    new_node.parent=current
                    new_node.size = int(operations[0])
                    current.mapped_files_and_dir[operations[1]] = new_node

        lineIndex+=1
    test = root
    x =0

    def traverse(node, depth, limit100k= False):
        nonlocal x
        size = 0
        indents = '>' * depth
        for i in node.mapped_files_and_dir:
            node1 = node.mapped_files_and_dir[i]
            #print(indents, node1.name, ' ', node1.dir, ' ', node1.size)
            this_node_size = node1.size
            if node1.dir:
                this_node_size = traverse(node1, depth + 1, limit100k)
            size += this_node_size
        node.size=size
        if limit100k and size <= 100000:
            x += size
        elif not limit100k:
            x+=size
        return size

    def find(node, atleast_needed):
        nonlocal min_size_seen
        size = node.size
        if len(str(size)) > 7:
            print(size , size >= atleast_needed)
        if size >= atleast_needed and size < min_size_seen:
            min_size_seen = size
        for i in node.mapped_files_and_dir:
            node1 = node.mapped_files_and_dir[i]
            #print(indents, node1.name, ' ', node1.dir, ' ', node1.size)
            this_node_size = node1.size
            if node1.dir:
                find(node1,atleast_needed)

    traverse(test,0, limit100k= True)
    print(x)
    x=0
    traverse(test, 0, limit100k=False)
    print(root.size)
    empty_space = 70000000 - root.size
    atleast_needed = 30000000 -  empty_space
    test = root
    min_size_seen = root.size
    print('atleast ', atleast_needed)
    find(test,atleast_needed)
    print(min_size_seen)
    #1642503

    '''
    for lines[]:
         if line.startswith("$"):
            operations = line.split()
            if operations[1] == 'cd':
            else:
    '''
