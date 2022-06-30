class Maze():

    MAZE_SIZE = 9

    ascii_maze = [
        ["#", "@", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
    ]

    maze = []

    start_pos = "@"
    end_pos = "X"

    def __init__(self):
        for i, row in enumerate(self.ascii_maze):
            self.maze.append([])
            for j, col in enumerate(row):
                self.maze[i].append(Cell(col))
        for i, row in enumerate(self.ascii_maze):
            for j, col in enumerate(row):
                ngs = []
                for pos in self.find_neighbour(i,j):
                    ngs.append(self.maze[i+pos[0]][j+pos[1]])
                self.maze[i][j].set_neighbours(ngs)
                

    def find_start(self):
        for i, row in enumerate(self.maze):
            for j, value in enumerate(row):
                if value == self.start_pos:
                    return i,j

    def find_neighbour(self, cell_pos_x, cell_pos_y):
        avb_pos = [[-1, 0], [1, 0], [0,1], [0, -1]]
        ngs = []
        for pos in avb_pos:
            x = cell_pos_x + pos[0]
            y = cell_pos_y + pos[1]
            if any([x<0, y<0, x>=self.MAZE_SIZE, y>=self.MAZE_SIZE]):
                pass
            else:
                ngs.append(pos)
        
        return ngs

    def print_maze(self):
        for row in self.maze:
            print([col.get_value() for col in row])

class Cell():
    _neighbours: list()
    _value: chr
    
    _is_visited = False
    
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_neighbours(self, neighbours):
        self._neighbours = neighbours

    def get_neighbours(self):
        return self._neighbours

    def set_visited(self, value: bool):
        self._is_visited = value

    def get_visited(self):
        return self._is_visited
