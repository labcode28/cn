# Distance Vector Routing Algorithm Implementation in Python

def initialize_network(num_nodes):
    """
    Initialize the distance matrix for the network.
    Set the distance between each pair of nodes.
    """
    print("\nEnter the cost matrix for the network (use 999 for no direct connection):")
    distance_matrix = []
    for i in range(num_nodes):
        row = list(map(int, input(f"Enter costs for node {i} to all nodes: ").split()))
        distance_matrix.append(row)
    return distance_matrix


def distance_vector_routing(num_nodes, distance_matrix):
    """
    Perform the Distance Vector Routing algorithm.
    Calculate the routing table for each node iteratively until convergence.
    """
    routing_tables = [[float("inf")] * num_nodes for _ in range(num_nodes)]
    
    # Initialize the routing tables with direct distances
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                routing_tables[i][j] = 0
            else:
                routing_tables[i][j] = distance_matrix[i][j]
    
    # Iteratively update routing tables
    converged = False
    iteration = 0
    while not converged:
        converged = True
        iteration += 1
        print(f"\nIteration {iteration}:")

        for i in range(num_nodes):
            for j in range(num_nodes):
                for k in range(num_nodes):
                    if routing_tables[i][j] > routing_tables[i][k] + routing_tables[k][j]:
                        routing_tables[i][j] = routing_tables[i][k] + routing_tables[k][j]
                        converged = False
        
        # Print intermediate routing tables
        for i in range(num_nodes):
            print(f"Routing table for node {i}: {routing_tables[i]}")
    
    return routing_tables


def main():
    """
    Main function to execute the Distance Vector Routing Algorithm.
    """
    print("Distance Vector Routing Algorithm")
    num_nodes = int(input("\nEnter the number of nodes in the network: "))
    distance_matrix = initialize_network(num_nodes)
    routing_tables = distance_vector_routing(num_nodes, distance_matrix)

    # Print final routing tables
    print("\nFinal Routing Tables:")
    for i in range(num_nodes):
        print(f"Node {i}: {routing_tables[i]}")


if __name__ == "__main__":
    main() 6. Implement distance vector routing algorithm for obtaining routing tables at 
each node.
Procedure:
1. Enter the number of nodes.
2. Enter the cost matrix (use 999 for no direct link).
3. Initialize each node’s routing table with direct distances.
4. For every node → check if a shorter path exists through another node.
5. Update the routing table if a shorter path is found.
6. Repeat until no changes occur (convergence).
7. Print routing tables after each iteration.
8. Print the final routing tables when all are stable.
9. Run the program → see how distances update until convergence
