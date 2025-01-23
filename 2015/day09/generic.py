import networkx as nx

def part1():
    G = nx.DiGraph() 
    result = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            G.add_weighted_edges_from([(line[0],line[2], line[4])])

    print(f"{G.nodes.items() }")
    print(f"{G.edges.items() }")
    print(f"part 1: {result}") 


def part2():
    result = {}
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            pass
            
    print(f"part 2: {result}") 


if __name__ == "__main__":
    part1()
    part2()
