import pygame

# inialize the pygame
pygame.init()

white = (255, 255, 255)
black = (198,238,78)

# create the screen
# (width, height)
screen_width = 850
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(black)
# caption and icon
pygame.display.set_caption("Matrix Practice")


matrix = [
    [1,1,0,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]

    ]
#creates a grid from the matrix
# grid = Grid(matrix=matrix)
# start = grid.node(0,0)
# end = grid.node(3,0)

# class setup:
#     def createFinder(self):
#         #create a new instance of a finder
#         self.finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
#         #The find_path function returns 2 values, the amounrs of times it runs to --
#         #-- find a path(runs) and the length of the finished path(path)
#         self.path, self.runs = self.finder.find_path(start, end, grid)
#         print(self.path)

#     def showPath(self):
#         print('operations', self.runs, 'path length:', len(self.path))
#         print(grid.grid_str(path=self.path, start=start, end=end))


def visualizeGrid(self):
    x = 0
    y = 0
    z = 0
    w = 0
    v = 0
    while w <=3:
        pygame.display.update()
        for i in matrix[z]:
            print("The matrix is ", matrix[z],"and Z is: ", i)
            v += 1
            x += x + 11
            if x >= 700:
                x = 0
                y += 11
            
            if v == 4:
                i += 1
                z+=1
                if z >= 4:
                    z = 0
                v = 0
                pygame.draw.rect(self, black, [x,y,10,10])
        w+1
                
visualizeGrid(screen)