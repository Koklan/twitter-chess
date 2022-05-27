import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor

global characters, pieces
characters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pieces = []
fields = []

class Field:
        def __init__(self,col,row,position,ocupation):
                self.col = col
                self.row = row
                self.position = position
                self.ocupation = ocupation
                fields.append(self)
                

        def posData(self):
                return(tuple(self.position))

class Chesspiece:
        def __init__(self, color, piece,position,col,row):
                self.color = color
                self.piece = piece
                self.position = position
                self.col = col
                self.row = row
                pieces.append(self)
                

        def position(self):
                return posData(self.position)

               
        def move(self, col, row):
                end_pos = globals()[col + str(row)]
                act_pos = globals()[self.col + str(self.row)]
                global col_moved
                global row_moved
                col_moved = []
                row_moved = []
                if characters.index(col) > characters.index(self.col):
                        diference_col = characters.index(col) - characters.index(self.col)
                        for i in range (characters.index(self.col) + 1, characters.index(self.col) + diference_col):
                                col_moved.append(characters[i])
                if characters.index(self.col) > characters.index(col):
                        diference_col = characters.index(self.col) - characters.index(col)
                        for i in range (characters.index(self.col) - diference_col + 1, characters.index(self.col)):
                                col_moved.append(characters[i])
                if row > self.row:
                        diference_row = row - self.row
                        for i in range (self.row+1,self.row + diference_row+1):
                                        row_moved.append(i)
                if self.row > row:
                        diference_row = self.row - row
                        for i in range (self.row - diference_row+1,self.row):
                                        row_moved.append(i)
                                        

                                
                if self.piece is 'pawn' and self.color is 'black' and end_pos.occupation is False:
                        if row is self.row - 1 and col==self.col:
                                act_pos.occupation = False
                                self.position = end_pos.pos_data()
                                self.col = col
                                self.row = row
                                end_pos.occupation = True

                        else:
                                print('invalid move')
                elif self.piece is 'pawn' and self.color is 'red' and end_pos.occupation is False:
                        if row is self.row + 1 and col==self.col:
                                act_pos.occupation = False
                                self.position = end_pos.pos_data()
                                self.col = col
                                self.row = row
                                end_pos.occupation = True
                        
                        else:
                                print('invalid move')

                elif self.piece is 'rook':
                        free = True
                        for x in range (0, len(row_moved)):
                                rows = row_moved[x]
                                mov_field = globals()[self.col + str(rows)]
                                if mov_field.occupation is True:
                                    free = False
                        for x in  range (0, len(col_moved)):
                                cols = col_moved[x]
                                mov_field = globals()[cols + str(self.row)]
                                if mov_field.occupation is True:
                                    free = False 
                        if row==self.row or col==self.col and free is True:
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
                        print(str(act_row)+","+str(act_new_row))
                        print(str(act_col)+","+str(act_new_col))
                        if (act_row==act_new_row+1 and act_col==act_new_col+2) or (act_row==act_new_row-1 and act_col==act_new_col-2) or (act_row==act_new_row+1 and act_col==act_new_col-2)or (act_row==act_new_row-1 and act_col==act_new_col+2):
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


for i in range (0,8):
        for x in range (0,8):
                globals()[characters[i] + '%s' % (8 - x)]= Field(characters[i], (8 - x), (70 + i * 120, 70 + x * 120), False)





chessboard = Image.open('chessboard.png')
black_knight = Image.open('black_knight_og.png').convert('RGBA')
black_knight = black_knight.resize((100,100))
black_knight.save("black_knight.png")
black_knight2 = black_knight.copy()
black_knightc= black_knight.copy()
black_knight = Chesspiece('black','knight', B8.pos_data(), 'B', 8)
black_knight2 = Chesspiece('black','knight', G8.pos_data(), 'G', 8)
red_knight = Image.open('red_knight_og.png').convert('RGBA')
red_knight = red_knight.resize((100,100))
red_knight.save("red_knight.png")
red_knightc= red_knight.copy()
red_knight2 = red_knight.copy()
red_knight = Chesspiece('red','knight', B1.pos_data(), 'B', 1)
red_knight2 = Chesspiece('red','knight', G1.pos_data(), 'G', 1)
black_rook = Image.open('black_rook_og.png').convert('RGBA') 
black_rook = black_rook.resize((100,100))
black_rook.save("black_rook.png")
black_rookc= black_rook.copy()
black_rook2 = black_rook.copy()
black_rook = Chesspiece('black','rook', A8.pos_data(), 'A', 8)
black_rook2 = Chesspiece('black','rook', H8.pos_data(), 'H', 8)
red_rook = Image.open('red_rook_og.png').convert('RGBA')
red_rook.save("red_rook.png")
red_rook = red_rook.resize((100,100))
red_rookc= red_rook.copy()
red_rook2= red_rook.copy()
red_rook = Chesspiece('red','rook', A1.pos_data(), 'A', 1)
red_rook2 = Chesspiece('red','rook', H1.pos_data(), 'H', 1)
black_queen = Image.open('black_queen_og.png').convert('RGBA')
black_queen = black_queen.resize((100,100))
black_queen.save("black_queen.png")
black_queenc= black_queen.copy()
black_queen = Chesspiece('black','queen', D8.pos_data(), 'D', 8)
red_queen = Image.open('red_queen_og.png').convert('RGBA')
red_queen = red_queen.resize((100,100))
red_queen.save("red_queen.png")
red_queenc= red_queen.copy()
red_queen = Chesspiece('red','queen', D1.pos_data(), 'D', 1)
black_king = Image.open('black_king_og.png').convert('RGBA')
black_king = black_king.resize((100,100))
black_king.save("black_king.png")
black_kingc= black_king.copy()
black_king = Chesspiece('black','king', E8.pos_data(), 'E', 8)
red_king = Image.open('red_king_og.png').convert('RGBA')
red_king = red_king.resize((100,100))
red_king.save("red_king.png")
red_kingc= red_king.copy()
red_king = Chesspiece('red','king', E1.pos_data(), 'E', 1)
black_bishop = Image.open('black_bishop_og.png').convert('RGBA')
black_bishop = black_bishop.resize((100,100))
black_bishop.save("black_bishop.png")
black_bishopc= black_bishop.copy()
black_bishop2 = black_bishop.copy()
black_bishop = Chesspiece('black','bishop', C8.pos_data(), 'C', 8)
black_bishop2 = Chesspiece('black','bishop', F8.pos_data(), 'F', 8)
red_bishop = Image.open('red_bishop_og.png').convert('RGBA')
red_bishop = red_bishop.resize((100,100))
red_bishop.save("red_bishop.png")
red_bishopc= red_bishop.copy()
red_bishop2= red_bishop.copy()
red_bishop = Chesspiece('red','bishop', C1.pos_data(), 'C', 1)
red_bishop2 = Chesspiece('red','bishop', F1.pos_data(), 'C', 1)
black_pawn = Image.open('black_pawn_og.png').convert('RGBA')
black_pawn = black_pawn.resize((100,100))
black_pawn.save("black_pawn.png")
black_pawnc= black_pawn.copy()
red_pawn = Image.open('red_pawn_og.png').convert('RGBA')
red_pawn = red_pawn.resize((100,100))
red_pawn.save("red_pawn.png")
red_pawnc= red_pawn.copy()
black_pawn1= Chesspiece('black','pawn', A7.pos_data(), 'A', 7)
black_pawn2= Chesspiece('black','pawn', B7.pos_data(), 'B', 7)
black_pawn3= Chesspiece('black','pawn', C7.pos_data(), 'C', 7)
black_pawn4= Chesspiece('black','pawn', D7.pos_data(), 'D', 7)
black_pawn5= Chesspiece('black','pawn', E7.pos_data(), 'E', 7)
black_pawn6= Chesspiece('black','pawn', F7.pos_data(), 'F', 7)
black_pawn7= Chesspiece('black','pawn', G7.pos_data(), 'G', 7)
black_pawn8= Chesspiece('black','pawn', H7.pos_data(), 'H', 7)
red_pawn1= Chesspiece('red','pawn', A2.pos_data(), 'A', 2)
red_pawn2= Chesspiece('red','pawn', B2.pos_data(), 'B', 2)
red_pawn3= Chesspiece('red','pawn', C2.pos_data(), 'C', 2)
red_pawn4= Chesspiece('red','pawn', D2.pos_data(), 'D', 2)
red_pawn5= Chesspiece('red','pawn', E2.pos_data(), 'E', 2)
red_pawn6= Chesspiece('red','pawn', F2.pos_data(), 'F', 2)
red_pawn7= Chesspiece('red','pawn', G2.pos_data(), 'G', 2)
red_pawn8= Chesspiece('red','pawn', H2.pos_data(), 'H', 2)

def begin():
    chessboard.paste(black_knightc, black_knight.position, black_knightc)
    chessboard.paste(black_knightc, black_knight2.position, black_knightc)
    chessboard.paste(red_knightc, red_knight.position, red_knightc)
    chessboard.paste(red_knightc, red_knight2.position, red_knightc)
    chessboard.paste(black_rookc, black_rook.position, black_rookc)
    chessboard.paste(black_rookc, black_rook2.position, black_rookc)
    chessboard.paste(red_rookc, red_rook.position, red_rookc)
    chessboard.paste(red_rookc, red_rook2.position, red_rookc)
    chessboard.paste(black_queenc, black_queen.position, black_queenc)
    chessboard.paste(red_queenc, red_queen.position, red_queenc)
    chessboard.paste(black_kingc, black_king.position, black_kingc)
    chessboard.paste(red_kingc, red_king.position, red_kingc)
    chessboard.paste(black_bishopc, black_bishop.position, black_bishopc)
    chessboard.paste(black_bishopc, black_bishop2.position, black_bishopc)
    chessboard.paste(red_bishopc, red_bishop.position, red_bishopc)
    chessboard.paste(red_bishopc, red_bishop2.position, red_bishopc)
    chessboard.paste(black_pawnc, black_pawn1.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn2.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn3.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn4.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn5.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn6.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn7.position, black_pawnc)
    chessboard.paste(black_pawnc, black_pawn8.position, black_pawnc)
    chessboard.paste(red_pawnc, red_pawn1.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn2.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn3.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn4.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn5.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn6.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn7.position, red_pawnc)
    chessboard.paste(red_pawnc, red_pawn8.position, red_pawnc)
    chessboard.save("begin_chessboard.png")
