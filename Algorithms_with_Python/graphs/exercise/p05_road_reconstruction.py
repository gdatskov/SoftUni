buildings_number = int(input())  # Nodes
streets_number = int(input())    # Edges
network = {b: [] for b in range(buildings_number)}
for street in range(streets_number):
    start, destination = [int(x) for x in input().split(" - ")]
    network[start].append(destination)
    network[destination].append(start)

# print(*network.items(), sep="\n")
# print()

important_streets = []
# all_streets_removed = False
for _ in range(streets_number):
    for building in range(buildings_number):
        if building in network:
            if len(network[building]) == 1:
                destination = network[building][0]
                network[destination].remove(building)
                important_streets.append(sorted((building, destination)))
                del network[building]

    # all_streets_removed = True


print("Important streets:")
for street in important_streets:
    print(" ".join(str(x) for x in street))

