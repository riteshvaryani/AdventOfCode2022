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

    def calculate(opponent, increment):
        #C -> 67 lose + 1 = 68 %67 = 1 + 64+23 = 88 (X)
        mine = chr((ord(opponent)- 65 + increment) % 3 + 65 + 23)
        print(mine)
        return mine

    with open(abs_file_path) as f:
        for i in f:
            i = i.strip()
            play = i.split(' ')
            if play[1] == 'Y':
                points += draw
                if play[0] == rock.opponent:
                    mine = rock.me
                elif play[0] == paper.opponent:
                    mine = paper.me
                else:
                    mine = scissors.me
            else:
                increment = 2 if play[1] == 'X' else 1
                mine = calculate(play[0], increment)
                if play[1] == 'Z':
                    points += win
            if rock.me == mine:
                points += 1
            elif paper.me == mine:
                points+=2
            else:
                points+=3

    print(points)

