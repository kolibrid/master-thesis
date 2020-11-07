import csv

number_nodes = list()
number_edges = list()
norm_edges = list()
max_num_edges = 0

with open('./data/bloodEdges.dat') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        nodes, edges = int(row[0]), int(row[1])
        number_nodes.append(nodes)
        number_edges.append(edges)
        if edges > max_num_edges:
            max_num_edges = edges

for f in number_edges:
    norm_edges.append(round(f/max_num_edges, 3))

f = open("./data/bloodEdgesCDF.dat", "w+")
for i in range(0, len(number_nodes) - 1):
    f.write(str(number_nodes[i]) + ' ' + str(norm_edges[i]) + '\n')
f.close()
