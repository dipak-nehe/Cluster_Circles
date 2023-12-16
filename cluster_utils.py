def reduce_clusters(ctuple_list):
    """
    Takes in an unordered list of ctuples. Identifies clusters of ctuples by overlapping area.
    Then returns a list of ctuples where each item in the list corresponds to one ctuple per
    cluster of the highest area.
    The length of the returned list should equal the number of clusters formed from the original
    ctuple list.

    :param ctuple_list: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
    :return: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
    """
    final_values_set = set()
    seen_before = set()

    for current_tuple in ctuple_list:
        seen_before.clear()
        reduce_clusters_recursive(current_tuple, seen_before, ctuple_list)
        max_cir = find_max_size_cir(seen_before)
        if max_cir:
            final_values_set.add(max_cir)
    return list(final_values_set)

def reduce_clusters_recursive(tuple, seen_before, ctuple_list):
    """
    Recursively find cluster of circles which overlap with each other
    :param tuple:
    :param seen_before: identified overlapping circles
    :param ctuple_list: input ctuples list
    :output:updates seen_before set with newly found intersecting circles
    """
    seen_before.add(tuple)
    for ctuple in ctuple_list:
        if ctuple not in seen_before and find_intersecting_tuples(tuple, ctuple):
            seen_before.add(ctuple)
            reduce_clusters_recursive(ctuple, seen_before, ctuple_list)


def find_intersecting_tuples(tuple1, tuple2):
    """
     Checks if two circles intersect based on their coordinates and radii
    :param tuple1: circle 1 to compare against another circle from the cluster
    :param tuple2: circle 2 to compare against another circle from the cluster
    :return: Boolean value based on if the circles are overlapping or not
    """
    x1, y1, r1 = tuple1
    x2, y2, r2 = tuple2
    c1c2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    return c1c2 <= (r1 + r2) ** 2

def find_max_size_cir(current_cluster_set):
    """
    Calculates the area of each circle in a cluster and returns the circle with the maximum area.
    :param current_cluster_set:Circles from current cluster
    :return:Circle with maximum area from current cluster
    """
    temp = 0
    max_tuple = None
    for ctuple in current_cluster_set:
        area_of_cir = 3.141592653589793 * ctuple[2] * ctuple[2]
        if temp < area_of_cir:
            temp = area_of_cir
            max_tuple = ctuple
    return max_tuple
