from Rubik import Cube
c=Cube()
edgePairs=[(1,28),(3,37),(5,19),(7,10),
           (12,41),(14,21),(23,30),(32,39),
           (16,46),(25,50),(34,52),(43,48)]
cornerTriples=[(0,29,36),(2,20,27),(6,9,38),(8,11,18),
               (15,44,45),(17,24,47),(26,33,53),(35,42,51)]
def solve(cube = c):
    solveDCross(cube)
    cube.solvestring+="\nDCrossSolved\n"
    solveDCorners(cube)
    cube.solvestring+="\nDCornersSolved\n"
    solveMEdges(cube)
    cube.solvestring+="\nMedgesSolved\n"
    solveUCross(cube)
    cube.solvestring+="\nUCrossSolved\n"
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

if __name__ == "__main__":
    c = Cube(input("please enter the colours of the cube: ").upper())
    print(c)
    solve(c)
    print(c)
    c.shorten()
    print(c.solvestring)
    input()


































