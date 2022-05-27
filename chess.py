import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor


bcg = Image.new('RGBA', (1080,1080), 'white')
blc = Image.new('RGBA', (120,120),(0,132,180))

class Field:
        def __init__(self,col,row,position,ocupation):
                self.col = col
                self.row = row
                self.position = position
                self.ocupation = ocupation
                
for i in range (0,4):
	bcg.paste(blc,(180+i*240,60))
	bcg.paste(blc,(60+i*240,180))
	bcg.paste(blc,(180+i*240,300))
	bcg.paste(blc,(60+i*240,420))
	bcg.paste(blc,(180+i*240,540))
	bcg.paste(blc,(60+i*240,660))
	bcg.paste(blc,(180+i*240,780))
	bcg.paste(blc,(60+i*240,900))
d = ImageDraw.Draw(bcg)
font = ImageFont.truetype("MonoSerif-Regular.ttf",60)
d.text((100,10),'A','black',font)
lst=['A','B','C','D','E','F','G','H']
characters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range (1,9):
	d.text((i*120-20,10),lst[i-1],'black',font)
	d.text((i*120-20,1030),lst[i-1],'black',font)

cisla=['8','7','6','5','4','3','2','1']
for i in range (1,9):
	d.text((10,i*120-20),cisla[i-1],'black',font)
	d.text((1030,i*120-20),cisla[i-1],'black',font)
black_knight = Image.open('black_knight.png').convert('RGBA')
black_knight = black_knight.resize((100,100))
bk = black_knight.copy()


class Chesspiece:
        def __init__(self, color, piece,position,col,row):
                self.color = color
                self.piece = piece
                self.position = position
                self.col = col
                self.row = row
                
        def move(self, col, row):
                end_pos = globals()[col + str(row)]
                if self.piece is 'pawn':
                        if row is self.row + 1 and col==self.col:
                                bcg.paste(bk, box = end_pos.position, mask=bk)
                                end_pos.occupation = True
                        else:
                                print('invalid move')
        
                
for i in range (0,8):
        for x in range (0,8):
                globals()[characters[i] + '%s' % (8 - x)]= Field(characters[i], (8 - x), (70 + i * 120, 70 + x * 120), False)
                
				    
