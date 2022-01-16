import pygame
import random

class maze_agent_memory:
    def __init__(self, start_point=None):
        if(start_point == None):
            self.x = 0
            self.y = 0
        else:
            self.x = start_point[0]
            self.y = start_point[1]
        self.total_steps = 0
        self.surrondings = None
        self.memory = []
        self.recentlyPoped = []
        self.prev_move = -1
        self.result = ''

    def draw(self, display):
        draw_x = self.x
        draw_y = self.y
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(draw_y*50, draw_x*50, 50, 50))
        pygame.time.wait(100)
    
    def move(self, env):
        if(self.x == env.get_goal()[0] and self.y == env.get_goal()[1]):
            print("You have solved the maze and reached the end...")
            self.result = 'Maze Solved, I reached the end...'
            return False
        elif(self.total_steps >= env.limit*env.limit):
            print("Did not halt, mostly unsolvable maze...")
            self.result = 'Did not halt, mostly unsolvable maze...'
            return False
        else:
            self.surrondings = [env.get_position(self.x+1, self.y),
                                env.get_position(self.x, self.y+1),
                                env.get_position(self.x-1, self.y), 
                                env.get_position(self.x, self.y-1)]
            possible_moves = []
            num_moves = 0
            for i in range(len(self.surrondings)):
                if self.surrondings[i] == 'F':
                    possible_moves.append(i)
                    num_moves += 1
            
            if(self.prev_move == 0):
                if(2 in possible_moves):
                    possible_moves.remove(2)
            elif(self.prev_move == 2):
                if(0 in possible_moves):
                    possible_moves.remove(0)
            elif(self.prev_move == 1):
                if(3 in possible_moves):
                    possible_moves.remove(3)
            elif(self.prev_move == 3):
                if(1 in possible_moves):
                    possible_moves.remove(1)
                    
            if(num_moves > 1):
                if(not self.recentlyPoped):
                    self.memory.append([self.x, self.y])
                elif(not(self.recentlyPoped[0] == self.x and self.recentlyPoped[1] == self.y)):
                    self.memory.append([self.x, self.y])
            
            if(possible_moves):
                random_move = random.choice(possible_moves)
                if(random_move == 0):
                    self.x += 1
                    self.prev_move = 0
                elif(random_move == 1):
                    self.y += 1
                    self.prev_move = 1
                elif(random_move == 2):
                    self.x -= 1
                    self.prev_move = 2
                elif(random_move == 3):
                    self.y -= 1
                    self.prev_move = 3
                else:
                    print("Maze is blocked for all the places...")
                    self.result = 'Maze is blocked for all the places...'
                    return False
            else:
                if(not self.memory):
                    print("Unsolvable maze, no route to exit...")
                    self.result = 'Unsolvable maze, no route to exit...'
                    return False
                last_choice_position = self.memory.pop(0)
                self.x = last_choice_position[0]
                self.y = last_choice_position[1]
                self.recentlyPoped = last_choice_position
                self.total_steps = 0
            
            self.total_steps += 1
            return True

    def tell_pos(self):
        print("I am currently at the position ({}, {})".format(self.x, self.y))