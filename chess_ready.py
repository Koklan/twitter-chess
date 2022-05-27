import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor

global characters, pieces, fields
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pieces = []
fields = []


class Field:
    def __init__(self, col, row, position, occupation):
        self.col = col
        self.row = row
        self.position = position
        self.occupation = occupation
        fields.append(self)

    def pos_data(self):
        return (tuple(self.position))


class Chesspiece:
    def __init__(self, img, color, piece, position, col, row):
        self.img = Image
        self.color = color
        self.piece = piece
        self.position = position
        self.col = col
        self.row = row
        #Field(str(self.col)+str(self.row)).occupation = True
        pieces.append(self)

    def position(self):
        return pos_data(self.position)

    def move(self, col, row):
        end_pos = globals()[col + str(row)]
        act_pos = globals()[self.col + str(self.row)]
        global col_moved
        global row_moved
        col_moved = []
        row_moved = []
        if characters.index(col) > characters.index(self.col):
            difference_col = characters.index(col) - characters.index(self.col)
            for i in range(characters.index(self.col) + 1, characters.index(self.col) + difference_col):
                col_moved.append(characters[i])
        if characters.index(self.col) > characters.index(col):
            difference_col = characters.index(self.col) - characters.index(col)
            for i in range(characters.index(self.col) - difference_col + 1, characters.index(self.col)):
                col_moved.append(characters[i])
        if row > self.row:
            difference_row = row - self.row
            for i in range(self.row + 1, self.row + difference_row + 1):
                row_moved.append(i)
        if self.row > row:
            difference_row = self.row - row
            for i in range(self.row - difference_row + 1, self.row):
                row_moved.append(i)

        if self.piece is 'pawn' and self.color is 'black':
            if row is self.row - 1 and col == self.col and end_pos.occupation is False:
                act_pos.occupation = False
                self.position = end_pos.pos_data()
                self.col = col
                self.row = row
                end_pos.occupation = True

            else:
                print('invalid move')
        elif self.piece is 'pawn' and self.color is 'red':
            if row is self.row + 1 and col == self.col and end_pos.occupation is False:
                act_pos.occupation = False
                self.position = end_pos.pos_data()
                self.col = col
                self.row = row
                end_pos.occupation = True

            else:
                print('invalid move')

        elif self.piece is 'rook':
            free = True
            for x in range(0, len(row_moved)):
                rows = row_moved[x]
                mov_field = globals()[self.col + str(rows)]
                if mov_field.occupation is True:
                    free = False
            for x in range(0, len(col_moved)):
                cols = col_moved[x]
                mov_field = globals()[cols + str(self.row)]
                if mov_field.occupation is True:
                    free = False
            if row == self.row or col == self.col and free is True:
                act_pos = globals()[self.col + str(self.row)]
                act_pos.occupation = False
                self.position = end_pos.pos_data()
                self.col = col
                self.row = row
                end_pos.occupation = True

            else:
                print('invalid move')

        elif self.piece is 'knight':
            act_row = row
            act_new_row = self.row
            act_col = characters.index(col)
            act_new_col = characters.index(self.col)
            print(str(act_row) + "," + str(act_new_row))
            print(str(act_col) + "," + str(act_new_col))
            if (act_row == act_new_row + 1 and act_col == act_new_col + 2) or (
                    act_row == act_new_row - 1 and act_col == act_new_col - 2) or (
                    act_row == act_new_row + 1 and act_col == act_new_col - 2) or (
                    act_row == act_new_row - 1 and act_col == act_new_col + 2):
                act_pos = globals()[self.col + str(self.row)]
                act_pos.occupation = False
                self.position = end_pos.pos_data()
                self.col = col
                self.row = row
                end_pos.occupation = True

            else:
                print('invalid move')

        print(row_moved)
        print(col_moved)

#dynamic variable creation FIX!!!
for i in range(0, 8):
    for x in range(0, 8):
        globals()[characters[i] + '%s' % (8 - x)] = Field(characters[i], (8 - x), (70 + i * 120, 70 + x * 120), False)

chessboard = Image.open('chessboard.png')
black_knight_img = Image.open('black_knight.png').convert('RGBA')
red_knight_img = Image.open('red_knight.png').convert('RGBA')
black_rook_img = Image.open('black_rook.png').convert('RGBA')
red_rook_img = Image.open('red_rook.png').convert('RGBA')
black_queen_img = Image.open('black_queen.png').convert('RGBA')
red_queen_img = Image.open('red_queen.png').convert('RGBA')
black_king_img = Image.open('black_king.png').convert('RGBA')
red_king_img = Image.open('red_king.png').convert('RGBA')
black_bishop_img = Image.open('black_bishop.png').convert('RGBA')
red_bishop_img = Image.open('red_bishop.png').convert('RGBA')
black_pawn_img = Image.open('black_pawn.png').convert('RGBA')
red_pawn_img = Image.open('red_pawn.png').convert('RGBA')


def begin():
    global black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8, black_knight, black_knight2, black_bishop, black_bishop2, black_rook, black_rook2, black_king, black_queen
    global red_pawn1, red_pawn2, red_pawn3, red_pawn4, red_pawn5, red_pawn6, red_pawn7, red_pawn8, red_knight, red_knight2, red_bishop, red_bishop2, red_rook, red_rook2, red_king, red_queen
    black_pawn1 = Chesspiece(black_pawn_img, 'black', 'pawn', A7.pos_data(), 'A', 7)
    black_pawn2 = Chesspiece(black_pawn_img, 'black', 'pawn', B7.pos_data(), 'B', 7)
    black_pawn3 = Chesspiece(black_pawn_img, 'black', 'pawn', C7.pos_data(), 'C', 7)
    black_pawn4 = Chesspiece(black_pawn_img, 'black', 'pawn', D7.pos_data(), 'D', 7)
    black_pawn5 = Chesspiece(black_pawn_img, 'black', 'pawn', E7.pos_data(), 'E', 7)
    black_pawn6 = Chesspiece(black_pawn_img, 'black', 'pawn', F7.pos_data(), 'F', 7)
    black_pawn7 = Chesspiece(black_pawn_img, 'black', 'pawn', G7.pos_data(), 'G', 7)
    black_pawn8 = Chesspiece(black_pawn_img, 'black', 'pawn', H7.pos_data(), 'H', 7)
    black_knight = Chesspiece(black_knight_img, 'black', 'knight', B8.pos_data(), 'B', 8)
    black_knight2 = Chesspiece(black_knight_img, 'black', 'knight', G8.pos_data(), 'G', 8)
    black_bishop = Chesspiece(black_bishop_img, 'black', 'bishop', C8.pos_data(), 'C', 8)
    black_bishop2 = Chesspiece(black_bishop_img, 'black', 'bishop', F8.pos_data(), 'F', 8)
    black_rook = Chesspiece(black_rook_img, 'black', 'rook', A8.pos_data(), 'A', 8)
    black_rook2 = Chesspiece(black_rook_img, 'black', 'rook', H8.pos_data(), 'H', 8)
    black_king = Chesspiece(black_king_img, 'black', 'king', E8.pos_data(), 'E', 8)
    black_queen = Chesspiece(black_queen_img, 'black', 'queen', D8.pos_data(), 'D', 8)
    red_pawn1 = Chesspiece(red_pawn_img, 'red', 'pawn', A2.pos_data(), 'A', 2)
    red_pawn2 = Chesspiece(red_pawn_img, 'red', 'pawn', B2.pos_data(), 'B', 2)
    red_pawn3 = Chesspiece(red_pawn_img, 'red', 'pawn', C2.pos_data(), 'C', 2)
    red_pawn4 = Chesspiece(red_pawn_img, 'red', 'pawn', D2.pos_data(), 'D', 2)
    red_pawn5 = Chesspiece(red_pawn_img, 'red', 'pawn', E2.pos_data(), 'E', 2)
    red_pawn6 = Chesspiece(red_pawn_img, 'red', 'pawn', F2.pos_data(), 'F', 2)
    red_pawn7 = Chesspiece(red_pawn_img, 'red', 'pawn', G2.pos_data(), 'G', 2)
    red_pawn8 = Chesspiece(red_pawn_img, 'red', 'pawn', H2.pos_data(), 'H', 2)
    red_knight = Chesspiece(red_knight_img, 'red', 'knight', B1.pos_data(), 'B', 1)
    red_knight2 = Chesspiece(red_knight_img, 'red', 'knight', G1.pos_data(), 'G', 1)
    red_bishop = Chesspiece(red_bishop_img, 'red', 'bishop', C1.pos_data(), 'C', 1)
    red_bishop2 = Chesspiece(red_bishop_img, 'red', 'bishop', F1.pos_data(), 'C', 1)
    red_rook = Chesspiece(red_rook_img, 'red', 'rook', A1.pos_data(), 'A', 1)
    red_rook2 = Chesspiece(red_rook_img, 'red', 'rook', H1.pos_data(), 'H', 1)
    red_king = Chesspiece(red_king_img, 'red', 'king', E1.pos_data(), 'E', 1)
    red_queen = Chesspiece(red_queen_img, 'red', 'queen', D1.pos_data(), 'D', 1)
    # chessboard.open("begin_chessboard.png")


def nextMove():
    #should work? PIL broken??
    # for piece in pieces:
    #    chessboard.paste(piece.img, piece.position, piece.img)
    chessboard.paste(black_knight_img, black_knight.position, black_knight_img)
    chessboard.paste(black_knight_img, black_knight2.position, black_knight_img)
    chessboard.paste(red_knight_img, red_knight.position, red_knight_img)
    chessboard.paste(red_knight_img, red_knight2.position, red_knight_img)
    chessboard.paste(black_rook_img, black_rook.position, black_rook_img)
    chessboard.paste(black_rook_img, black_rook2.position, black_rook_img)
    chessboard.paste(red_rook_img, red_rook.position, red_rook_img)
    chessboard.paste(red_rook_img, red_rook2.position, red_rook_img)
    chessboard.paste(black_queen_img, black_queen.position, black_queen_img)
    chessboard.paste(red_queen_img, red_queen.position, red_queen_img)
    chessboard.paste(black_king_img, black_king.position, black_king_img)
    chessboard.paste(red_king_img, red_king.position, red_king_img)
    chessboard.paste(black_bishop_img, black_bishop.position, black_bishop_img)
    chessboard.paste(black_bishop_img, black_bishop2.position, black_bishop_img)
    chessboard.paste(red_bishop_img, red_bishop.position, red_bishop_img)
    chessboard.paste(red_bishop_img, red_bishop2.position, red_bishop_img)
    chessboard.paste(black_pawn_img, black_pawn1.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn2.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn3.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn4.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn5.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn6.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn7.position, black_pawn_img)
    chessboard.paste(black_pawn_img, black_pawn8.position, black_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn1.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn2.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn3.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn4.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn5.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn6.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn7.position, red_pawn_img)
    chessboard.paste(red_pawn_img, red_pawn8.position, red_pawn_img)
    chessboard.show()


begin()
black_pawn1.move("A",6)
black_rook.move("A",7)
print(black_rook.row)
print(black_rook.col)
print(black_pawn1.row)
print(black_pawn1.col)
nextMove()
