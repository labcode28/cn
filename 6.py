CN program:
5. Take an example subnet of hosts and obtain a broadcast tree for the subnet.

Procedure:
1. Enter the number of nodes.
2. Create an adjacency matrix (n × n).
3. Fill the matrix with 0 (no edge) or 1 (edge exists).
4. Enter the root node.
5. Check which nodes have a 1 in that row (meaning connected).
6. Print all those nodes as adjacent to the root.
7. Run the program → it shows the adjacent nodes

                                                              def main():
    # Input the number of nodes
    n = int(input("Enter the number of nodes: "))

    # Initialize adjacency matrix
    adjacency_matrix = [[0] * (n + 1) for _ in range(n + 1)]

    print("Enter adjacency matrix:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adjacency_matrix[i][j] = int(input(f"Enter connection between node {i} and node {j} (0 or 1): "))

    # Input root node
    root = int(input("Enter the root node: "))

    # Display adjacent nodes of the root
    print(f"Adjacent nodes of root node {root}:")
    for j in range(1, n + 1):
        if adjacency_matrix[root][j] == 1:  # Check for connection
            print(j, end="\t")

    print("\n")  # Newline for clean output

if __name__ == "__main__":
    main()
