from pyamaze import maze, agent, textLabel

def recursiveSearch(m, currCell, path, marked):
    if currCell == (1, 1):
        return True
    
    x, y = currCell
    marked.add(currCell)
    
    for d in 'ESNW':
        if m.maze_map[currCell][d] == True:
            if d == 'E':
                childCell = (x, y + 1)
            elif d == 'W':
                childCell = (x, y - 1)
            elif d == 'N':
                childCell = (x - 1, y)
            elif d == 'S':
                childCell = (x + 1, y)
            
            if childCell not in marked:
                path[childCell] = currCell
                if recursiveSearch(m, childCell, path, marked):
                    return True

    marked.remove(currCell)
    return False

if __name__ == '__main__':
    m = maze(35, 35)
    m.CreateMaze()
    
    start = (m.rows, m.cols)
    path = {}
    marked = set()
    
    if recursiveSearch(m, start, path, marked):
        fwdPath = {}
        cell = (1, 1)
        
        while cell != start:
            fwdPath[path[cell]] = cell
            cell = path[cell]
        
        a = agent(m, footprints=True)
        m.tracePath({a: fwdPath})
        l = textLabel(m, 'Recursive Search Path Length', len(fwdPath) + 1)
        m.run()
    else:
        print("No path found!")
