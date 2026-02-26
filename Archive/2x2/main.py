"""
0 = White
1 = Blue
2 = Orange
3 = Green
4 = Red
5 = Yellow

[0] = U
[1] = F
[2] = R
[3] = B
[4] = L
[5] = D

[][0] = TL
[][1] = TR
[][2] = BL
[][3] = BR
"""
sq = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]

def move_U():
    newU = [sq[0][2], sq[0][0], sq[0][3], sq[0][1]]
    newF = [sq[2][0], sq[2][1], sq[1][2], sq[1][3]]
    newR = [sq[3][0], sq[3][1], sq[2][2], sq[2][3]]
    newB = [sq[4][0], sq[4][1], sq[3][2], sq[3][3]]
    newL = [sq[1][0], sq[1][1], sq[4][2], sq[4][3]]
    newD = sq[5][:]
    return [newU, newF, newR, newB, newL, newD]

def move_D():
    newD = [sq[5][2], sq[5][0], sq[5][3], sq[5][1]]
    newF = [sq[1][0], sq[1][1], sq[4][2], sq[4][3]]
    newR = [sq[2][0], sq[2][1], sq[1][2], sq[1][3]]
    newB = [sq[3][0], sq[3][1], sq[2][2], sq[2][3]]
    newL = [sq[4][0], sq[4][1], sq[3][2], sq[3][3]]
    newU = sq[0][:]
    return [newU, newF, newR, newB, newL, newD]

def move_L():
    newU = [sq[3][1], sq[0][1], sq[3][3], sq[0][3]]
    newF = [sq[1][0], sq[1][1], sq[0][0], sq[0][2]]
    newR = sq[2][:]
    newB = [sq[5][0], sq[3][0], sq[5][2], sq[3][2]]
    newL = [sq[4][3], sq[4][0], sq[4][1], sq[4][2]]
    newD = [sq[1][2], sq[5][1], sq[1][0], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def move_R():
    newU = [sq[0][0], sq[1][1], sq[0][2], sq[1][3]]
    newF = [sq[1][0], sq[5][1], sq[1][2], sq[5][3]]
    newR = [sq[2][1], sq[2][3], sq[2][0], sq[2][2]]
    newB = [sq[0][1], sq[3][1], sq[0][3], sq[3][3]]
    newL = sq[4][:]
    newD = [sq[5][0], sq[3][0], sq[5][2], sq[3][2]]
    return [newU, newF, newR, newB, newL, newD]

def move_F():
    newU = [sq[0][0], sq[0][1], sq[4][3], sq[4][1]]
    newF = [sq[1][2], sq[1][0], sq[1][3], sq[1][1]]
    newR = [sq[2][0], sq[0][3], sq[2][2], sq[0][2]]
    newB = sq[3][:]
    newL = [sq[4][0], sq[5][0], sq[4][2], sq[5][2]]
    newD = [sq[2][1], sq[2][3], sq[5][2], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def move_B():
    newU = [sq[2][0], sq[2][2], sq[0][2], sq[0][3]]
    newF = sq[1][:]
    newR = [sq[5][1], sq[5][3], sq[2][2], sq[2][3]]
    newB = [sq[3][2], sq[3][0], sq[3][3], sq[3][1]]
    newL = [sq[0][0], sq[0][1], sq[4][2], sq[4][3]]
    newD = [sq[4][0], sq[4][1], sq[5][2], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def move_Ux():
    newU = [sq[0][1], sq[0][3], sq[0][0], sq[0][2]]
    newF = [sq[4][0], sq[4][1], sq[1][2], sq[1][3]]
    newR = [sq[1][0], sq[1][1], sq[2][2], sq[2][3]]
    newB = [sq[2][0], sq[2][1], sq[3][2], sq[3][3]]
    newL = [sq[3][0], sq[3][1], sq[4][2], sq[4][3]]
    newD = sq[5][:]
    return [newU, newF, newR, newB, newL, newD]

def move_Dx():
    newD = [sq[5][1], sq[5][3], sq[5][0], sq[5][2]]
    newF = [sq[1][0], sq[1][1], sq[2][2], sq[2][3]]
    newR = [sq[2][0], sq[2][1], sq[3][2], sq[3][3]]
    newB = [sq[3][0], sq[3][1], sq[4][2], sq[4][3]]
    newL = [sq[4][0], sq[4][1], sq[1][2], sq[1][3]]
    newU = sq[0][:]
    return [newU, newF, newR, newB, newL, newD]

def move_Lx():
    newU = [sq[1][0], sq[0][1], sq[1][2], sq[0][3]]
    newF = [sq[1][2], sq[1][3], sq[5][0], sq[5][2]]
    newR = sq[2][:]
    newB = [sq[3][1], sq[3][3], sq[0][0], sq[0][2]]
    newL = [sq[4][1], sq[4][2], sq[4][3], sq[4][0]]
    newD = [sq[3][0], sq[5][1], sq[3][2], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def move_Rx():
    newR = [sq[2][1], sq[2][3], sq[2][0], sq[2][2]]
    newU = [sq[0][0], sq[1][1], sq[0][2], sq[1][3]]
    newF = [sq[1][0], sq[5][1], sq[1][2], sq[5][3]]
    newD = [sq[5][0], sq[3][2], sq[5][2], sq[3][0]]
    newB = [sq[3][3], sq[0][1], sq[3][1], sq[0][3]]
    newL = sq[4][:]
    return [newU, newF, newR, newB, newL, newD]

def move_Fx():
    newU = [sq[0][0], sq[0][1], sq[1][2], sq[1][0]]
    newF = [sq[1][1], sq[1][3], sq[1][0], sq[1][2]]
    newR = [sq[2][0], sq[5][0], sq[2][2], sq[5][2]]
    newB = sq[3][:]
    newL = [sq[4][0], sq[0][2], sq[4][2], sq[0][3]]
    newD = [sq[4][1], sq[4][3], sq[5][2], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def move_Bx():
    newU = [sq[4][0], sq[4][2], sq[0][2], sq[0][3]]
    newF = sq[1][:]
    newR = [sq[2][0], sq[2][1], sq[0][1], sq[0][3]]
    newB = [sq[3][1], sq[3][3], sq[3][0], sq[3][2]]
    newL = [sq[5][1], sq[5][3], sq[4][2], sq[4][3]]
    newD = [sq[2][0], sq[2][2], sq[5][2], sq[5][3]]
    return [newU, newF, newR, newB, newL, newD]

def print_cube(sq):
    colours = ['W', 'B', 'O', 'G', 'R', 'Y']  # Colour initials

    # Convert each face to initials
    faces = [[colours[sticker] for sticker in face] for face in sq]

    def row(a, b):  # Return a row of two stickers
        return f"{a} {b}"

    def pad(s):  # Center-align for U, D, B
        return f"     {s}"

    # Print Up face
    print(pad(row(faces[0][0], faces[0][1])))
    print(pad(row(faces[0][2], faces[0][3])))

    # Print Left, Front, Right faces (tighter spacing)
    print(f"{row(faces[4][0], faces[4][1])}  {row(faces[1][0], faces[1][1])}  {row(faces[2][0], faces[2][1])}")
    print(f"{row(faces[4][2], faces[4][3])}  {row(faces[1][2], faces[1][3])}  {row(faces[2][2], faces[2][3])}")

    # Print Down face
    print(pad(row(faces[5][0], faces[5][1])))
    print(pad(row(faces[5][2], faces[5][3])))

    # Print Back face
    print(pad(row(faces[3][0], faces[3][1])))
    print(pad(row(faces[3][2], faces[3][3])))

def apply_move(sq, move):
        if move == "U":
            return move_U()
        elif move == "Ux":
            return move_Ux()
        elif move == "D":
            return move_D()
        elif move == "Dx":
            return move_Dx()
        elif move == "F":
            return move_F()
        elif move == "Fx":
            return move_Fx()
        elif move == "B":
            return move_B()
        elif move == "Bx":
            return move_Bx()
        elif move == "L":
            return move_L()
        elif move == "Lx":
            return move_Lx()
        elif move == "R":
            return move_R()
        elif move == "Rx":
            return move_Rx()
        else:
            raise ValueError(f"Invalid move: {move}")

while True:
    print_cube(sq)
    sq = apply_move(sq, input("Next Move: "))