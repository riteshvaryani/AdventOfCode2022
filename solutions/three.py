import os
def execute(absolutepath:None):
    abs_file_path = os.path.join(absolutepath, 'inputs/input_3_4.txt')

    win = 6
    draw = 3
    loss = 0
    class Element:
        def __init__(self, name, opponent, me, points):
            self.name = name
            self.opponent = opponent
            self.me = me
            self.points = points
    '''
    me opponnet   diff
    2    1         1     --> win
    2    0         2     --> lose
    1    2         -1    --> lose
    1    0          1    --> win
    0    1         -1    --> lose
    0    2         -2    --> win
    '''
    rock = Element('Rock','A','X',1)
    paper = Element('Paper','B','Y',2)
    scissors = Element('Scissor','C','Z',3)
    points = 0

    def calculate(me, opponent):
        diff = ord(me) - ord(opponent)
        if me == opponent:
            return draw
        elif diff == 1 or diff == -2:
            return win
        else:
            return loss
    with open(abs_file_path) as f:
        for i in f:
            i = i.strip()
            play = i.split(' ')
            print(play, ' ', play[0], ' ',play[1], ' ',chr(ord(play[1])-23))
            result = calculate( chr(ord(play[1])-23), play[0])
            points += result
            if rock.me == play[1]:
                points += 1
            elif paper.me == play[1]:
                points+=2
            else:
                points+=3

    print(points)

