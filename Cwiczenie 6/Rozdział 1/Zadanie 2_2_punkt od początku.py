from pyamaze import maze, agent, textLabel
from queue import Queue

def breadthFirstSearch(m):
    start = (1, 1)  # Zmieniony punkt początkowy na (1, 1)
    goal = (m.rows // 2, m.cols // 2)  # Ustawienie punktu docelowego na środek labiryntu

    bfsPath = {}

    queue = Queue()
    queue.put(start)

    while not queue.empty():
        currCell = queue.get()

        if currCell == goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                if childCell not in bfsPath:
                    queue.put(childCell)
                    bfsPath[childCell] = currCell

    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    return fwdPath

if __name__ == '__main__':
    m = maze(25, 25)
    m.CreateMaze()
    path = breadthFirstSearch(m)

    a = agent(m, footprints=True, start=(1, 1))  # Ustawienie punktu początkowego agenta na (1, 1)
    m.tracePath({a: path})
    l = textLabel(m, 'Breadth-First Search Path Length', len(path) + 1)

    m.run()
