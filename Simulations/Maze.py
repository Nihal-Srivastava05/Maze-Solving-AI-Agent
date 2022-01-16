import pygame
from MazeGenerator import MazeGenerator

class Maze:
    def __init__(self, limit, maze=None, start=None, goal=None):
        if(maze == None):
            maze_generator = MazeGenerator(limit, limit)
            created_maze = maze_generator.generate_maze()
            self.limit = limit
            self.maze = created_maze[0]
            self.start = created_maze[1]
            self.goal = created_maze[2]
        else:
            self.limit = limit
            self.start = start
            self.goal = goal
            self.maze = maze
    
    def get_start(self):
        return self.start
    
    def draw(self, display):
        dx = 0
        dy = 0
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(0, 0, self.limit*50, self.limit*50), width=1)
        for i in range(0, self.limit ):
            for j in range(0, self.limit):
                if(self.maze[i][j] == 'B'):
                    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(dx*50, dy*50, 50, 50))
                dx = dx + 1
                if dx > self.limit-1:
                    dx = 0 
                    dy = dy + 1
    
    def get_limit(self):
        return self.limit
    
    def show_maze(self):
        for i in range(self.limit):
            for j in range(self.limit):
                print(self.maze[i][j], end=" ")
            print()
    
    def get_goal(self):
        return self.goal
    
    def get_position(self, x, y):
        if(x > self.limit-1 or y > self.limit-1):
            return 'B'
        if(x < 0 or y < 0):
            return 'B'
        return self.maze[x][y]
    