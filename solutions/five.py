import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_5_6.txt')

    with open(abs_file_path) as f:
        scores = 0
        for i in f:
            i = i.strip()
            first = i[0:len(i) // 2]
            second = i[len(i)//2:]
            first = set([i for i in first])
            second = set([i for i in second])
            common = second.intersection(first)
            if list(common)[0].isupper():
                scores += ord(list(common)[0])-64+26
            else:
                scores += ord(list(common)[0]) - 96


    print(scores)

