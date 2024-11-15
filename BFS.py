from collections import deque
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        # start clean
        self.frontier = deque([])
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)

        # open list
        self.frontier.append(initialstate)

        # while we have states in open list
        while len(self.frontier) > 0:
            shallowest_node = self.frontier.popleft()  # FIFO queue
            self.explored_set.append(shallowest_node)

            # get neighbors
            neighbors = self.get_neighbors(shallowest_node)

            # for each neighbor
            for neighbor in neighbors:
                if neighbor in self.explored_set or neighbor in self.frontier:
                    continue  # skip already explored or queued nodes

                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
                    continue  # skip invalid paths

                neighbor.parent = shallowest_node  # mark parent
                self.frontier.append(neighbor)  # add to frontier

                if neighbor.equal(goalstate):
                    return self.get_path(neighbor)
        return None