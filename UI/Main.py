from UI.Maze import maze,COLOR,pel, textLabel
from Model.BFS import BFS
from Model.DFS import DFS
m=maze(5,5)
#Vẽ mê cung

m.createMaze(loopPercent=100)
search, path = DFS(m)

a=pel(m,color = COLOR.blue)
b=pel(m)


m.tracePath({a:search},delay=100)
m.tracePath({b:path},delay=100)
l=textLabel(m,'Length of Shortest Path',len(path)+1)
m.run()