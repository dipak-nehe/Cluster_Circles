from cluster_utils import reduce_clusters

def testcase_for_recursive(input_list, expected):
    """
    testcases to validate function reduce_clusters in cluster_utils.py
    :param input_list: An unordered list of ctuples
    :param expected: Expected output to compare against actual output
    :return: Asserts if the values are equal or not
    """
    actual = reduce_clusters(input_list)
    assert sorted(actual) == sorted(expected), "The returned cluster list does not match with expected cluster list"

#tests from the given exercise
testcase_for_recursive([(0.5, 0.5, 0.5), (1.5, 1.5, 1.1), (0.7, 0.7, 0.4), (4, 4, 0.7)], [(1.5, 1.5, 1.1), (4, 4, 0.7)])
testcase_for_recursive([(1, 3, 0.7), (2, 3, 0.4), (3, 3, 0.9)],[(3, 3, 0.9)])
testcase_for_recursive([(1.5,1.5,1.3),(4,4,0.7)],[(1.5,1.5,1.3),(4,4,0.7)])
#testcase where only one circle was given as input
testcase_for_recursive([(1.5, 1.5, 1.5)], [(1.5, 1.5, 1.5)])
#testcase with empty input list
testcase_for_recursive([], [])
#test with two circles with same data
testcase_for_recursive([(1.5, 1.5, 1.3),(1.5, 1.5, 1.3)],[(1.5, 1.5, 1.3)])
#testcase for multiple clusters in the input
testcase_for_recursive([(0.5,0.5,0.5),(0.7,0.7,0.7),(4,4,0.7),(3,5,0.9)],[(3, 5, 0.9), (0.7, 0.7, 0.7)])
