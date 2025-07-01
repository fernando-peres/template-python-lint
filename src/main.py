"""
Main file - Hello World
"""

_var = "a variable"


def main() -> None:
    """
    Main function
    """

    print("Hello World!")

    print("a")
    print("b")
    print("c")


def foo() -> None:
    print("foo")


MY_LIST = [
    "Jane",
    "John",
    "Joe",
    "Jill",
    "Jack",
    "Jill",
    "Jane",
    "John",
    "Joe",
    "Jill",
    "Jack",
]

MY_DICT = {
    "key": "value",
    "key2": "value2",
    "key3": "value3",
}

long_string = "This is a very long line that exceeds the maximum allowed  line length for \
Python code. This is a very long line that exceeds the maximum allowed"

MY_TUPLE = (1, 2, 3)

if __name__ == "__main__":
    main()
