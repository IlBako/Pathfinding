from time import sleep
import Scripts

class Breadth_First_Search():

    queue = []

    def setup(self, maze):
        self.maze = maze
        #self.maze.print_maze()

    def run(self, pos):
        current = self.maze.get_Cell(pos)
        current.set_visited(True)
        self.queue.append(current)
        self.loop()
        #self.maze.print_maze()

    def loop(self):
        while(self.queue):
            current = self.queue.pop(0)
            #print(current.get_pos())
            for ng in current.get_neighbours():
                if ng.get_value() == 100:
                    print("FINITO!")
                    print("Final position is: " + str(ng.get_pos()))
                    return
                if not ng.get_visited():
                    ng.set_visited(True)
                    ng.set_parent(current)
                    self.queue.append(ng)                    
            #self.maze.print_maze()
            #print("\n")
            #sleep(0.5)

        