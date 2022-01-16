# Simulations

## About and Setup:
For a better visual representation of the agent in the maze I have made a GUI representation of the agent moving in the maze according to the agent. To achieve this, I have used 
pygame library. To use this on your device you will need to install the library which can be done using the below steps:
- If you prefer to create an environment for the project you can (Not necessary as we only need one library)
- For windows, open command prompt (or anaconda prompt if you use conda) and type `pip install pygame`
- For more details according your respective OS visit: https://www.pygame.org/wiki/GettingStarted

## Example run:
Once you have it installed on your device go open the python file you want to see and run the file. A new window will appear and you can see the agent run.
Few examples of how it will look like:  
<p align="center">
<img src="https://github.com/Nihal-Srivastava05/Maze-Solving-AI-Agent/blob/main/Simulations/Agent3Simulation1_gif.gif" width="450" height="500">  <img src="https://github.com/Nihal-Srivastava05/Maze-Solving-AI-Agent/blob/main/Simulations/Agent3Simulation2_gif.gif" width="450" height="500">
</p>

As we can see the red square is the agent and the black squares are walls. White lines are basically free spaces which the agent can move on and its goal is to reach the other end.

## Code layout and how to use:
- Here we have Maze.py file which contains the class Maze which is used to create our own maze or generate a maze randomly.
- To generate a maze randomly I have used Prims Randomized algorithm, reference:(https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e)
- Now you can either pass just a limit (Size of maze) to the Maze class and it will create a random maze or pass: limit, maze (which is a 2D array with entries as 'F' of free or empty cell and 'B' For blocked or wall, start (tuple with index for start state) and goal (tuple with index for goal state).
- Next we have an Agent. You can either create your own agent or use those I have made (Will be adding more as time goes). To it you need to pass the starting point (tuple with start indexes)
- Finally we have the Simulator class. This takes in either as limit and an agent as in input (Create its own maze using that limit) or take limit, player, maze, start and goal (Same values as above)
- Now you can import and call the Simulator class anywhere to run the simulation:
- `simulation = Simulation(6, maze_agent_memory)` //Maze of size - 6 with maze_agent_memory as the agent
  `simulation.on_execute()` //To run the simulation
