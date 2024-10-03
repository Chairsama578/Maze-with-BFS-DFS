
from Maze import maze,COLOR,agent
import random

m=maze(100,100)
m.CreateMaze(loopPercent=100)

a=agent(m,footprints=True,filled=True)

m.tracePath({a:m.path},delay=200,kill=True)

m.run()
