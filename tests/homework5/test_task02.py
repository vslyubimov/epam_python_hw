from homework5.task02 import print_result


def test_custom_wrap_decorator():
    @print_result
    def function_name(a, b):
        """test_docstring"""
        return a * b

    assert str(function_name.__doc__) == "test_docstring"
    assert str(function_name.__name__) == "function_name"
