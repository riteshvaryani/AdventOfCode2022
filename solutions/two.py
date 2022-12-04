import os
import heapq
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_1_2.txt')

    curr_total=0
    h = []
    with open(abs_file_path) as f:
        for i in f:
            if i == '\n':
                heapq.heappush(h, curr_total)
                curr_total = 0
                if len(h) > 3:
                    heapq.heappop(h)
            else:
                curr_total += int(i)
        heapq.heappush(h, curr_total)
        if len(h) > 3:
            heapq.heappop(h)
    print(h)
    print(sum(h))