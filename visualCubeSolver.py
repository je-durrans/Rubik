from tkinter import *
from time import sleep

# ________________|
# |  0 |  1 |  2 |||
# |  3 |  4 |  5 |||
# |  6 |  7 |  8 |||
# _______RED______|________________|________________|________________|
# |  9 | 10 | 11 ||| 18 | 19 | 20 ||| 27 | 28 | 29 ||| 36 | 37 | 38 |||
# | 12 | 13 | 14 ||| 21 | 22 | 23 ||| 30 | 31 | 32 ||| 39 | 40 | 41 |||
# | 15 | 16 | 17 ||| 24 | 25 | 26 ||| 33 | 34 | 35 ||| 42 | 43 | 44 |||
# ______GREEN_____|_______BLUE_____|_____YELLOW_____|______WHITE_____|
# | 45 | 46 | 47 |||
# | 48 | 49 | 50 |||
# | 51 | 52 | 53 |||    TOP RED - FRONT GREEN - BOTTOM ORANGE
# _____ORANGE_____|     LEFT WHITE - RIGHT BLUE - BACK YELLOW

COLORS = ["R","G","B","Y","W","O"]
labels = []
class Cube():
    def __init__(self, colors = ""):
        self.colors = []
        self.solvestring=""
        if colors == "":
            colors = "R"*9+"G"*9+"B"*9+"Y"*9+"W"*9+"O"*9
        for i in colors:
            self.colors.append(i)
    def shorten(self):
        self.solvestring=self.solvestring.replace("U, U, U, U, ", "")
        self.solvestring=self.solvestring.replace("U, U, U, ", "Ui, ")
        self.solvestring=self.solvestring.replace("U, U, ", "U2, ")
        self.solvestring=self.solvestring.replace("R, Ri, ", "")
        self.solvestring=self.solvestring.replace("Ri, R, ", "")
        self.solvestring=self.solvestring.replace("MU, Di, ", "SB, ")
        self.solvestring=self.solvestring.replace("SB, U, ", "SC, ")
        self.solvestring=self.solvestring.replace("U, SB, ", "SC, ")
        self.solvestring=self.solvestring.replace("SB, SB, SB, SB, ", "")
    def U(self,s=True):
        c=self.colors
        c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],   c[9],c[10],c[11],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38] = \
        c[6],c[3],c[0],c[7],c[4],c[1],c[8],c[5],c[2],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38],  c[9],c[10],c[11]
        if s:
            self.solvestring+="U, "
        display(), sleep(0.1)
    def F(self,s=True):
        c=self.colors
        c[6],c[7],c[8],     c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],   c[18],c[21],c[24],  c[45],c[46],c[47],  c[38],c[41],c[44] = \
        c[44],c[41],c[38],  c[15],c[12],c[9],c[16],c[13],c[10],c[17],c[14],c[11],   c[6],c[7],c[8],     c[24],c[21],c[18],  c[45],c[46],c[47]
        if s:
            self.solvestring+="F, "
            display(), sleep(0.1)
    def R(self,s=True):
        c=self.colors
        c[2],c[5],c[8],     c[11],c[14],c[17],   c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26],  c[27],c[30],c[33], c[47],c[50],c[53] = \
        c[11],c[14],c[17],  c[47],c[50],c[53],   c[24],c[21],c[18],c[25],c[22],c[19],c[26],c[23],c[20],  c[8],c[5],c[2],    c[33],c[30],c[27]
        if s:
            self.solvestring+="R, "
        display(), sleep(0.1)
    def B(self,s=True):
        c=self.colors
        c[0],c[1],c[2],     c[20],c[23],c[26],  c[27],c[28],c[29],c[30],c[31],c[32],c[33],c[34],c[35],  c[36],c[39],c[42],  c[51],c[52],c[53] = \
        c[20],c[23],c[26],  c[53],c[52],c[51],  c[33],c[30],c[27],c[34],c[31],c[28],c[35],c[32],c[29],  c[2],c[1],c[0],     c[36],c[39],c[42]
        if s:
            self.solvestring+="B, "
        display(), sleep(0.1)
    def L(self,s=True):
        c=self.colors
        c[0],c[3],c[6],     c[9],c[12],c[15],   c[29],c[32],c[35],  c[36],c[37],c[38],c[39],c[40],c[41],c[42],c[43],c[44],  c[45],c[48],c[51]  = \
        c[35],c[32],c[29],  c[0],c[3],c[6],     c[51],c[48],c[45],  c[42],c[39],c[36],c[43],c[40],c[37],c[44],c[41],c[38],  c[9],c[12],c[15]
        if s:
            self.solvestring+="L, "
        display(), sleep(0.1)
    def D(self,s=True):
        c=self.colors
        c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[42],c[43],c[44],  c[45],c[46],c[47],c[48],c[49],c[50],c[51],c[52],c[53] = \
        c[42],c[43],c[44],  c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[51],c[48],c[45],c[52],c[49],c[46],c[53],c[50],c[47]
        if s:
            self.solvestring+="D, "
        display(), sleep(0.1)
    def Ui(self,s=True):
        c=self.colors
        c[6],c[3],c[0],c[7],c[4],c[1],c[8],c[5],c[2],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38],  c[9],c[10],c[11] = \
        c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],   c[9],c[10],c[11],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38]
        if s:
            self.solvestring+="Ui, "
        display(), sleep(0.1)
    def Fi(self,s=True):
        c=self.colors
        c[44],c[41],c[38],  c[15],c[12],c[9],c[16],c[13],c[10],c[17],c[14],c[11],   c[6],c[7],c[8],     c[24],c[21],c[18],  c[45],c[46],c[47] = \
        c[6],c[7],c[8],     c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],   c[18],c[21],c[24],  c[45],c[46],c[47],  c[38],c[41],c[44]        
        if s:
            self.solvestring+="Fi, "
        display(), sleep(0.1)
    def Ri(self,s=True):
        c=self.colors
        c[11],c[14],c[17],  c[47],c[50],c[53],   c[24],c[21],c[18],c[25],c[22],c[19],c[26],c[23],c[20],  c[8],c[5],c[2],    c[33],c[30],c[27] = \
        c[2],c[5],c[8],     c[11],c[14],c[17],   c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26],  c[27],c[30],c[33], c[47],c[50],c[53]
        if s:
            self.solvestring+="Ri, "
        display(), sleep(0.1)
    def Bi(self,s=True):
        c=self.colors
        c[20],c[23],c[26],  c[53],c[52],c[51],  c[33],c[30],c[27],c[34],c[31],c[28],c[35],c[32],c[29],  c[2],c[1],c[0],     c[36],c[39],c[42] = \
        c[0],c[1],c[2],     c[20],c[23],c[26],  c[27],c[28],c[29],c[30],c[31],c[32],c[33],c[34],c[35],  c[36],c[39],c[42],  c[51],c[52],c[53]
        if s:
            self.solvestring+="Bi, "
        display(), sleep(0.1)
    def Li(self,s=True):
        c=self.colors
        c[35],c[32],c[29],  c[0],c[3],c[6],     c[51],c[48],c[45],  c[42],c[39],c[36],c[43],c[40],c[37],c[44],c[41],c[38],  c[9],c[12],c[15] = \
        c[0],c[3],c[6],     c[9],c[12],c[15],   c[29],c[32],c[35],  c[36],c[37],c[38],c[39],c[40],c[41],c[42],c[43],c[44],  c[45],c[48],c[51]
        if s:
            self.solvestring+="Li, "
        display(), sleep(0.1)
    def Di(self,s=True):
        c=self.colors
        c[42],c[43],c[44],  c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[51],c[48],c[45],c[52],c[49],c[46],c[53],c[50],c[47] = \
        c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[42],c[43],c[44],  c[45],c[46],c[47],c[48],c[49],c[50],c[51],c[52],c[53]
        if s:
            self.solvestring+="Di, "
        display(), sleep(0.1)
    def MU(self):#TDi
        c=self.colors
        c[12],c[13],c[14],  c[21],c[22],c[23],  c[30],c[31],c[32],  c[39],c[40],c[41] = \
        c[21],c[22],c[23],  c[30],c[31],c[32],  c[39],c[40],c[41],  c[12],c[13],c[14]
        self.solvestring+="MU, "
        display(), sleep(0.1)
    def MF(self):#FBi
        c=self.colors
        c[3],c[4],c[5],     c[19],c[22],c[25],  c[50],c[49],c[48],  c[43],c[40],c[37] = \
        c[43],c[40],c[37],  c[3],c[4],c[5],     c[19],c[22],c[25],  c[50],c[49],c[48]
        self.solvestring+="MF, "
        display(), sleep(0.1)
    def MR(self):#RLi
        c=self.colors
        c[7],c[4],c[1],     c[16],c[13],c[10],  c[28],c[31],c[34],  c[52],c[49],c[46] = \
        c[16],c[13],c[10],  c[52],c[49],c[46],  c[7],c[4],c[1],  c[28],c[31],c[34]
        self.solvestring+="MR, "
        display(), sleep(0.1)
    def spinBottom(self):
        self.MU()
        self.Di()
        display(), sleep(0.1)
    def __str__(self):
        response = "\n| "
        for i in range(9):
            response += self.colors[i] + " | "
            if (i + 1) % 3 == 0:
                response += "\n| "
        for i in range(3):
            for j in range(1,5):
                for k in range(3):
                    response += self.colors[9 * j + 3 * i + k] + " | "
            response += "\n| "
        for i in range(9):
            response += self.colors[45 + i] + " | "
            if (i + 1) % 3 == 0:
                response += "\n| "
        response = response[:-2]

        return response

colors={
    "R":"red",
    "G":"green",
    "B":"blue",
    "W":"white",
    "O":"orange",
    "Y":"yellow"}        

c=Cube()
edgePairs=[(1,28),(3,37),(5,19),(7,10),
           (12,41),(14,21),(23,30),(32,39),
           (16,46),(25,50),(34,52),(43,48)]
cornerTriples=[(0,29,36),(2,20,27),(6,9,38),(8,11,18),
               (15,44,45),(17,24,47),(26,33,53),(35,42,51)]
from time import sleep
def solve(cube = c):
    solveDCross(cube)
    cube.solvestring+="\nDCrossSolved\n"
    sleep(1)
    solveDCorners(cube)
    cube.solvestring+="\nDCornersSolved\n"
    sleep(1)
    solveMEdges(cube)
    cube.solvestring+="\nMedgesSolved\n"
    sleep(1)
    solveUCross(cube)
    cube.solvestring+="\nUCrossSolved\n"
    sleep(1)
    solveUCorners(cube)
    cube.solvestring+="\nUCornersSolved\n"
    cube.solvestring+="\nCube Solved\n"
def solveDCross(cube):
    for i in range(4):
        if not (cube.colors[16] == cube.colors[13] and
                cube.colors[46] == cube.colors[49]):
            placeDEdge(cube)
        cube.spinBottom()
def findDEdge(cube):
    for a, b in edgePairs:
        if a in cube.colors[13] + cube.colors[49] and b in cube.colors[13] + cube.colors[49]:
            return a, b
def placeDEdge(cube):
    a,b=findDEdge(cube)
    if a == 12 or b == 12:
        cube.Li()
        cube.U()
        cube.L()
    elif a == 14 or b == 14:
        cube.R()
        cube.U()
        cube.Ri()
    elif a == 30 or b == 30:
        cube.Ri()
        cube.U()
        cube.R()
    elif a == 32 or b == 32:
        cube.L()
        cube.U()
        cube.Li()
    a,b=findDEdge(cube)
    if a == 16 or b == 16:
        for i in range(2):
            cube.F()
    elif a == 25 or b == 25:
        for i in range(2):
            cube.R()
    elif a == 34 or b == 34:
        for i in range(2):
            cube.B()
    elif a == 43 or b == 43:
        for i in range(2):
            cube.L()
    a,b=findDEdge(cube)
    while a in (1,3,5) or b in (1,3,5):
        cube.U()
        a,b=findDEdge(cube)
    if cube.colors[7] == cube.colors[49]:
        for i in range(2):
            cube.F()
    else:
        cube.F()
        cube.D()
        cube.Ri()
        cube.Di()
def findDEdge(cube):
    for a, b in edgePairs:
        if cube.colors[a] in cube.colors[13] + cube.colors[49] and cube.colors[b] in cube.colors[13] + cube.colors[49]:
            return a, b
def solveDCorners(cube):
    for i in range(4):
        if not (cube.colors[17] == cube.colors[13] and
                cube.colors[24] == cube.colors[22] and
                cube.colors[47] == cube.colors[49]):
            placeDCorner(cube)
        cube.spinBottom()
def placeDCorner(cube):
    a,b,c = findDCorner(cube)
    if a == 15 or b == 15 or c == 15:
        cube.Li()
        cube.U()
        cube.L()
    elif a == 17 or b == 17 or c == 17:
        cube.R()
        cube.U()
        cube.Ri()
    elif a == 26 or b == 26 or c == 26:
        cube.Ri()
        cube.U()
        cube.R()
    elif a == 35 or b == 35 or c == 35:
        cube.L()
        cube.U()
        cube.Li()
    a,b,c = findDCorner(cube)
    while a in (0,2,6) or b in (0,2,6) or c in (0,2,6):
        cube.U()
        a,b,c = findDCorner(cube)
    cube.R()
    cube.U()
    cube.Ri()
    while not (cube.colors[17] == cube.colors[13] and
               cube.colors[24] == cube.colors[22] and
               cube.colors[47] == cube.colors[49]):
        for i in range(2):
            cube.R()
            cube.U()
            cube.Ri()
            cube.Ui()
def findDCorner(cube):
    for a,b,c in cornerTriples:
        if cube.colors[a] in cube.colors[13] + cube.colors[22] + cube.colors[49] and \
           cube.colors[b] in cube.colors[13] + cube.colors[22] + cube.colors[49] and \
           cube.colors[c] in cube.colors[13] + cube.colors[22] + cube.colors[49]:
            return a,b,c
def solveMEdges(cube):
    for i in range(4):
        if not (cube.colors[14]==cube.colors[13] and cube.colors[21]==cube.colors[22]):
            a,b=findMEdge(cube)
            placeMEdge(cube,a,b)
        else:
            cube.spinBottom()
def findMEdge(cube):
    for a,b in edgePairs[:8]:
        if cube.colors[a] in cube.colors[13] + cube.colors[22] and cube.colors[b] in cube.colors[13] + cube.colors[22]:
            return a,b
def placeMEdge(cube,a,b):
    if a not in (1,3,5,7) and b not in (1,3,5,7):
        if a in (23,32) or b in (23,32):
            for i in range(2):
                cube.spinBottom()
        if a in (12,23) or b in (12,23):
            placeMLEdge(cube)
        else:
            placeMREdge(cube)
        if a in (23,32) or b in (23,32):
            for i in range(2):
                cube.spinBottom()
    for i in range(4):
        if not (cube.colors[10] == cube.colors[13] and cube.colors[7] == cube.colors[22]):
            cube.U()
        else:
            break
    if not (cube.colors[10] == cube.colors[13] and cube.colors[7] == cube.colors[22]):
        cube.spinBottom()
        for i in range(4):
            if not (cube.colors[10] == cube.colors[13] and cube.colors[7] == cube.colors[40]):
                cube.U()
            else:
                break
        placeMLEdge(cube)
    else:
        placeMREdge(cube)
        cube.spinBottom()
def placeMLEdge(cube):
    cube.Ui()
    cube.Li()
    cube.U()
    cube.L()
    cube.U()
    cube.F()
    cube.Ui()
    cube.Fi()
def placeMREdge(cube):
    cube.U()
    cube.R()
    cube.Ui()
    cube.Ri()
    cube.Ui()
    cube.Fi()
    cube.U()
    cube.F()
def solveUCross(cube):
    getUCross(cube)
    orientUCross(cube)
def getUCross(cube):
    while not (cube.colors[1] == cube.colors[3] == cube.colors[4] == cube.colors[5] == cube.colors[7]):
        if cube.colors[1] == cube.colors[4] == cube.colors[7]:
            cube.U()
        if cube.colors[3] == cube.colors[5] == cube.colors[5]:
            UCrossMix(cube)
        elif (cube.colors[1] == cube.colors[4] == cube.colors[3] or
              cube.colors[1] == cube.colors[4] == cube.colors[5] or
              cube.colors[3] == cube.colors[4] == cube.colors[7] or
              cube.colors[5] == cube.colors[4] == cube.colors[7]):
            while not(cube.colors[1] == cube.colors[4] == cube.colors[3]):
                cube.U()
            for i in range(2):
                UCrossMix(cube)
        else:
            UCrossMix(cube)
            for i in range(2):
                cube.U()
            for i in range(2):
                UCrossMix(cube)
def UCrossMix(cube):
    cube.F()
    cube.R()
    cube.U()
    cube.Ri()
    cube.Ui()
    cube.Fi()
def orientUCross(cube):
    solvedCross = False
    while not solvedCross:
        for i in range(4):
            if (cube.colors[10] == cube.colors[13] and
                cube.colors[19] == cube.colors[22] and
                cube.colors[28] == cube.colors[31] and
                cube.colors[37] == cube.colors[40]):
                solvedCross = True
                break
            else:
                cube.U()
        if solvedCross:
            break
        for i in range(4):
            if not cube.colors[10] == cube.colors[13]:
                cube.U()
            else:
                break
        if cube.colors[19] == cube.colors[22]:
            for i in range(2):
                cube.U()
                cube.spinBottom()
        elif cube.colors[37] == cube.colors[22]:
            cube.Ui()
            rearrangeCross(cube)
        else:
            cube.spinBottom()
def rearrangeCross(cube):
    cube.U()
    cube.R()
    cube.U()
    cube.Ri()
    cube.U()
    cube.R()
    cube.U()
    cube.U()
    cube.Ri()
#(0,29,36),(2,20,27),(6,9,38),(8,11,18)
def solveUCorners(cube):
    orientCorners(cube)
    turnCorners(cube)
def orientCorners(cube):
    while not(cube.colors[0] in cube.colors[4] + cube.colors[31] + cube.colors[40] and
              cube.colors[29] in cube.colors[4] + cube.colors[31] + cube.colors[40] and
              cube.colors[36] in cube.colors[4] + cube.colors[31] + cube.colors[40] and
              
              cube.colors[2] in cube.colors[4] + cube.colors[22] + cube.colors[31] and
              cube.colors[20] in cube.colors[4] + cube.colors[22] + cube.colors[31] and
              cube.colors[27] in cube.colors[4] + cube.colors[22] + cube.colors[31] and
              
              cube.colors[6] in cube.colors[4] + cube.colors[13] + cube.colors[40] and
              cube.colors[9] in cube.colors[4] + cube.colors[13] + cube.colors[40] and
              cube.colors[38] in cube.colors[4] + cube.colors[13] + cube.colors[40] and
              
              cube.colors[8] in cube.colors[4] + cube.colors[13] + cube.colors[22] and
              cube.colors[11] in cube.colors[4] + cube.colors[13] + cube.colors[22] and
              cube.colors[18] in cube.colors[4] + cube.colors[13] + cube.colors[22]):
        for i in range(4):
            if not(cube.colors[8] in cube.colors[4] + cube.colors[13] + cube.colors[22] and
                   cube.colors[11] in cube.colors[4] + cube.colors[13] + cube.colors[22] and
                   cube.colors[18] in cube.colors[4] + cube.colors[13] + cube.colors[22]):
                cube.U()
                cube.spinBottom()
            else:
                break
        mixCorners(cube)
def turnCorners(cube):
    for i in range(4):
        while not cube.colors[8] == cube.colors[4]:
            for j in range(2):
                cube.Ri()
                cube.Di()
                cube.R()
                cube.D()
        cube.U()
def mixCorners(cube):
    cube.U()
    cube.R()
    cube.Ui()
    cube.Li()
    cube.U()
    cube.Ri()
    cube.Ui()
    cube.L()
from random import randint
def scramble(cube):
    moves = ("U","Ui","F","Fi","R","Ri","B","Bi","L","Li","D","Di")
    for i in range(20):
        exec("cube."+moves[randint(0,11)]+"(s=False)")

##scramble(c)
##print("start")
##print(c)
##solve(c)
##print(c)
##c.shorten()
##print(c.solvestring)
##print(len(c.solvestring.split(", ")))
##print("end")

##n=100000
##total=0
##for i in range(n):
##    c=Cube()
##    scramble(c)
##    solve(c)
##    c.shorten()
##    total+=len(c.solvestring.replace("SC, ", "").split(","))
##total/=n
##print(total)

def display():#c, labels):
    for i in range(min([len(c.colors), len(labels)])):
        labels[i].config(bg=colors[c.colors[i]])
    global root
    root.update()

if __name__ == "__main__":

    root = Tk()
    frame = Frame(root)
    frame.grid()

    data = input("please enter the colours of the cube: ").upper()

    
    root.deiconify()
    
    if data:
        c = Cube()
    else:
        c = Cube()
        scramble(c)    

    for starty, startx in ((0,0), (3,0), (3,3), (3,6), (3,9), (6,0)):
        for y in range(3):
            for x in range(3):
                l=Button(frame, width=5, height=3)
                l.grid(row = starty+y, column=startx+x)
                labels.append(l)
    display(), sleep(0.1)
    print(c)
    solve(c)
    print(c)
    c.shorten()
    print(c.solvestring)
    input()
