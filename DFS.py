def DFS(m):
    start = (m.rows, m.cols)
    visited = [start]
    stack = [start]
    dfsPath = {}
    search = []
    while len(stack) > 0:
        # xóa phần tử ở vị trí cuối
        currCell = stack.pop()
        search.append(currCell)
        if currCell == m._goal:
            break
        for d in "WNSE":
            if m.maze_map[currCell][d] == True:
                if d == "E":
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == "W":
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == "S":
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == "N":
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in visited:
                    continue
                visited.append(childCell)
                stack.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return search, fwdPath
