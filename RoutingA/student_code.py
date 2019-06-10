import heapq


def heuristic(a, b, graph):
    di = graph.intersections

    return abs(di[a][0] - di[b][0]) + abs(di[a][1] - di[b][1])


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def shortest_path(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    cost_so_far[start] = 0
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        for next in graph.roads[current]:
            print(next, cost_so_far[current], cost_so_far[next])
            new_cost = cost_so_far[current] + cost_so_far[next]

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next, graph)
                frontier.put(next, priority)
                came_from[next] = current

        res = [x for x in came_from]
        return res
