from unittest.mock import MagicMock


def my_function(a, b):
    return a + b


mock_function = MagicMock(return_value=3)
result = mock_function(1, 2)
try:
    assert result == 3
    print("Pass")
except AssertionError:
    print("Fail")


class MyClass:
    def my_method(self, a, b):
        return a + b

    def test(self):
        mock_obj = MagicMock(spec=MyClass)
        mock_obj.my_method.return_value = 4

        result = mock_obj.my_method(1, 2)
        try:
            assert result == 3
            print("Pass")
        except AssertionError:
            print("Fail")


inst = MyClass()
inst.test()
