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

def display():
    for i in range(54):
        labels[i].config(bg=colors[c.colors[i]])
    root.update()

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
        display()
    def F(self,s=True):
        c=self.colors
        c[6],c[7],c[8],     c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],   c[18],c[21],c[24],  c[45],c[46],c[47],  c[38],c[41],c[44] = \
        c[44],c[41],c[38],  c[15],c[12],c[9],c[16],c[13],c[10],c[17],c[14],c[11],   c[6],c[7],c[8],     c[24],c[21],c[18],  c[45],c[46],c[47]
        if s:
            self.solvestring+="F, "
            display()
    def R(self,s=True):
        c=self.colors
        c[2],c[5],c[8],     c[11],c[14],c[17],   c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26],  c[27],c[30],c[33], c[47],c[50],c[53] = \
        c[11],c[14],c[17],  c[47],c[50],c[53],   c[24],c[21],c[18],c[25],c[22],c[19],c[26],c[23],c[20],  c[8],c[5],c[2],    c[33],c[30],c[27]
        if s:
            self.solvestring+="R, "
        display()
    def B(self,s=True):
        c=self.colors
        c[0],c[1],c[2],     c[20],c[23],c[26],  c[27],c[28],c[29],c[30],c[31],c[32],c[33],c[34],c[35],  c[36],c[39],c[42],  c[51],c[52],c[53] = \
        c[20],c[23],c[26],  c[53],c[52],c[51],  c[33],c[30],c[27],c[34],c[31],c[28],c[35],c[32],c[29],  c[2],c[1],c[0],     c[36],c[39],c[42]
        if s:
            self.solvestring+="B, "
        display()
    def L(self,s=True):
        c=self.colors
        c[0],c[3],c[6],     c[9],c[12],c[15],   c[29],c[32],c[35],  c[36],c[37],c[38],c[39],c[40],c[41],c[42],c[43],c[44],  c[45],c[48],c[51]  = \
        c[35],c[32],c[29],  c[0],c[3],c[6],     c[51],c[48],c[45],  c[42],c[39],c[36],c[43],c[40],c[37],c[44],c[41],c[38],  c[9],c[12],c[15]
        if s:
            self.solvestring+="L, "
        display()
    def D(self,s=True):
        c=self.colors
        c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[42],c[43],c[44],  c[45],c[46],c[47],c[48],c[49],c[50],c[51],c[52],c[53] = \
        c[42],c[43],c[44],  c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[51],c[48],c[45],c[52],c[49],c[46],c[53],c[50],c[47]
        if s:
            self.solvestring+="D, "
        display()
    def Ui(self,s=True):
        c=self.colors
        c[6],c[3],c[0],c[7],c[4],c[1],c[8],c[5],c[2],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38],  c[9],c[10],c[11] = \
        c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],   c[9],c[10],c[11],   c[18],c[19],c[20],  c[27],c[28],c[29],  c[36],c[37],c[38]
        if s:
            self.solvestring+="Ui, "
        display()
    def Fi(self,s=True):
        c=self.colors
        c[44],c[41],c[38],  c[15],c[12],c[9],c[16],c[13],c[10],c[17],c[14],c[11],   c[6],c[7],c[8],     c[24],c[21],c[18],  c[45],c[46],c[47] = \
        c[6],c[7],c[8],     c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],   c[18],c[21],c[24],  c[45],c[46],c[47],  c[38],c[41],c[44]        
        if s:
            self.solvestring+="Fi, "
        display()
    def Ri(self,s=True):
        c=self.colors
        c[11],c[14],c[17],  c[47],c[50],c[53],   c[24],c[21],c[18],c[25],c[22],c[19],c[26],c[23],c[20],  c[8],c[5],c[2],    c[33],c[30],c[27] = \
        c[2],c[5],c[8],     c[11],c[14],c[17],   c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26],  c[27],c[30],c[33], c[47],c[50],c[53]
        if s:
            self.solvestring+="Ri, "
        display()
    def Bi(self,s=True):
        c=self.colors
        c[20],c[23],c[26],  c[53],c[52],c[51],  c[33],c[30],c[27],c[34],c[31],c[28],c[35],c[32],c[29],  c[2],c[1],c[0],     c[36],c[39],c[42] = \
        c[0],c[1],c[2],     c[20],c[23],c[26],  c[27],c[28],c[29],c[30],c[31],c[32],c[33],c[34],c[35],  c[36],c[39],c[42],  c[51],c[52],c[53]
        if s:
            self.solvestring+="Bi, "
        display()
    def Li(self,s=True):
        c=self.colors
        c[35],c[32],c[29],  c[0],c[3],c[6],     c[51],c[48],c[45],  c[42],c[39],c[36],c[43],c[40],c[37],c[44],c[41],c[38],  c[9],c[12],c[15] = \
        c[0],c[3],c[6],     c[9],c[12],c[15],   c[29],c[32],c[35],  c[36],c[37],c[38],c[39],c[40],c[41],c[42],c[43],c[44],  c[45],c[48],c[51]
        if s:
            self.solvestring+="Li, "
        display()
    def Di(self,s=True):
        c=self.colors
        c[42],c[43],c[44],  c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[51],c[48],c[45],c[52],c[49],c[46],c[53],c[50],c[47] = \
        c[15],c[16],c[17],  c[24],c[25],c[26],  c[33],c[34],c[35],  c[42],c[43],c[44],  c[45],c[46],c[47],c[48],c[49],c[50],c[51],c[52],c[53]
        if s:
            self.solvestring+="Di, "
        display()
    def MU(self):#TDi
        c=self.colors
        c[12],c[13],c[14],  c[21],c[22],c[23],  c[30],c[31],c[32],  c[39],c[40],c[41] = \
        c[21],c[22],c[23],  c[30],c[31],c[32],  c[39],c[40],c[41],  c[12],c[13],c[14]
        self.solvestring+="MU, "
        display()
    def MF(self):#FBi
        c=self.colors
        c[3],c[4],c[5],     c[19],c[22],c[25],  c[50],c[49],c[48],  c[43],c[40],c[37] = \
        c[43],c[40],c[37],  c[3],c[4],c[5],     c[19],c[22],c[25],  c[50],c[49],c[48]
        self.solvestring+="MF, "
        display()
    def MR(self):#RLi
        c=self.colors
        c[7],c[4],c[1],     c[16],c[13],c[10],  c[28],c[31],c[34],  c[52],c[49],c[46] = \
        c[16],c[13],c[10],  c[52],c[49],c[46],  c[7],c[4],c[1],  c[28],c[31],c[34]
        self.solvestring+="MR, "
        display()
    def spinBottom(self):
        self.MU()
        self.Di()
        display()
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
labels = []
if __name__ == "__main__":
    c = Cube(input("please enter the colours of the cube: ").upper())
    print(c)
