
adj_matrix = [[2,2,2] for _ in range(5)]

def getEulerCircuit(here, circuit):
    for vertex in adj_matrix[here]:

        while adj_matrix[here][vertex] > 0:
            adj_matrix[here][vertex] -= 1
            adj_matrix[vertex][here] -= 1
            getEulerCircuit(vertex, circuit)

    circuit.append(here)    

print(getEulerCircuit(0,[]))
    