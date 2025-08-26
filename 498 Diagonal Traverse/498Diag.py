class Solution(object):
    def findDiagonalOrder(self, mat):
        Direction = "Up"
        rows = len(mat)
        cols = len(mat[0])
        xcount = 0
        ycount = 0
        path = []
        for i in range(rows*cols):
            path.append(mat[xcount][ycount])
            if Direction == "Up":        #[0][2]
                if(ycount + 1 >= cols ):
                    Direction = "Down" 
                    xcount += 1      #[-1][2]
                                     #[1][2]
                elif(xcount - 1 < 0):
                    Direction = "Down" 
                    ycount += 1 
                else:
                    xcount -= 1
                    ycount += 1

            elif Direction == "Down":
                if(xcount + 1 >= rows): #[2][1]
                    Direction = "Up" 
                    ycount += 1 #[2][0]
                                #[2][2]
                elif(ycount - 1 < 0):
                    Direction = "Up" 
                    xcount += 1 
                else:
                    xcount += 1
                    ycount -= 1
        return path