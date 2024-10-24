from Maze import maze,COLOR,pel, textLabel
from BFS import BFS
from DFS import DFS
m=maze(5,5)
#Vẽ mê cung

m.CreateMaze(loopPercent=100)
search, path = BFS(m)

a=pel(m,color = COLOR.blue)
b=pel(m)


m.tracePath({a:search},delay=500)
m.tracePath({b:path},delay=100)
l=textLabel(m,'Length of Shortest Path',len(path)+1)
m.run()