
if __name__ == '__main__':
    vertices, edges = map(int, input().split(' '))
    conn = [[] for _ in range(vertices)]
    for _ in range(edges):
        x, y = map(int, input().split(' '))
        conn[x].append(y)
        conn[y].append(x)
    visited_list = [False] * vertices

    def navigate(node, from_node):
        if visited_list[node]:
            print("Bad")
            exit()
        visited_list[node] = True
        for conn_node in conn[node]:
            if conn_node != from_node:
                navigate(conn_node, node)

    for i in range(len(visited_list)):
        if not visited_list[i]:
            navigate(i, None)
    print("Good")
