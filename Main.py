
from Maze import maze,COLOR,agent, textLabel
from BFS import BFS
import random

m=maze(100,100)
m.CreateMaze(loopPercent=100)

path=BFS(m)

a=agent(m,footprints=True,filled=True)

m.tracePath({a:path},delay=200,kill=True)
l=textLabel(m,'Length of Shortest Path',len(path)+1)
m.run()
