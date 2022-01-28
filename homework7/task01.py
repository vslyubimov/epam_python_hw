"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree, element):
    return 1 if tree == element else find_occurrences_recursive(tree, element)


def find_occurrences_recursive(tree, element):
    found = 0
    found += go_down(tree, element)
    if isinstance(tree, dict):
        found += go_down(tree.values(), element)
    return found


def count_increment(checked, element):
    return 1 if checked == element else 0


def check_nested_dict(value, element):
    return find_occurrences_recursive(value, element) \
        if isinstance(value, dict) else 0


def check_nested_list(checked, element):
    return go_down(checked, element) if isinstance(checked, list) else 0


def go_down(checked, element):
    found = 0
    for item in checked:
        found += check_nested_list(item, element)
        found += check_nested_dict(item, element)
        found += count_increment(item, element)
    return found
