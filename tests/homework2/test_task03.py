from homework2.task03 import combinations, combinations_v2

test_data_1 = [1, 2], [3, 4]
test_data_2 = [1, 2, 3], [3, 4, 5], [5, 6]
end_result_1 = [[1, 3], [1, 4], [2, 3], [2, 4]]
end_result_2 = [[1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [1, 5, 5],
                [1, 5, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
                [2, 5, 5],
                [2, 5, 6],
                [3, 3, 5],
                [3, 3, 6],
                [3, 4, 5],
                [3, 4, 6],
                [3, 5, 5],
                [3, 5, 6]]


def test_combinations_test_data_1():
    assert combinations(*test_data_1) == end_result_1


def test_combinations_test_data_2():
    assert combinations(*test_data_2) == end_result_2


def test_combinations_v2_test_data_1():
    assert combinations_v2(*test_data_1) == end_result_1


def test_combinations_v2_test_data_2():
    assert combinations_v2(*test_data_2) == end_result_2
