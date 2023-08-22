def main():
    n, m = map(int, input("Enter the number of vertices (N) and edges (M): ").split())
    u, v = 0, 0
    degrees = [0] * n
    edge_types = [-1] * m

    print("Initial degrees:", degrees)
    print("Initial edge types:", edge_types)

    if m % 2 != 0 and n % 2 != 0:
        print("The combination of odd edges and odd vertices is not allowed.")
    else:
        for i in range(m):
            u, v = map(int, input(f"Enter the vertices for edge {i+1}: ").split())
            if degrees[u - 1] % 2 == 0 and degrees[v - 1] % 2 == 0:
                edge_types[i] = 0
                degrees[v - 1] += 1
            elif degrees[u - 1] % 2 != 0 and degrees[v - 1] % 2 == 0:
                edge_types[i] = 1
                degrees[u - 1] += 1
            elif degrees[u - 1] % 2 == 0 and degrees[v - 1] % 2 != 0:
                degrees[v - 1] += 1
                edge_types[i] = 1

        for degree in degrees:
            if degree % 2 != 0:
                print("There's a vertex with an odd degree, the graph is not valid.")
                exit(0)

        print("Final edge types:", edge_types)

if __name__ == "__main__":
    main()
