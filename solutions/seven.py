import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_7_8.txt')
    overlaps = 0
    with open(abs_file_path) as f:
         for i in f:
            i = i.strip()
            elves = i.split(',')
            elf1 = list(map(lambda x: int(x), elves[0].split('-')))
            elf2 = list(map(lambda x: int(x), elves[1].split('-')))

            if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
                overlaps+=1

    print(overlaps)

