def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    search = []
    while len(frontier) > 0:
        # xóa phần tử ở vị trí đầu
        currCell = frontier.pop(0)
        search.append(currCell)
        if currCell == m._goal:
            break
        for d in "NWSE":
            if m.maze_map[currCell][d] == True:
                if d == "E":
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == "N":
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == "S":
                    childCell = (currCell[0] + 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return search, fwdPath
