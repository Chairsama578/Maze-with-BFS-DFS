from Maze import maze,COLOR,agent, textLabel
from BFS import BFS
from DFS import DFS
#Khơi tạo mê cung 100x100
m=maze(10,10)
#Tạo 
m.CreateMaze(loopPercent=100)
search, path=BFS(m)

a=agent(m,color = COLOR.blue)
b=agent(m)

m.tracePath({a:search},delay=100)
m.tracePath({b:path},delay=100)
l=textLabel(m,'Length of Shortest Path',len(path)+1)
m.run()