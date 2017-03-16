import math


def calculate_distance(p0, p1):
    dif_x = p0[0] - p1[0]
    dif_y = p0[1] - p1[1]
    return dif_x * dif_x + dif_y * dif_y


def ternary_search(vertices, p):
    v0, v4 = vertices
    for _ in xrange(125):
        v2 = (v0[0] - (v0[0] - v4[0]) / 3.0, v0[1] - (v0[1] - v4[1]) / 3.0)
        v3 = (v4[0] - (v4[0] - v0[0]) / 3.0, v4[1] - (v4[1] - v0[1]) / 3.0)
        if calculate_distance(v3, p) < calculate_distance(v2, p):
            v0 = v2
        else:
            v4 = v3
    return calculate_distance(p, v0)

if __name__ == '__main__':
    num_values, p_x, p_y = map(int, raw_input().split(' '))
    p = (p_x, p_y)
    furthest_distance = 0
    old_distance = 0
    old_point = None
    shortest_distance = 20000000000000000000
    first_point = None
    for i in xrange(num_values):
        vertex = [float(j) for j in raw_input().split(' ')]
        distance = calculate_distance(vertex, p)
        if distance > furthest_distance:
            furthest_distance = distance
        if old_point is not None:
            distance = ternary_search((vertex, old_point), p)
            if distance < shortest_distance:
                shortest_distance = distance
        else:
            first_point = vertex
        if i == num_values - 1:
            distance = ternary_search((vertex, first_point), p)
            if distance < shortest_distance:
                shortest_distance = distance
        old_point = vertex
        old_distance = distance
    # print("furthest", furthest_distance, "shortest", shortest_distance)
    print(math.pi * furthest_distance - math.pi * shortest_distance)
