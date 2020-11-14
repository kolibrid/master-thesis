import csv
import collections

number_nodes = list()
number_edges = list()
cum_edges = list()
total_num_edges = 0
previous_value = 0

with open('./data/bloodEdges.dat') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        nodes, edges = int(row[0]), int(row[1])
        number_nodes.append(nodes)
        number_edges.append(edges)
        total_num_edges += edges

number_nodes, number_edges = zip(*sorted(zip(number_nodes, number_edges)))

for i in range(0, len(number_edges)):
    previous_value += number_edges[i]/total_num_edges
    cum_edges.append(round(previous_value, 3))

f = open("./data/bloodEdgesCDF.dat", "w+")
f.write("x f(x)\n")
for i in range(0, len(number_nodes)):
    f.write(str(number_nodes[i]) + ' ' + str(cum_edges[i]) + '\n')
f.close()
