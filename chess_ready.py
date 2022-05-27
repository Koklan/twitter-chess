import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor
import string

global characters, pieces, fields
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pieces = []
# fields = ["A8", "A7", "A6", "A5", "A4", "A3", "A2", "A1", "B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1", "C8", "C7",
#          "C6", "C5", "C4", "C3", "C2", "C1", "D8", "D7", "D6", "D5", "D4", "D3", "D2", "D1", "E8", "E7", "E6", "E5",
#          "E4", "E3", "E2", "E1", "F8", "F7", "F6", "F5", "F4", "F3", "F2", "F1", "G8", "G7", "G6", "G5", "G4", "G3",
#          "G2", "G1", "H8", "H7", "H6", "H5", "H4", "H3", "H2", "H1"]

fields = []


class Field:
# only position will be given (ex. A8), pixel position calculation function, col and row separation functions will
# be here, occupation default as false
    def __init__(self, name, occupation = None):
        self.occupation = occupation
        self.name = name
        if occupation != None:
            fields.append(self)

    def occupation_change(self, occupation):
        if occupation != None:
            self.occupation = occupation
            fields.append(self)
        elif occupation == None:
            fields.remove(self)
            del self

    def col(self):
        return str(list(self.name)[0])

    def row(self):
        return int(list(self.name)[1])
    
    #returns pixel position for chesspiece icon pasting 
    def pos_data(self):
        return (70 + characters.index(self.col()) * 120, 70 + (8 - self.row()) * 120)

    def occupied(self, flag = None):
        for field in fields:
            if field.name == self.name:
                if flag == None:
                    return True
                elif flag == 'color':
                    return field.occupation
                else:
                    raise ValueError('Invalid flag')

            

chessboard = Image.open('images/chessboard.png')
black_knight_img = Image.open('images/black_knight.png').convert('RGBA')
red_knight_img = Image.open('images/red_knight.png').convert('RGBA')
black_rook_img = Image.open('images/black_rook.png').convert('RGBA')
red_rook_img = Image.open('images/red_rook.png').convert('RGBA')
black_queen_img = Image.open('images/black_queen.png').convert('RGBA')
red_queen_img = Image.open('images/red_queen.png').convert('RGBA')
black_king_img = Image.open('images/black_king.png').convert('RGBA')
red_king_img = Image.open('images/red_king.png').convert('RGBA')
black_bishop_img = Image.open('images/black_bishop.png').convert('RGBA')
red_bishop_img = Image.open('images/red_bishop.png').convert('RGBA')
black_pawn_img = Image.open('images/black_pawn.png').convert('RGBA')
red_pawn_img = Image.open('images/red_pawn.png').convert('RGBA')

class Chesspiece:
    def __init__(self, color, position, img):
        self.img = img
        self.color = color
        self.position = Field(position,color)
        pieces.append(self)

    def col(self):
        return self.position.col()

    def row(self):
        return self.position.row()

    def pos_data(self):
        return self.position.pos_data()

    def change_pos(self, pos):
        self.position.occupation_change(None)
        self.position = pos
        print("My new position is: " + pos.name)
        self.position.occupation_change(self.color)

    def moved_fields(self, end_pos, piece):
        # Moved fields detection starts here. Needed for collision detection for rook, bishop and queen
        moved_fields = []
        col_moved = []
        row_moved = []
        # print(end_pos)
        if characters.index(end_pos.col()) > characters.index(self.col()):
            for i in range(characters.index(self.col()) + 1,
                           characters.index(end_pos.col())):
                print(i)
                col_moved.append(characters[i])

        if characters.index(self.col()) > characters.index(end_pos.col()):
            for i in range(characters.index(end_pos.col()) + 1,
                           characters.index(self.col())):
                print(i)
                col_moved.append(characters[i])

        if end_pos.row() > self.row():
            for i in range(self.row() + 1, end_pos.row()):
                row_moved.append(i)

        if self.row() > end_pos.row():
            for i in range(end_pos.row() + 1, self.row()):
                row_moved.append(i)
        
        if piece == Rook:
            for i in range(0, len(row_moved)):
                rows = row_moved[x]
                moved_fields.append(Field(self.col() + str(rows)))
            for i in range(0, len(col_moved)):
                cols = col_moved[x]
                moved_fields.append(Field(cols + str(self.row())))
            return [moved_fields,col_moved,row_moved]

        if piece == Bishop:
            for i in range(0, len(col_moved)):
                moved_fields.append(Field(col_moved[i] + str(row_moved[i])))
            return [moved_fields,col_moved,row_moved]


        
class Pawn(Chesspiece):
    def __init__(self, color, position):
        #self.color = color
        #self.position = position
        #fields[self.position] = self.color
        #pieces.append(self)
        if color == 'black':
            img = black_pawn_img
            print(type(img))
        elif color == 'red':
            img = red_pawn_img
        Chesspiece.__init__(self, color, position, img)



    def move(self, end_pos):
        pos = Field(end_pos)
        if self.color is 'black':
            if pos.row() is self.row() - 1 and pos.col() == self.col() and not pos.occupied() or pos.row() == 5 and self.row() == 7 and not pos.ocuupied():
                if self.row() == 1:
                    print('promotion')
                else:
                    self.change_pos(pos)
            elif pos.row() == self.row() - 1 and (characters.index(self.col()) == characters.index(pos.col()) - 1 or characters.index(self.col()) == characters.index(pos.col()) + 1) and pos.occupied():
                if pos.occupied('color') != self.color:
                    print('capture')
                elif pos.occupied('color') == self.color:
                    print('invalid pawn move cause same color')

            else:
                print('pawn invalid move')
        elif self.color is 'red':
            if pos.row() is self.row() + 1 and pos.col() == self.col() and not pos.occupied() or pos.row() == 4 and self.row() == 2 and not pos.occupied():
                if self.row() == 8:
                    print('promotion')
                else:
                    
                    
                    self.change_pos(pos)
            elif pos.row() is self.row() + 1 and (characters.index(pos.col()) == characters.index(self.col()) + 1 or characters.index(pos.col()) == characters.index(self.col()) - 1) and pos.occupied():
                if pos.occupied('color') != self.color:
                    print('capture')
                elif pos.occupied('color') == self.color:
                    print('invalid pawn move cause same color')

            else:
                print('pawn invalid move')

    def promotion():
        pass


class Rook(Chesspiece):
    def __init__(self, color, position):
        #self.color = color
        #self.position = position
        #fields[self.position] = self.color
        #pieces.append(self)
        if color == 'black':
            img = black_rook_img
        elif color == 'red':
            img = red_rook_img
        Chesspiece.__init__(self, color, position, img)
    
    def moved_fields(self, end_pos):
        return Chesspiece.moved_fields(self, end_pos, type(self))

    def move(self, end_pos):
        pos = Field(end_pos)
        free = True
        moved_fields = self.moved_fields(pos)[0]
        for field in moved_fields:
            if field.occupied():
                free = false
                break
        if pos.row() == self.row() or pos.col() == self.col() and free:
            if pos.occupied():
                if pos.occupied('color') == self.color:
                    print('rook invalid move cause your color')
                elif pos.occupied('color') != self.color:
                    print('capture')
            else:
                self.change_pos(pos)

        else:
            print('rook invalid move')

class Knight(Chesspiece):
    def __init__(self, color, position):
        #self.color = color
        #self.position = position
        #fields[self.position] = self.color
        #pieces.append(self)
        if color == 'black':
            img = black_knight_img
        elif color == 'red':
            img = red_knight_img
        Chesspiece.__init__(self, color, position, img)


    def move(self, end_pos):
        pos = Field(end_pos)
        act_row = pos.row()
        act_new_row = self.row()
        act_col = characters.index(pos.col())
        act_new_col = characters.index(self.col())
        print(str(act_row) + "," + str(act_new_row))
        print(str(act_col) + "," + str(act_new_col))
        if pos.occupied:
            if pos.occupied('color') != self.color:
                print('capture')
            if pos.occupied('color') == self.color:
                print('invalid knight move cause same color')
        elif (act_row == act_new_row + 1 and act_col == act_new_col + 2) or (
                act_row == act_new_row - 1 and act_col == act_new_col - 2) or (
                act_row == act_new_row + 1 and act_col == act_new_col - 2) or (
                act_row == act_new_row - 1 and act_col == act_new_col + 2):
            self.change_pos(pos)
        else:
            print('invalid knight move')
        


class Bishop(Chesspiece):
    def __init__(self, color, position):
        #self.color = color
        #self.position = position
        #fields[self.position] = self.color
        #pieces.append(self)
        if color == 'black':
            img = black_bishop_img
        elif color == 'red':
            img = red_bishop_img
        Chesspiece.__init__(self, color, position, img)
    
    def moved_fields(self, end_pos):
        return Chesspiece.moved_fields(self, end_pos, type(self))

    def move(self, end_pos):
        pos = Field(end_pos)
        moved_fields = self.moved_fields(pos)[0]
        col_moved = self.moved_fields(pos)[1]
        row_moved = self.moved_fields(pos)[2]
        free = True
        if len(col_moved) == len(row_moved):
            for field in moved_fields:
                if field.occupied:
                    free = False
            if pos.occupied:
                if pos.occupied('color') == self.color:
                    print('rook invalid move cause same color')
                elif pos.occupied('color') != self.color:
                    print('capture')
            elif free:
                self.change_pos(pos)


        else:
            print('bishop invalid move')

class King(Chesspiece):
    def __init__(self, color, position):
        if color == 'black':
            img = black_king_img
        elif color == 'red':
            img = red_king_img
        Chesspiece.__init__(self, color, position, img)

    def move(self, end_pos):
        pos = Field(end_pos)
        if (abs(characters.index(pos.col()) - characters.index(self.col())) == 1 \
                or abs(pos.row() - self.row()) == 1) and not pos.occupied():
                self.change_pos(pos)

        else:
            print("king invalid move")

class Queen(Chesspiece):
    def __init__(self, color, position):
        #self.color = color
        #self.position = position
        #fields[self.position] = self.color
        #pieces.append(self)
        if color == 'black':
            img = black_queen_img
        elif color == 'red':
            img = red_queen_img
        Chesspiece.__init__(self, color, position, img)

    def moved_fields(self, end_pos):
        return Chesspiece.moved_fields(self, end_pos, type(self))

    def move(self, end_pos):
        pos = Field(end_pos)
        moved_fields = self.moved_fields(pos)[0]
        col_moved = self.moved_fields(pos)[1]
        row_moved = self.moved_fields(pos)[2]
        free = True
        if pos.col() == self.col() \
            or pos.row() == self.row() \
            or len(col_moved) == len(row_moved):
                for field in moved_fields:
                    if field.occupied():
                        free = False
                        break
                if pos.occupied():
                    if pos.occupied('color') == self.color:
                        print('invalid move cause color')
                    if pos.occupied('color') != self.color:
                        print('capture')
                elif free:
                    self.change_pos(pos)



# noinspection PyGlobalUndefined
def begin():
    global black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8, \
        black_knight, black_knight2, black_bishop, black_bishop2, black_rook, black_rook2, black_king, black_queen, \
        red_pawn1, red_pawn2, red_pawn3, red_pawn4, red_pawn5, red_pawn6, red_pawn7, red_pawn8, red_knight, red_knight2, \
        red_bishop, red_bishop2, red_rook, red_rook2, red_king, red_queen
    black_pawn1 = Pawn('black', "A7")
    black_pawn2 = Pawn('black', "B7")
    black_pawn3 = Pawn('black', "C7")
    black_pawn4 = Pawn('black', "D7")
    black_pawn5 = Pawn('black', "E7")
    black_pawn6 = Pawn('black', "F7")
    black_pawn7 = Pawn('black', "G7")
    black_pawn8 = Pawn('black', "H7")
    black_knight = Knight('black', "B8")
    black_knight2 = Knight('black', "G8")
    black_bishop = Bishop('black', "C8")
    black_bishop2 = Bishop('black', "F8")
    black_rook = Rook('black', "A8")
    black_rook2 = Rook('black', "H8")
    black_king = King('black', "E8")
    black_queen = King('black', "D8")       #queen
    red_pawn1 = Pawn('red', "A2")
    red_pawn2 = Pawn('red', "B2")
    red_pawn3 = Pawn('red', "C2")
    red_pawn4 = Pawn('red', "D2")
    red_pawn5 = Pawn('red', "E2")
    red_pawn6 = Pawn('red', "F2")
    red_pawn7 = Pawn('red', "G2")
    red_pawn8 = Pawn('red', "H2")
    red_knight = Knight('red', "B1")
    red_knight2 = Knight('red', "G1")
    red_bishop = Bishop('red', "C1")
    red_bishop2 = Bishop('red', "F1")
    red_rook = Rook('red', "A1")
    red_rook2 = Rook('red', "H1")
    red_king = King('red', "E1")        
    red_queen = King('red', "D1")       #queen
    # chessboard.open("begin_chessboard.png")

    
def next_move():
    for piece in pieces:
        chessboard.paste(piece.img,(piece.pos_data()[0],piece.pos_data()[1],piece.pos_data()[0]+100,piece.pos_data()[1]+100),piece.img)
    chessboard.show()


begin()
black_pawn1.move("A6")
black_rook.move("A7")
red_pawn4.move("D3")
red_pawn5.move("E3")
red_bishop.move("F4")
black_king.move("F8")
red_king.move("E2")
red_bishop.move("D2")


next_move()
