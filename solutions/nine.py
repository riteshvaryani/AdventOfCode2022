import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_9_10.txt')
    stacks = [['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
    ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
    ['C', 'V', 'S', 'H'],
    ['H', 'F', 'G'],
    ['P', 'G', 'J', 'B', 'Z'],
    ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
    ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
    ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
    ['W', 'P', 'V', 'M', 'B', 'H']]
    with open(abs_file_path) as f:
         for i in f:
            i = i.strip()
            parts = i.split(' ')
            count = int(parts[1])
            from_stack = int(parts[3]) -1
            to_stack = int(parts[5]) -1
            while count >0:
                stacks[to_stack].append(stacks[from_stack].pop())
                count-=1

    res=''
    for i in stacks:
        res +=i[-1]

    print(res)