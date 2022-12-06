import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_11_12.txt')
    with open(abs_file_path) as f:
         stream  =f.readlines()[0]
         mapped = dict()
         for i,x in enumerate(stream):
             if x in mapped:
                 mapped[x] += 1
             else:
                 mapped[x] = 1
             if i > 13:
                 if mapped[stream[i-14]] == 1:
                     del mapped[stream[i-14]]
                 else:
                     mapped[stream[i-14]]-=1
                 if len(mapped) == 14:
                     print(i+1)
                     break