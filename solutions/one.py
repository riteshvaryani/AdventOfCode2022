import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_1_2.txt')

    curr_max=0
    max_till_now = curr_max
    with open(abs_file_path) as f:
        for i in f:
            if i == '\n':
                max_till_now = max(max_till_now, curr_max)
                curr_max=0
            else:
                curr_max += int(i)
        max_till_now = max(max_till_now, curr_max)
    print(max_till_now)