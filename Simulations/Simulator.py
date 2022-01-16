import pygame
from Maze import Maze
from Agent3_Memory import maze_agent_memory

class Simulation:
    windowHeight = 700
    windowWidth = 700

    def __init__(self, limit, player, maze=None, start=None, goal=None):
        self._running = True
        self._display_surf = None
        self.maze = Maze(limit, maze, start, goal)
        self.agent = player(start_point=self.maze.get_start()) #maze_agent_memory(start_point=self.maze.get_start()) 
    
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
    simulation = Simulation(6, maze_agent_memory)
    simulation.on_execute()