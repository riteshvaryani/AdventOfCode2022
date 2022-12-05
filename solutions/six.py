import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_5_6.txt')

    with open(abs_file_path) as f:
        scores = 0
        counts=0
        group = []
        for i in f:
            i = i.strip()
            if counts == 3:
                common = group[0].intersection(group[1]).intersection(group[2])
                if list(common)[0].isupper():
                    scores += ord(list(common)[0]) - 64 + 26
                else:
                    scores += ord(list(common)[0]) - 96
                group=[]
                counts = 0

            group.append(set(i))
            counts += 1
        if counts == 3:
            common = group[0].intersection(group[1]).intersection(group[2])
            if list(common)[0].isupper():
                scores += ord(list(common)[0]) - 64 + 26
            else:
                scores += ord(list(common)[0]) - 96

    print(scores)

