import pprint

def read_graph(filename, directed = False):
    graph = {}
    with open(filename) as input_file:
        for line in input_file:
            parts = line.split()
            if len(parts) !=3:
                continue
            [n1,n2,w] = [ int(x) for x in parts]
            if n1 not in graph:
                graph[n1] = []
            if n2 not in graph:
                graph[n2] = []
            graph[n1].append((n1, w))
    return graph

g = read_graph("DijkstrasFirst.txt")
pprint.pprint(g)
