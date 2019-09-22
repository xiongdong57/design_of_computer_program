Fail = []


def pour_problem(X, Y, goal, start=(0, 0)):
    """X and Y are the capacity of glass. (x, y) is the current fill levels
    and represents a state. The goal is a level that can be in either glass.
    start at start state and follow successors until we reach the goal.
    keep track of frontier and perviously explored.fial when no froniter."""
    if goal is start:
        return [start]
    explored = set()
    froniter = [[start]]
    while froniter:
        path = froniter.pop(0)
        x, y = path[-1]
        for state, action in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    froniter.append(path2)

    return Fail


def successors(x, y, X, Y):
    """return a dict of {state: action} describle whath can be reached from
    (x, y) sate and how"""
    assert x <= X and y <= Y
    return {(X, y): 'fill X', (x, Y): 'fill Y',
            (0, y): 'empty X', (x, 0): 'empty Y',
            (0, y+x) if y + x <= Y else (x-(Y-y), y+(Y-y)): 'X->Y',
            (x+y, 0) if x + y <= X else (x+(X-x), y-(X-x)): 'X<-Y'}


print(pour_problem(4, 9, 7))
