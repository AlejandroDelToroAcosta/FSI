class Order(Queue):
    def _init_(self):
        self.A = []
        self.start = 0
        self.keep = set()


    def append(self, item):
        self.A.append(item)

    def _len_(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)
        self.A = sorted(self.A, key=lambda node_x: node_x.path_cost)
        print(self.A)


    def pop(self):
        while self.A:
            e = self.A.pop(0)
            if e.state not in self.keep:
                self.keep.add(e.state)
                return e
        return None


class euristicList(Queue):
    def _init_(self, problem):
        self.A = []
        self.start = 0
        self.p = problem
        self.keep = set()

    def append(self, item):
        self.A.append(item)

    def _len_(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)
        self.A = sorted(self.A, key=lambda node_x: node_x.path_cost + search.GPSProblem.h(self.p, node_x))
        print(self.A)


    def pop(self):
        while self.A:
            e = self.A.pop(0)
            if e.state not in self.keep:
                self.keep.add(e.state)
                return e
        return None


def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None
