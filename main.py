import random

#Variables
piece_active = False
current_piece = 0

#Define piece types and their block positions
#1 = T piece
#2 = I piece
#3 = L piece
#4 = Mirrored L piece
#5 = Block Piece
#6 = S piece
#7 = Mirrored S piece
piece_types = {
    1: [(-1, 0), (0, 1), (1, 0)],
    2: [(0, 1), (0, -1), (0, -2)],
    3: [(0, 1), (1, 0), (2, 0)],
    4: [(0, 1), (-1, 0), (-2, 0)],
    5: [(1, 0), (0, 1), (1, 1)],
    6: [(0, -1), (1, 0), (1, 1)],
    7: [(0, -1), (-1, 0), (-1, 1)]
}

#Make the map
def make_map():
    rows = {}
    for i in range(20):
        rows[i] = []
    print(rows)
make_map()

def assign_piece():
    #Assign piece to the main point
    global current_piece
    current_piece = piece_types[random.randint(1, 7)]
    print(current_piece)
    assign_global_coords()

def assign_global_coords():
    print (current_piece)
    main_block_cords = {
    1: [5, 19],
    2: [5 + current_piece[0][0], 19 + current_piece[0][1]],
    3: [5 + current_piece[1][0], 19 + current_piece[1][1]],
    4: [5 + current_piece[2][0], 19 + current_piece[2][1]],
    }
    print(main_block_cords)

def main_frame_loop():
    if not piece_active:
        assign_piece()

main_frame_loop()
