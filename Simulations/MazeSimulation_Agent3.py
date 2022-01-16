import pygame
import random

cust_maze = [['F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
             ['F', 'B', 'F', 'B', 'B', 'F', 'B', 'B'],
             ['F', 'B', 'F', 'F', 'B', 'F', 'B', 'F'],
             ['F', 'B', 'B', 'B', 'B', 'F', 'B', 'F'],
             ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
             ['B', 'F', 'B', 'B', 'B', 'B', 'B', 'F'],
             ['B', 'F', 'F', 'F', 'F', 'F', 'B', 'F'],
             ['F', 'F', 'B', 'B', 'F', 'B', 'B', 'F'],]

cust_maze2 = [['F', 'F', 'B', 'B', 'F'],
              ['F', 'F', 'B', 'B', 'B'],
              ['B', 'F', 'F', 'F', 'F'],
              ['B', 'B', 'F', 'B', 'F'],
              ['B', 'B', 'B', 'B', 'F']]

cust_maze3 = [['F', 'F', 'F', 'B', 'B'],
              ['F', 'F', 'B', 'B', 'F'],
              ['F', 'B', 'B', 'B', 'B'],
              ['F', 'B', 'F', 'F', 'F'],
              ['F', 'F', 'F', 'B', 'F']]

cust_maze4 = [['F', 'F', 'B',]]

class self_driving_agent_memory:
    def __init__(self):
        self.x = 0
        self.y = 0
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

class Maze:
    def __init__(self, maze, limit, goal):
        self.limit = limit
        self.goal = goal
        self.maze = maze
    
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

class Simulation:
    windowHeight = 500
    windowWidth = 500

    def __init__(self, maze, goal):
        self._running = True
        self._display_surf = None
        self.maze = Maze(maze, len(maze), goal)
        self.agent = self_driving_agent_memory() 
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Maze Solver')
        self._running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((255, 255, 255))
        self.maze.draw(self._display_surf)
        self.agent.draw(self._display_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        agent_final_status = True
        agent_stop = False
        while(self._running):
            pygame.event.pump()

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_ESCAPE]):
                self._running = False

            if(not agent_stop):
                agent_stop = not self.agent.move(self.maze)
            else:
                result_font = pygame.font.Font('freesansbold.ttf', 16)
                result_text = result_font.render(self.agent.result, True, (0, 0, 0))
                result_text_rect = result_text.get_rect()
                result_text_rect.center = (self.windowWidth//2, self.windowHeight-25)
                self._display_surf.blit(result_text, result_text_rect)

                if(agent_final_status):
                    ticks = pygame.time.get_ticks()
                ticks_font = pygame.font.Font('freesansbold.ttf', 16)
                ticks_text = ticks_font.render("Time taken by the agent: {} milliseconds".format(ticks), True, (0, 0, 0))
                ticks_text_rect = ticks_text.get_rect()
                ticks_text_rect.center = (self.windowWidth//2, result_text_rect[1]-25)
                self._display_surf.blit(ticks_text, ticks_text_rect)
                agent_final_status = False
            
            for event in pygame.event.get():
                self.on_event(event)

            pygame.display.update()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    simulation = Simulation(cust_maze, (7, 7))
    simulation.on_execute()