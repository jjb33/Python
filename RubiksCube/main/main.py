import random as rand
import copy

blocks = ['y1', 'y2', 'y3', 'y4', 'o1', 'o2', 'o3', 'o4', 'r1', 'r2', 'r3', 'r4', 'g1', 'g2', 'g3', 'g4', 'b1', 'b2', 'b3', 'b4', 'w1', 'w2', 'w3', 'w4']
moves = ['x1', 'x1i', 'x2', 'x2i', 'y1', 'y1i', 'y2', 'y2i', 'z1', 'z1i', 'z2', 'z2i']
solved_sides = [['y1', 'y2', 'y3', 'y4'], ['o1', 'o2', 'o3', 'o4'], ['r1', 'r2', 'r3', 'r4'], ['g1', 'g2', 'g3', 'g4'], ['b1', 'b2', 'b3', 'b4'], ['w1', 'w2', 'w3', 'w4']]

cube = {}
side_number = 1
side_colors = []
while len(blocks) != 0:
    rand.shuffle(blocks)
    block = blocks.pop()
    side_colors.append(block)
    if len(side_colors) == 4:
        cube[side_number] = side_colors
        side_colors = []
        side_number += 1
cube_start = copy.deepcopy(cube)


#MOVING
moves_record = []

while True:
    print('Turns:', len(moves_record))
    #Pick a random move
    rand.shuffle(moves)
    current_move = moves[0]
    moves_record.append(current_move)

    if current_move == 'x1':
        pos1 = cube[6][3]
        pos2 = cube[6][1]
        cube[6][3], cube[6][1] = cube[3][0], cube[3][2]
        cube[3][0], cube[3][2] = cube[2][0], cube[2][2]
        cube[2][0], cube[2][2] = cube[1][0], cube[1][2]
        cube[1][0], cube[1][2] = pos1, pos2

    if current_move == 'x1i':
        pos1 = cube[6][1]
        pos2 = cube[6][3]
        cube[6][1], cube[6][3] = cube[3][2], cube[3][0]
        cube[3][2], cube[3][0] = cube[2][2], cube[2][0]
        cube[2][2], cube[2][0] = cube[1][2], cube[1][0]
        cube[1][2], cube[1][0] = pos1, pos2

    if current_move == 'x2':
        pos1 = cube[6][2]
        pos2 = cube[6][0]
        cube[6][2], cube[6][0] = cube[3][1], cube[3][3]
        cube[3][1], cube[3][3] = cube[2][1], cube[2][3]
        cube[2][1], cube[2][3] = cube[1][1], cube[1][3]
        cube[1][1], cube[1][3] = pos1, pos2

    if current_move == 'x2i':
        pos1 = cube[6][0]
        pos2 = cube[6][2]
        cube[6][0], cube[6][2] = cube[3][3], cube[3][1]
        cube[3][3], cube[3][1] = cube[2][3], cube[2][1]
        cube[2][3], cube[2][1] = cube[1][3], cube[1][1]
        cube[1][3], cube[1][1] = pos1, pos2

    if current_move == 'y1':
        pos1 = cube[6][0]
        pos2 = cube[6][1]
        cube[6][0], cube[6][1] = cube[5][0], cube[5][1]
        cube[5][0], cube[5][1] = cube[4][0], cube[4][1]
        cube[4][0], cube[4][1] = cube[2][0], cube[2][1]
        cube[2][0], cube[2][1] = pos1, pos2

    if current_move == 'y1i':
        pos1 = cube[6][1]
        pos2 = cube[6][0]
        cube[6][1], cube[6][0] = cube[5][1], cube[5][0]
        cube[5][1], cube[5][0] = cube[4][1], cube[4][0]
        cube[4][1], cube[4][0] = cube[2][1], cube[2][0]
        cube[2][1], cube[2][0] = pos1, pos2

    if current_move == 'y2':
        pos1 = cube[6][2]
        pos2 = cube[6][3]
        cube[6][2], cube[6][3] = cube[5][2], cube[5][3]
        cube[5][2], cube[5][3] = cube[4][2], cube[4][3]
        cube[4][2], cube[4][3] = cube[2][2], cube[2][3]
        cube[2][2], cube[2][3] = pos1, pos2

    if current_move == 'y2i':
        pos1 = cube[6][3]
        pos2 = cube[6][2]
        cube[6][3], cube[6][2] = cube[5][3], cube[5][2]
        cube[5][3], cube[5][2] = cube[4][3], cube[4][2]
        cube[4][3], cube[4][2] = cube[2][3], cube[2][2]
        cube[2][3], cube[2][2] = pos1, pos2

    if current_move == 'z1':
        side2_duplicate = cube[2].copy()
        cube[2][0] = side2_duplicate[1]
        cube[2][1] = side2_duplicate[3]
        cube[2][2] = side2_duplicate[0]
        cube[2][3] = side2_duplicate[2]

    if current_move == 'z1i':
        side2_duplicate = cube[2].copy()
        cube[2][0] = side2_duplicate[2]
        cube[2][1] = side2_duplicate[0]
        cube[2][2] = side2_duplicate[3]
        cube[2][3] = side2_duplicate[1]

    if current_move == 'z2':
        side6_duplicate = cube[6].copy()
        cube[6][0] = side6_duplicate[1]
        cube[6][1] = side6_duplicate[3]
        cube[6][2] = side6_duplicate[0]
        cube[6][3] = side6_duplicate[2]

    if current_move == 'z2i':
        side6_duplicate = cube[6].copy()
        cube[6][0] = side6_duplicate[2]
        cube[6][1] = side6_duplicate[0]
        cube[6][2] = side6_duplicate[3]
        cube[6][3] = side6_duplicate[1]

    if sorted(cube[1]) not in solved_sides:
        moves_record = []
        continue
    if sorted(cube[2]) not in solved_sides:
        moves_record = []
        continue
    if sorted(cube[3]) not in solved_sides:
        moves_record = []
        continue
    if sorted(cube[4]) not in solved_sides:
        moves_record = []
        continue
    if sorted(cube[5]) not in solved_sides:
        moves_record = []
        continue
    if sorted(cube[6]) not in solved_sides:
        moves_record = []
        continue
    else:
        break
    
        
print("It's a winning combination!:\n")
print(moves_record, '\n')
print('and the starting layout was:\n')
print(cube_start)

end = input('Hit anything to quit')
   

